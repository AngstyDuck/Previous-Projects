import os


os.environ['QT_API'] = 'pyqt'
os.environ['ETS_TOOLKIT'] = 'qt4'


import numpy as np
from mayavi import mlab

x = np.load('xdata.dat')
y = np.load('ydata.dat')
z = np.load('zdata.dat')

density = np.load('density.dat')

figure = mlab.figure('DensityPlot')

pts = mlab.contour3d(density, contours=20, opacity=0.5)
mlab.axes()
mlab.show()




































