from sklearn.decomposition import PCA
from sklearn import datasets
import matplotlib.pyplot as plt

# ————————————————PCA数据降维——————————————————————
# 载入数据
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 实例化模型
# pca = PCA(2)  # 按给定维度降维
pca = PCA(n_components=0.95 , svd_solver='full')  # 按信息保存率降维
x = pca.fit_transform(X)
print(x)
print(y)

# # 数据显示
# plt.figure()
# plt.scatter(X[y == 0, 0], x[y == 0, 1], c='r')
# plt.scatter(x[y == 1, 0], x[y == 1, 1], c='g')
# plt.scatter(x[y == 2, 0], x[y == 2, 1], c='b')
# plt.legend([iris.target_names[0], iris.target_names[1], iris.target_names[2]])
# plt.show()

# ————————————————SVD数据降维——————————————————————
from sklearn.decomposition import TruncatedSVD
svd = TruncatedSVD(2)
x = svd.fit_transform(X)

# plt.figure()
# plt.scatter(X[y == 0, 0], x[y == 0, 1], c='r')
# plt.scatter(x[y == 1, 0], x[y == 1, 1], c='g')
# plt.scatter(x[y == 2, 0], x[y == 2, 1], c='b')
# plt.legend([iris.target_names[0], iris.target_names[1], iris.target_names[2]])
# plt.show()
