from sklearn import datasets
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.model_selection import cross_val_score

# 载入波士顿房价数据
load_data = datasets.fetch_california_housing()
data_X = load_data.data
data_y = load_data.target

print(data_y.min(), data_y.max())
# ————————————LinearRegression——————————————
# 实例化模型
lr = LinearRegression()
lr.fit(data_X, data_y)
# 训练模型(交叉验证)
loss_lr = -cross_val_score(lr, data_X, data_y, cv=5, scoring='neg_mean_squared_error').mean()

print(loss_lr)
# print(lr.coef_)
# print(lr.intercept_)

# ————————————lasso——————————————
# 实例化模型
lasso = Lasso(alpha=0.01)

# 训练模型(交叉验证)
loss_lasso = -cross_val_score(lr, data_X, data_y, cv=5, scoring='neg_mean_squared_error').mean()

print(loss_lasso)

# ————————————lasso——————————————
# 实例化模型
ridge = Ridge(alpha=0.01)

# 训练模型(交叉验证)
loss_ridge = -cross_val_score(ridge, data_X, data_y, cv=5, scoring='neg_mean_squared_error').mean()

print(loss_ridge)

# ————————————lasso——————————————
# 实例化模型
elasticnet = ElasticNet(alpha=0.01)

# 训练模型(交叉验证)
loss_elasticnet = -cross_val_score(elasticnet, data_X, data_y, cv=5, scoring='neg_mean_squared_error').mean()

print(loss_elasticnet)
