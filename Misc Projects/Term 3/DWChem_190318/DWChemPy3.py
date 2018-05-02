from scipy.misc import derivative
import math
from sympy import *
import numpy as np
import scipy.constants as c

def spherical_to_cartesian(r,theta,phi):
    x = round(r*np.sin(theta)*np.cos(phi),5)
    y = round(r*np.sin(theta)*np.sin(phi),5)
    z = round(r*np.cos(phi),5)
    return (x,y,z)

def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2+y**2+z**2)
    theta = np.arccos(z/np.sqrt(x**2+y**2+z**2))
    phi = np.arctan2(y,x)
    return r,theta,phi

def absolute(cn):
    absol = np.sqrt((np.real(cn))**2 + (np.imag(cn))**2)
    return absol

def angular_wave_func(m,l,theta,phi):
    if l == 0:
        if m == 0:
            ans = np.sqrt(1/(4*c.pi))
    elif l == 1:
        if m == 0:
            ans = np.sqrt(3/(4*c.pi)) * np.cos(theta)
        elif m == 1:
            ans = -np.sqrt(3/(8*c.pi))*np.sin(theta)*np.exp(phi*1j)
        elif m == -1:
            ans = np.sqrt(3/(8*c.pi))*np.sin(theta)*np.exp(phi*-1j)
    elif l == 2:
        if m == 0: # l=2, m=0
            ans = np.sqrt(5/(16*c.pi))*(3*(np.cos(theta)**2)-1)
        elif m == 1: # l=2, m= +1
            ans = -np.sqrt(15/(8*c.pi))*np.cos(theta)*np.sin(theta)*np.exp(phi*1j)
        elif m == 2: # l=2, m= +2
            ans = np.sqrt(15/(32*c.pi))*(np.sin(theta)**2)*np.exp(phi*2j)
        elif m == -1: # l=2, m= -1
            ans = np.sqrt(15/(8*c.pi))*np.cos(theta)*np.sin(theta)*np.exp(phi*-1j)
        elif m == -2: # l=2, m= -2
            ans = np.sqrt(15/(32*c.pi))*(np.sin(theta)**2)*np.exp(phi*-2j)
    return ans

def radial_wave_func(n,l,r):
    #print('---------------------------------------')
    #print('a: {0}'.format(a))
    #print('r: {0}'.format(r))
    if n == 1: # If n = 1
        if l == 0:
            R = ((2/np.sqrt(a**3)) * np.exp(-r/a) / a(-3/2))
    elif n == 2:
        if l == 0:
            R = (1/np.sqrt(2)) * (a**(-3/2)) * (1-(r/(2*a))) * (np.exp(-r/(2*a))) / (a**(-3/2))
        elif l == 1:
            R = ((1/np.sqrt(24)) * (a**(-3/2)) * (r/a) * np.exp(-r/(2*a)) / a**(-3/2))
    elif n == 3:
        if l == 0:
            R = (2/81*np.sqrt(2)) * (a**(-3/2)) * ((27-18)*(r/a)+2*(r/a)*2) * (np.exp(-r/(3*a))) / (a**(-3/2))
            ############################################################^here###
        elif l == 1:
            R = (8/(27*np.sqrt(6))) * (a**(-3/2)) * (((1-(r/(6*a)))*(r/a))) * (np.exp(-r/(3*a))) / (a**(-3/2))
        elif l == 2:
            R = (4/(81*np.sqrt(30))) * (a**(-3/2)) * (r/a)*2 * (np.exp(-r/(3*a))) / (a**(-3/2))
            ##############################################^here####
    return R


def linspace(start, stop, num=50):
    step = (stop - start)/(num-1)
    space = []
    if not num:
        step = (stop - start)/(49)
        for i in range(num ):
            space.append(start + step * i)
    for i in range(num ):
        space.append(round(start + step * i, 5))
    return space



def meshgrid(x,y,z):
    row1 = []
    for h in range(len(y)):
        second_list = []
        for i in range(len(x)):
            inner_list = []
            for j in range(len(z)):
                inner_list.append(float(x[i]))
            second_list.append(inner_list)
        row1.append(second_list)
    row2 = []
    for i in range(len(y)):
        inner_list = []
        second_list = []
        for j in range(len(z)):
            inner_list.append(float(y[i]))
        for k in range(len(x)):
            second_list.append(inner_list)
        row2.append(second_list)
    row3 = []
    for h in range(len(y)):
        second_list = []
        for i in range(len(x)):
            inner_list = []
            for j in range(len(z)):
                inner_list.append(float(z[j]))
            second_list.append(inner_list)
        row3.append(second_list)
    return (row1,row2,row3)


vspherical = np.vectorize(cartesian_to_spherical)
vangular = np.vectorize(angular_wave_func)
vradial = np.vectorize(radial_wave_func)
vabs = np.vectorize(absolute)
vround=np.vectorize(round)
a=c.physical_constants['Bohr radius'][0]
def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    xx, yy, zz = np.mgrid[-roa:roa:(Nx*1j),-roa:roa:(Ny*1j),-roa:roa:(Nz*1j)]

    r, theta, phi = vspherical(xx, yy, zz)

    if m == 0:
        angular = vangular(m,l,theta,phi)

    elif m > 0:
        angular = (1/np.sqrt(2))*(vangular(-m,l,theta,phi)+(-1)**m*vangular(m,l,theta,phi))

    elif m < 0:
        angular = (1j/np.sqrt(2))*(vangular(m,l,theta,phi)-(-1)**m*vangular(-m,l,theta,phi))

    radial = vradial(n,l,r*a)
    mag = vabs(radial * angular)**2
    return np.round((xx,yy,zz,mag),5)




#-----------------------------------------CHANGE THIS ONLY--------------------------
x,y,z,mag=hydrogen_wave_func(3,2,2,13,20,20,20)
#-----------------------------------------------------------------------------------




x.dump('xdata.dat')
y.dump('ydata.dat')
z.dump('zdata.dat')
mag.dump('density.dat')


import matplotlib.pyplot as plt
import importlib
importlib.import_module('mpl_toolkits.mplot3d').Axes3D

x = np.load('xdata.dat')
y = np.load('ydata.dat')
z = np.load('zdata.dat')

mag = np.load('density.dat')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for a in range(0,len(mag)):
    for b in range(0,len(mag)):
        for c in range(0,len(mag)):
            ax.scatter(x[a][b][c],y[a][b][c],z[a][b][c], marker='o', alpha=(mag[a][b][c]/np.amax(mag)))

plt.show()



































