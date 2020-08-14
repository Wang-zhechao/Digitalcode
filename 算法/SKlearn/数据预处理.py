from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = datasets.load_iris(return_X_y=True)

# ————————————————数据预处理——————————————————————
# 标准化
X = preprocessing.StandardScaler().fit_transform(X)

# 归一化（默认归一化到0~1）
X = preprocessing.MinMaxScaler.fit_transform(X)

# 处理异常值
X = preprocessing.RobustScaler.fit_transform(X)

# 稀疏矩阵处理：除最大值后缩放到-1~1
X = preprocessing.maxabs_scale(X)


# ————————————————数据缺失处理——————————————————————
from sklearn.impute import SimpleImputer
'''
sklearn:
SimpleImputer(missing_values=np.nan, strategy="mean", fill_value=None, verbose=0, copy=True, add_indicator=False)
strategy = 'mean'  'median'  'most_frequent'  'constant'

pandas:
data.loc[:,'AGE'] = data.loc[:,'AGE'].fillna(data.loc[:,'AGE'].median())  # 填补
data.dropna(axis=0)  # 删除行
data.dropna(axis=1)  # 删除列
'''

