from sklearn import svm
from sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)

# 保存模型1:pickle
# # 保存
# import pickle
# with open('save/clf.pickel', 'wb') as f:
#     pickle.dump(clf, f)
# # 读取
# with open('save/clf.pickel', 'rb') as f:
#     clf = pickle.load(f)

# 模型保存2: joblib
# # 保存
# from sklearn.externals import joblib
# joblib.dump(clf, 'save/clf.pkl')
# # 读取
# clf = joblib.load('save/clf.pkl')
