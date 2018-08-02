import numpy as np

# #This code saves numpy arrays as txt files
# x = np.array([[1,1],[0,1],[0,0]])
# np.savetxt(r'/home/pi/dw1d/Datafiles/data.txt',x,fmt='%d')




b = np.loadtxt(r'C:\Users\User\Desktop\Work\Digital World\1D_final\rpi_files_2.0/data_black_edges.txt', dtype=int)
print(b[:100,20:50].shape)









