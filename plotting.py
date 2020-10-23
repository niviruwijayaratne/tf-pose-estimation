from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import random
import pyqtgraph.exporters
from tfpose.src.estimator import TfPoseEstimator
from tfpose.src.run import get_points

# class Plotter()
matrix = get_points('./tfpose/images/hand.jpg', True)
points = matrix.T 
def normalize(matrix):
    max_val = np.max(matrix)
    min_val = np.min(matrix)
    matrix = ((2*(matrix - min_val))/(max_val - min_val)) - 1
    return matrix

def webglify(normalized_matrix):
    arr = []
    for row in normalized_matrix:
        row = np.squeeze(row)
        for elem in row:
            arr.append(elem)
    return arr

points = normalize(points)
print(webglify(points))

_CONNECTION = [
        [0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [0, 7], [7, 8],
        [8, 9], [9, 10], [8, 11], [11, 12], [12, 13], [8, 14], [14, 15],
        [15, 16]]

app = QtGui.QApplication([])
graph = gl.GLViewWidget()
graph.setBackgroundColor(0, 0, 0, 0.8)
graph.show()
graph.setWindowTitle('pyqtgraph example: GLSurfacePlot')
graph.setCameraPosition(distance=2)

## Add a grid to the view
spacing_vector = QtGui.QVector3D(100, 100, 100)
x = gl.GLGridItem(size=QtGui.QVector3D(1000, 1000, 1), color=(0, 0, 0, 255))
x.setSpacing(spacing=spacing_vector)
x.rotate(90, 1, 0, 0)
x.scale(2.0, 2.0, 1.0)  # draw grid after surfaces since they may be translucent
x.translate(1000, 0,1000)
graph.addItem(x)

y = gl.GLGridItem(size=QtGui.QVector3D(1000, 1000, 1), color=(0, 0, 0, 255))
y.setSpacing(spacing=spacing_vector)
y.rotate(90, 0, 1,0)
y.scale(2.0, 2.0, 1.0)
y.translate(0, 1000, 1000)
graph.addItem(y)

z = gl.GLGridItem(size=QtGui.QVector3D(1000, 1000, 1), color=(0, 0, 0, 255))
z.setSpacing(spacing=spacing_vector)
z.scale(2.0, 2.0, 1.0)
z.translate(1000, 1000, 0)
graph.addItem(z)
a = gl.GLAxisItem(size=QtGui.QVector3D(50, 50,50))
graph.addItem(a)


_CONNECTION = [
        [0, 1], [1, 2], [2, 3], [0, 4], [4, 5], [5, 6], [0, 7], [7, 8],
        [8, 9], [9, 10], [8, 11], [11, 12], [12, 13], [8, 14], [14, 15],
        [15, 16]]

for pair in _CONNECTION:
    ind1 = pair[0]
    ind2 = pair[1]
    print(ind1, ind2)
    p1 = points[ind1].T
    p2 = points[ind2].T
    connection = np.array([np.vstack((p1, p2))])
    line = gl.GLLinePlotItem(pos=connection, color = pg.glColor((0, 255, 0)), width = 5.0, mode = 'lines')
    graph.addItem(line)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

