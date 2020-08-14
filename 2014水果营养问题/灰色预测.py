# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def GM11(x, n):
    '''
    灰色预测
    x：序列，numpy对象
    n:需要往后预测的个数
    '''
    x1 = x.cumsum()  # 一次累加
    z1 = (x1[:len(x1) - 1] + x1[1:]) / 2.0  # 紧邻均值
    z1 = z1.reshape((len(z1), 1))
    B = np.append(-z1, np.ones_like(z1), axis=1)
    Y = x[1:].reshape((len(x) - 1, 1))
    # a为发展系数 b为灰色作用量
    [[a], [b]] = np.dot(np.dot(np.linalg.inv(np.dot(B.T, B)), B.T), Y)  # 计算参数
    result = (x[0] - b / a) * np.exp(-a * (n - 1)) - (x[0] - b / a) * np.exp(-a * (n - 2))
    S1_2 = x.var()  # 原序列方差
    e = list()  # 残差序列
    for index in range(1, x.shape[0] + 1):
        predict = (x[0] - b / a) * np.exp(-a * (index - 1)) - (x[0] - b / a) * np.exp(-a * (index - 2))
        e.append(x[index - 1] - predict)
    S2_2 = np.array(e).var()  # 残差方差
    C = S2_2 / S1_2  # 后验差比
    if C <= 0.35:
        assess = '后验差比<=0.35，模型精度等级为好'
    elif C <= 0.5:
        assess = '后验差比<=0.5，模型精度等级为合格'
    elif C <= 0.65:
        assess = '后验差比<=0.65，模型精度等级为勉强'
    else:
        assess = '后验差比>0.65，模型精度等级为不合格'
    # 预测数据
    row = list()
    predict = list()
    # 原始数据拟合
    for index in range(1, x.shape[0]+1):
        row.append((x[0] - b / a) * np.exp(-a * (index - 1)) - (x[0] - b / a) * np.exp(-a * (index - 2)))
    row = np.array(row)

    # 数值预测
    for index in range(x.shape[0] + 1, x.shape[0] + n + 1):
        predict.append((x[0] - b / a) * np.exp(-a * (index - 1)) - (x[0] - b / a) * np.exp(-a * (index - 2)))
    predict = np.array(predict)
    return {
        'a': {'value': a, 'desc': '发展系数'},
        'b': {'value': b, 'desc': '灰色作用量'},
        'row': {'value': row, 'desc': '前%d个拟合值' % x.shape[0]},
        'C': {'value': C, 'desc': assess},
        'predict': {'value': predict, 'desc': '往后预测%d个的序列' %(n)},
    }


if __name__ == "__main__":
    load_data = pd.read_excel('./data/Fruits.xlsx')
    data_X = load_data['时间'].values
    data_y = load_data['苹果'].values
    data_time = load_data['时间_pre'].values
    data_row = load_data['苹果_pre'].values
    x = data_y  # 输入数据
    y = data_row  # 需要预测的数据
    result = GM11(x, 10)
    # 拟合输出
    row = result['row']['value']
    row = np.round(row, 1)
    # 预测输出
    predict = result['predict']['value']
    predict = np.round(predict, 1)
    # print('真实值:', y)
    # print('预测值:', predict)
    print(result['C'])

    plt.figure()
    plt.scatter(data_X, data_y, marker='x')
    plt.scatter(data_time, data_row, marker='^')
    plt.plot(range(2001, 2011), row, c='g')
    plt.plot(range(2011, 2021), predict, c='r')
    # plt.legend(['原始数据', '真实数据', '拟合数据', '预测数据'])
    plt.legend(['拟合数据', '预测数据', '原始数据'])
    plt.xticks(range(2001, 2021, 2))
    plt.show()