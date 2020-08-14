from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2, random_state=22,
                           n_clusters_per_class=1, scale=100)

# X = preprocessing.minmax_scale(X, feature_range=(-1, 1))  # 归一化范围到（-1,1）
X = preprocessing.scale(X)  # 归一化范围到（-1,1）

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 实例化模型
clf = SVC()

# 训练模型
clf.fit(X_train, y_train)

# 模型评价
print(clf.score(X_test, y_test))
