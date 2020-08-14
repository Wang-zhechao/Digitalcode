from sklearn import datasets
from sklearn.decomposition import PCA, TruncatedSVD, LatentDirichletAllocation
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import geatpy

iris = datasets.load_iris()
y = iris.target
X = iris.data

'''
n_components =  'mle'             —— 自选最优超参数, 
                [0, 1]之间的浮点数 —— 选择信息保留比例（svd_solver='full'）
svd_solver = ['auto', 'full', 'arpack', 'randomized']
random_state = 整数  ——随机种子
'''
pca = PCA(n_components=2)
# —————————————————降维————————————————
# 方法一、pca.fit_transform()
X_dr = pca.fit_transform(X)
# # 方法二、fit() and transform()
# pca.fit(X)
# X_dr = pca.transform(X)

# —————————————————降维还原原数据空间——————————————
X_invers = pca.inverse_transform(X_dr)

# —————————————————输出中间数据———————————
# V = pca.components_  # 提取V（k , n），用于映射的新特征空间  X_dr = X * V.T
#
# print(X.shape)
# print(V.shape)
print(X_dr.shape)

print(pca.explained_variance_)  # 查看降维后每个新特征向量上所带信息量的大小（可解释性方差）
print(pca.explained_variance_ratio_)  # 查看降维后每个新特征向量上所带信息量占原始数据的百分比（可解释性方差贡献率）
print(pca.explained_variance_ratio_.sum())  # 信息保留百分比

# —————————————————数据可视化——————————
# plt.figure()
# plt.scatter(X_dr[y == 0, 0], X_dr[y == 0, 1], label=iris.target_names[0])
# plt.scatter(X_dr[y == 1, 0], X_dr[y == 1, 1], label=iris.target_names[1])
# plt.scatter(X_dr[y == 2, 0], X_dr[y == 2, 1], label=iris.target_names[2])
# plt.legend()
# plt.show()

# —————————————————使用KNN绘制参数分类曲线(交叉验证)——————————
score = []
for i in range(10):
    once = cross_val_score(KNN(i+1), X_dr, y, cv=5).mean()
    score.append(once)
plt.figure(figsize=[20, 5])
plt.plot(range(1, 11), score)
plt.show()
