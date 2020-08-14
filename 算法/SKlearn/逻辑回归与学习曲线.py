from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt

# 数据加载
breast = datasets.load_breast_cancer()
X = breast.data
y = breast.target

# 模型构建
lrl1 = LogisticRegression(penalty='l1', solver='liblinear', C=1, max_iter=1000)
lrl2 = LogisticRegression(penalty='l2', solver='liblinear', C=1, max_iter=1000)

# 计算学习曲线
train_size, train_acc, test_acc = learning_curve(lrl1, X, y, cv=5)

plt.figure()
plt.plot(train_size, train_acc.mean(axis=1))
plt.plot(train_size, test_acc.mean(axis=1))
plt.legend(['train_acc', 'test_acc'])
plt.show()
