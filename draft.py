# -*- coding: utf-8 -*-
"""
@Time    : 2017/11/26 上午11:47
@Author  : VincentGum
@File    : draft.py
"""
import pandas as pd
import numpy as np
import LOF

data = pd.read_csv('data/Q2Q3_input.csv')
data.pop('user_id')
data = data.values

a = np.array([[0, 0], [0, 1], [1, 1], [3, 0]])
lof_ = LOF.LOF(data, k=2, dist_mode=1, top=5)
lof = LOF.LOF(data, k=3, dist_mode=2, top=5)

lof_.scan()
lof.scan()
print('Given k = 2, using Manhattan distance')
print(lof_.OUTLIERS_SET)
print('\n')
print('Given k = 3, using Euclidean distance')
print(lof.OUTLIERS_SET)