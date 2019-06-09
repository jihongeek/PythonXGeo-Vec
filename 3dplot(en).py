from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# vertices of cube
v = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[1,1,1],[0,1,1]])
v1 =np.array([[0,1,1],[2,1,1],[2,3,1],[0,3,1],[0,1,3],[2,1,3],[2,3,3],[0,3,3]])
v3 = np.array([[0,0,0],[2,0,0],[2,2,0],[0,2,0]])
def cube(v,alpha):
    verts = [[v[0], v[1], v[2], v[3]], [v[0], v[3], v[7], v[4]],
             [v[0], v[1], v[5], v[4]], [v[6], v[2], v[3], v[7]], [v[6], v[2], v[1], v[5]], [v[6], v[5], v[4], v[7]]]
    face = Poly3DCollection(verts, linewidths=1, edgecolors='r', alpha=alpha)
    face.set_facecolor([0.2, 0.8, 0.3])
    return ax.add_collection3d(face)
def plane(v,color,alpha):
    verts = [[v[0], v[1], v[2], v[3]]]
    return ax.add_collection3d(Poly3DCollection(verts,
                                                facecolors=color, linewidths=1, edgecolors='r', alpha=alpha))
cube(v,0.3)
cube(v1,0.3)
plane(v3,'green',0)
plt.show()