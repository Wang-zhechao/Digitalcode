from sklearn.covariance import EllipticEnvelope
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn import svm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 数据读取
file_path = open('/数模/2020河北省赛题/data/data 1.csv')
df = pd.read_csv(file_path)
del df['starttime']
# print(df.head())
speed = df['speed'].dropna().values.reshape(-1, 1)

# --------------------异常值筛选---------------------------
# ------孤立森林/隔离森林法
# https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html?highlight=isolationforest#sklearn.ensemble.IsolationForest
IF = IsolationForest(n_estimators=50, random_state=0)

IF.fit(speed)
speed_if = IF.predict(speed)  # 检测结果：-1 异常；1 正常
# print(speed_pre)
# print(IF.score_samples(speed))  # 计算异常分数，越低越异常

# ------局部离群因子法
# https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html?highlight=localoutlierfactor#sklearn.neighbors.LocalOutlierFactor
'''
当使用 LOF 进行离群点检测的时候，不能使用 predict, decisionfunction 和 score_samples 方法， 只能使用 fit_predict 方法。训练
样本的异常性得分可以通过 negative_outlier_factor 属性来获得。 

注意当使用LOF算法进行新奇点检测的时候(novelty 设为 True)， predict, decision_function 和 score_samples 函数可被用于新的未见
过数据。

novelty  --False :用于异常值检测
         --True :用于新奇点检测
'''
LOF = LocalOutlierFactor(n_neighbors=5)

speed_lof = LOF.fit_predict(speed)  # 检测结果：-1 异常；1 正常
# print(speed_lof)
# print(LOF.negative_outlier_factor_)  # 越接近-1代表越正常

# -----椭圆模型拟合
# https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope
EE = EllipticEnvelope(contamination=0.25)
speed_ee = EE.fit_predict(speed)
# print(speed_ee)
# print(EE.score_samples(speed))  # 计算负马氏距离

# -----单类svm算法(但是训练中不能包含异常值)
# https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html?highlight=oneclasssvm#sklearn.svm.OneClassSVM
OCS = svm.OneClassSVM(nu=0.3, kernel="rbf", gamma=0.1)
OCS.fit(speed)
speed_ocs = OCS.predict(speed)
# print(speed_ocs)
# print(OCS.score_samples(speed))

# -----数据可视化
col_if = np.where(speed_if == -1, 'r', 'g')  # 填补值为绿色
col_lof = np.where(speed_lof == -1, 'r', 'g')  # 填补值为绿色
col_ee = np.where(speed_ee == -1, 'r', 'g')  # 填补值为绿色
col_ocs = np.where(speed_ocs == -1, 'r', 'g')  # 填补值为绿色

plt.figure()
plt.subplot(411)
plt.scatter(range(len(speed)), speed, c=col_if, s=0.2)
plt.subplot(412)
plt.scatter(range(len(speed)), speed, c=col_lof, s=0.2)
plt.subplot(413)
plt.scatter(range(len(speed)), speed, c=col_ee, s=0.2)
plt.subplot(414)
plt.scatter(range(len(speed)), speed, c=col_ocs, s=0.2)
plt.show()
