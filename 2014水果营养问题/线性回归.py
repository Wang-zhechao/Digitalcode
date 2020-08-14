import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 载入波士顿房价数据
load_data = pd.read_excel('./data/Fruits.xlsx')
data_X = load_data['时间'].values.reshape(-1, 1)
data_y = load_data['苹果'].values.reshape(-1, 1)

data_pre = np.array([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)

# 实例化模型
model = LinearRegression()
# model = Lasso()
# model = Ridge()
# model = ElasticNet()

# 训练模型
model.fit(data_X, data_y)

# 输出预测与真值
# print(data_pre)
# print(model.predict(data_pre))
# print(load_data['苹果_pre'].values.reshape(-1, 1))
apple_pre = model.predict(data_pre)
apple_row = load_data['苹果_pre'].values.reshape(-1, 1)

plt.figure()
plt.subplot(211)
plt.title('LinearRegression')
plt.scatter(data_X, data_y, c='red')
plt.plot(data_X, model.predict(data_X))
plt.legend(['拟合曲线', '苹果数据'])

plt.subplot(212)
plt.title('后10年预测')
plt.plot(data_pre, apple_pre)
plt.plot(data_pre, apple_row)
plt.legend(['苹果预测数据', '苹果真实数据'])
plt.show()

# # 输出模型参数
# print(model.coef_)
# print(model.intercept_)
#
# # 输出模型定义参数
# print(model.get_params())
#
# # 模型评估
# print(model.score(data_X, data_y))  # R^2
