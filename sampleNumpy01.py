import numpy as np
import matplotlib.pyplot as plt

# 等間隔の1000点のデータ定義
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs**2 + ys**2)

# ２次元配列の値を表現する
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $¥sqrt{x^2 + y^2}$ for a grid of values")