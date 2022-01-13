from matplotlib import scale
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#%matplotlib inline

plt.rcParams['figure.figsize'] = (6, 8)
plt.rcParams['figure.dpi'] = 150

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([6, 0])
ax.set_ylim([0, 6])
ax.set_zlim([0, 8])

begin = (0, 1, 0)
eind = (0, 2, 0)

ax.scatter(0, 1, 0)
ax.scatter(0, 2, 0)
# plt.quiver(begin[0], begin[1], begin[2], eind[0], eind [1], eind[2], scale=1)
ax.quiver(begin[0], begin[1], begin[2], eind[0], eind [1], eind[2], length=0.45)


plt.savefig('representation.png')

