import numpy as np
import pandas as pd
from pandas.plotting import lag_plot
import matplotlib.pyplot as plt

import pmdarima as pm
from pmdarima.arima import ndiffs
from pmdarima.metrics import smape
from sklearn.metrics import mean_squared_error

print(f"Using pmdarima {pm.__version__}")


def autoCorrelationPlot(data):
    """
    MSFT 自相关差分图
    """
    fig, axes = plt.subplots(3, 2, figsize=(8, 12))
    plt.title('MSFT Autocorrelation plot')

    # The axis coordinates for the plots
    ax_idcs = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (2, 0),
        (2, 1)
    ]

    for lag, ax_coords in enumerate(ax_idcs, 1):
        ax_row, ax_col = ax_coords
        axis = axes[ax_row][ax_col]
        lag_plot(data, lag=lag, ax=axis)
        axis.set_title(f"Lag={lag}")

    plt.show()


def KPSS_ADF_test(data):
    """
    使用KPSS测试和 ADF测试，在两者之间选择一个最大值作为保守值
    """
    kpss_diffs = ndiffs(x_train, alpha=0.05, test='kpss', max_d=6)
    adf_diffs = ndiffs(x_train, alpha=0.05, test='adf', max_d=6)
    n_diffs = max(adf_diffs, kpss_diffs)

    print(f"Estimated differencing term: {n_diffs}")
    return n_diffs


def forecast_one_step(model):
    fc, conf_int = model.predict(n_periods=1, return_conf_int=True)
    return fc[0], conf_int[0]


def finalplot(traindata, testdata, forecasts):
    fig, axes = plt.subplots(2, 1, figsize=(12, 12))

    # --------------------- Actual vs. Predicted --------------------------
    axes[0].plot(traindata, color='blue', label='Training Data')
    axes[0].plot(range(len(traindata)-1, len(traindata)+len(forecasts)-1), forecasts, color='green', marker='o',
                 label='Predicted Price')

    axes[0].plot(range(len(traindata)-1, len(traindata)+len(forecasts)-1), testdata, color='red', label='Actual Price')
    axes[0].set_title('Microsoft Prices Prediction')
    axes[0].set_xlabel('Dates')
    axes[0].set_ylabel('Prices')

    # axes[0].set_xticks(np.arange(0, 7982, 1300).tolist(), df['Date'][0:7982:1300].tolist())
    axes[0].legend()

    # ------------------ Predicted with confidence intervals ----------------
    axes[1].plot(traindata, color='blue', label='Training Data')
    axes[1].plot(range(len(traindata)-1, len(traindata)+len(forecasts)-1), forecasts, color='green',
                 label='Predicted Price')

    axes[1].set_title('Prices Predictions & Confidence Intervals')
    axes[1].set_xlabel('Dates')
    axes[1].set_ylabel('Prices')

    conf_int = np.asarray(confidence_intervals)
    axes[1].fill_between(range(len(traindata)-1, len(traindata)+len(forecasts)-1),
                         conf_int[:, 0], conf_int[:, 1],
                         alpha=0.9, color='orange',
                         label="Confidence Intervals")

    # axes[1].set_xticks(np.arange(0, 7982, 1300).tolist(), df['Date'][0:7982:1300].tolist())
    axes[1].legend()
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('./data/sock.csv')
    data = data['open']
    # print(data.shape)

    # autoCorrelationPlot(data)

    x_train, x_test = data.values[0:int(data.shape[0] * 0.8)], data.values[int(data.shape[0] * 0.8)::]

    n_diffs = KPSS_ADF_test(x_train)

    arima = pm.auto_arima(x_train, d=n_diffs,
                          seasonal=False, stepwise=True,
                          suppress_warnings=True, error_action="ignore", max_p=6, max_order=None, trace=True)

    # arima = pm.auto_arima(data, start_p=1, start_q=1,
    #                       max_p=3, max_q=3, m=12,
    #                       start_P=0, seasonal=True,
    #                       d=1, D=1, trace=True,
    #                       error_action='ignore',
    #                       suppress_warnings=True,
    #                       stepwise=True)

    # arima = pm.auto_arima(data, start_p=1, start_q=1, max_p=9, max_q=6, max_d=3, max_order=None,
    #                       seasonal=False, m=1, test='adf', trace=False,
    #                       error_action='ignore',  # don't want to know if an order does not work
    #                       suppress_warnings=True,  # don't want convergence warnings
    #                       stepwise=True, information_criterion='bic', njob=-1)  # set to stepwise
    # # 把训练数据放入auto_arima得到最优模型，ARIMA里的三个参数PDQ都是可以进行自动调参的，就是通过调整start_p和max_p
    print('arima_AIC is:', arima.aic())
    print('arima_order is:', arima.order)

    # fc, conf_int = forecast_one_step(arima)
    # print(pre[0])
    # print(conf_int[0])
    # print(pre.tolist()[0])
    # print(np.asarray(conf_int).tolist()[0])

    forecasts = []
    confidence_intervals = []
    for new_ob in x_test:
        fc, conf = forecast_one_step(arima)
        forecasts.append(fc)
        confidence_intervals.append(conf)

        # Updates the existing model with a small number of MLE steps
        arima.update(new_ob)
    print(f"Mean squared error: {mean_squared_error(x_test, forecasts)}")
    print(f"SMAPE: {smape(x_test, forecasts)}")

    finalplot(x_train, x_test, forecasts)

