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


a = np.array([[0, 0], [0, 1], [1, 1], [3, 0]])
lof = LOF.LOF(data.values, k=3, dist_mode=2, top=5)
lof.scan()
print(lof.OUTLIERS_SET)



