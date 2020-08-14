import sklearn
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_digits
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# print(sklearn.metrics.SCORERS.keys())

# 载入数据集
digits = load_digits()
X = digits.data
y = digits.target

# 需要改变的参数
param_range = np.logspace(-6, -2.3, 5)

# 交叉验证
train_loss, test_loss = validation_curve(SVC(), X, y, param_name='gamma', param_range=param_range,
                                         cv=10, scoring='neg_mean_squared_error')

# 打印损失
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

plt.figure()
plt.plot(param_range, train_loss_mean, 'o-', c='r')
plt.plot(param_range, test_loss_mean, 'o-', c='g')
plt.legend(['Training', 'Val'])
plt.xlabel('gamma')
plt.ylabel('Loss')
plt.show()
