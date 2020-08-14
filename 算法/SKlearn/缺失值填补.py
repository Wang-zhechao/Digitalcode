import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import KNNImputer, SimpleImputer, IterativeImputer, MissingIndicator
from sklearn.ensemble import RandomForestRegressor

print("Sklearn verion is {}".format(sklearn.__version__))

# ---------------------------数据读取
file_path = open('/数模/2020河北省赛题/data/data 1.csv')
df = pd.read_csv(file_path)
del df['starttime']
print(df.head())

# ---------------------------标记缺失值
indicator = MissingIndicator(missing_values=np.nan)
mask_missing_values_only = indicator.fit_transform(df)
print('mask_missing_values is:')
print(mask_missing_values_only)

# ---KNN填补缺失值
KI = KNNImputer(n_neighbors=10, missing_values=np.nan)

df_knn = KI.fit_transform(df)
print('KNNImputer is:')
print(df_knn)

# ---单变量插补
'''
"mean" ---平均值
"median" ---中位数
"most_frequent" ---众数
"constant" ---常数
'''
SI = SimpleImputer(missing_values=np.nan, strategy="mean")

df_si = SI.fit_transform(df)
print('SimpleImputer is:')
print(df_si)

# ---多变量插补
II = IterativeImputer(max_iter=10, random_state=0)

df_ii = II.fit_transform(df)
print('IterativeImputer is:')
print(df_ii)

# # ---随机森林插补(有监督填补，标签不能为空，填补为特征中的缺失值)
# # 构建新特征矩阵
# df = X_missing_reg
# fillc = df.iloc[:, i]
# df = pd.concat([df.iloc[:, df.columns != 6], pd.DataFrame(y_full)], axis=1)
#
# # 在新特征矩阵中，对含有缺失值的列用0填补
# df_0 = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0).fit_transform(df)
#
# # 找出训练集和测试集
# Ytrain = fillc[fillc.notnull()]
# Ytest = fillc[fillc.isnull()]
# Xtrain = df_0[Ytrain.index, :]
# Xtest = df_0[Ytest.index, :]
#
# # 回归森林填补缺失值
# rfc = RandomForestRegressor(n_estimators=100)
# rfc.fit(Ytrain, Xtrain)
# Ypredict = rfc.predict(Xtest)
#
# # 将填补好的特征放入原始特征矩阵中
# X_missing_reg.loc[X_missing_reg.iloc[:, i].isnull(), i] = Ypredict

# ---数据可视化
col = np.where(mask_missing_values_only[:, 0] == True, 'r', 'g')  # 填补值为绿色

plt.figure()
plt.subplot(311)
plt.scatter(range(len(df_knn[:, 0])), df_knn[:, 0], c=col, s=0.1)
plt.subplot(312)
plt.scatter(range(len(df_si[:, 0])), df_si[:, 0], c=col, s=0.1)
plt.subplot(313)
plt.scatter(range(len(df_ii[:, 0])), df_ii[:, 0], c=col, s=0.1)
plt.show()
