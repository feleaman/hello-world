import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_ubyte
import skimage.filters

n = 100
x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n)

z = np.zeros((n, n))
for i in range(n):
	for j in range(n):
		z[i][j] = x[i]*y[j] + np.random.random_sample()/10
		if j > 48 and j < 52:
			z[i][j] = z[i][j]*2

z = z / np.max(z)
plt.pcolormesh(x, y, z, cmap='gray')
plt.colorbar()
# print(skimage.filters.threshold_otsu(z))
plt.show()


# z = img_as_ubyte(z)
# z = skimage.filters.median(image=z, selem=np.ones((3, 3)))
# plt.pcolormesh(x, y, z, cmap='gray')
# plt.colorbar()
# plt.show()

thr = skimage.filters.threshold_otsu(z)


selem = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
z2 = skimage.filters.rank.otsu(image=z, selem=selem)
plt.pcolormesh(x, y, z2, cmap='gray')
plt.colorbar()
plt.show()

z3 = np.zeros((n, n))
for i in range(n):
	for j in range(n):
			if z[i][j] >= thr:
				z3[i][j] = 1
			else:
				z3[i][j] = 0

plt.pcolormesh(x, y, z3, cmap='gray')
plt.colorbar()
plt.show()

print(z3[50])