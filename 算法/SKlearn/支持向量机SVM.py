from sklearn.svm import LinearSVC, SVC
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn import datasets

# # ————————————svc二分类(线性)——————————————
# X, y = datasets.make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.6)
# plt.figure()
# plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='rainbow')
# plt.show()
#
# # 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed' or a callable.
# svc = SVC(kernel='linear')
# print(cross_val_score(svc, X, y, cv=5, scoring='accuracy').mean())

# ————————————svc二分类(非线性)——————————————
X, y = datasets.make_circles(n_samples=1000, noise=0.03, factor=0.6)
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, s=10, cmap='rainbow')
plt.show()

# 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed' or a callable.
svc = SVC(kernel='rbf')
print(cross_val_score(svc, X, y, cv=5, scoring='accuracy').mean())
