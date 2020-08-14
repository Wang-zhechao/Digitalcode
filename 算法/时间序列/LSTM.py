from keras.models import Sequential
from keras.layers import Dense, LSTM, BatchNormalization
from sklearn.preprocessing import MinMaxScaler

import argparse
import pandas as pd
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt


def create_model(steps, features):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(steps, features)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model


def get_dataset():
    # # 从csv读取数据
    # data = pd.read_csv('./data/stockdata.csv')

    # 从tushare读取股票数据
    pro = ts.pro_api('7b959deb4d92893a6bb5d638c3823e90c9b84c0d08761a516a7a96cb')
    data = pro.daily(ts_code='000002.SZ', start_date='20190701', end_date='20200701')
    data.to_csv('./data/sock.csv', index=None)

    # 列名选取行，剔除不需要开头的行
    # del data['ts_code', 'trade_date']

    # 反转数据，历史日期在前
    dataReverse = data.reindex(index=data.index[::-1])

    # 得到数据值
    X = dataReverse.loc[:, ['high', 'low', 'close', 'vol', 'amount']].values
    Y = dataReverse.loc[:, ['open']].values

    return X, Y


def get_lstm_xdataset(data, steps):
    """
    数据按照时间步长重组为3维矩阵
    """
    lstm_xdataset = []
    for i in range(steps, data.shape[0]):
        lstm_xdataset.append(data[i-steps:i])
    lstm_xdataset = np.array(lstm_xdataset)
    return lstm_xdataset


def get_lstm_ydataset(data, steps):
    """
    数据按照时间步长重组为3维矩阵
    """
    lstm_ydataset = []
    for i in range(steps, data.shape[0]):
        lstm_ydataset.append(data[i])
    lstm_ydataset = np.array(lstm_ydataset)
    return lstm_ydataset


if __name__ == '__main__':
    # 设置参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=5, help='时间步长')
    parser.add_argument('--features', type=int, default=5, help='输入变量数')
    parser.add_argument('--epoch', type=int, default=100)
    parser.add_argument('--batchsize', type=int, default=2)
    args = parser.parse_args()

    n_steps = args.steps
    n_features = args.features

    # 取得数据
    x_data, y_data = get_dataset()
    # 数据归一化
    mms = MinMaxScaler(feature_range=(0, 1))
    x_data = mms.fit_transform(x_data)
    y_data = mms.fit_transform(y_data)

    # 划分训练集和测试集
    x_train, y_train = x_data[0:int(x_data.shape[0] * 0.3)], y_data[0:int(y_data.shape[0] * 0.3)]
    x_test, y_test = x_data[int(x_data.shape[0] * 0.3)::], y_data[int(y_data.shape[0] * 0.3)::]

    # 重组数据为3维矩阵
    x_train, y_train = get_lstm_xdataset(x_train, n_steps), get_lstm_ydataset(y_train, n_steps)
    x_test, y_test = get_lstm_xdataset(x_test, n_steps), get_lstm_ydataset(y_test, n_steps)

    # 构建模型
    model = create_model(n_steps, n_features)
    model.fit(x=x_train, y=y_train, epochs=args.epoch, batch_size=args.batchsize)
    y_predictes = model.predict(x_test)

    # 反归一化数据
    y_test = mms.inverse_transform(y_test)
    y_predictes = mms.inverse_transform(y_predictes)

    plt.figure()
    plt.plot(y_test, label='row')
    plt.plot(y_predictes, label='pre')
    plt.legend()
    plt.show()

