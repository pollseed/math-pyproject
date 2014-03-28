__author__ = 'shn'

import numpy as np

arr = np.random.randn(5, 4)
arr.mean()
arr.mean(axis=1)
np.mean(arr)
arr.sum()
arr.sum(0)

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
arr.cumsum(0)
arr.sumprod(1)