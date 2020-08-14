import sklearn
from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

print(sklearn.metrics.SCORERS.keys())

# 载入莺尾花数据
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

k_range = range(1, 31)
k_scores = []
k_loss = []
for k in k_range:
    # 实例化模型
    knn = KNeighborsClassifier(n_neighbors=k)

    # 模型训练(数据集经过多次划分（cv = 5）)
    scores = cross_val_score(knn, iris_X, iris_y, cv=5, scoring='accuracy')
    loss = -cross_val_score(knn, iris_X, iris_y, cv=5, scoring='neg_mean_squared_error')
    k_scores.append(scores.mean())
    k_loss.append(loss.mean())

plt.figure()
plt.plot(k_range, k_scores)
plt.show()

plt.figure()
plt.plot(k_range, k_loss)
plt.show()
