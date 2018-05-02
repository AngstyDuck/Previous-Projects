import numpy as np


x = np.array([[1,1],[0,1],[0,0]])

np.savetxt(r'/home/pi/dw1d/Datafiles/data.txt',x,fmt='%d')
b = np.loadtxt(r'/home/pi/dw1d/Datafiles/data.txt', dtype=int)
print(b)
print(x==b)








