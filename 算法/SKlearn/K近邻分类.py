import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 载入莺尾花数据
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

# 划分测试数据和验证数据集
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)

# 实例化模型
knn = KNeighborsClassifier()

# 模型训练
knn.fit(X_train, y_train)

# 打印结果
print(knn.predict(X_test))
print(y_test)

acc = knn.score(X_test, y_test)
print(acc)