from sklearn import datasets
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet

# 载入波士顿房价数据
load_data = datasets.load_boston()
data_X = load_data.data
data_y = load_data.target

# 实例化模型
model = LinearRegression()

# 训练模型
model.fit(data_X, data_y)

# 输出预测与真值
print(model.predict(data_X[:4, :]))
print(data_y[:4])

# 输出模型参数
print(model.coef_)
print(model.intercept_)

# 输出模型定义参数
print(model.get_params())

# 模型评估
print(model.score(data_X, data_y))  # R^2
