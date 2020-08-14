import numpy as np
import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()

iris_pd = pd.DataFrame()

for i in range(4):
    iris_pd[i] = iris.data[:, i]
iris_pd.to_excel('./data/irais.xlsx')
