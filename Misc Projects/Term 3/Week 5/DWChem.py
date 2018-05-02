#ALL IMPORTS
from math import *
import numpy as np
import copy



#Week 2
#DEGREE RADIAN
def deg_to_rad(deg):
    x = (deg / 360) * pi * 2
    x = round(x, 5)
    return x

def rad_to_deg(rad):
    x = (rad / (2 * pi)) * 360
    x = round(x, 5)
    return x



#SPHERICAL CARTESIAN
def spherical_to_cartesian(r, theta, phi):
    x = round(r * np.sin(theta) * np.cos(phi), 5)
    y = round(r * np.sin(theta) * np.sin(theta), 5)
    z = round(r * np.cos(theta), 5)
    return (x, y, z)

def cartesian_to_spherical(x, y, z):
    smol = 10 ** (-50)
    if (x == 0):
        x = smol
    if (y == 0):
        y = smol
    if (z == 0):
        z = smol
    phi = np.arctan(y / x)
    theta = np.arctan(y / (z * np.sin(phi)))
    r = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    phi = round(phi, 5)
    theta = round(theta, 5)
    r = round(r, 5)
    return (r, theta, phi)



#ABSOLUTE
def absolute(cnumber):
    x = cnumber.real
    y = cnumber.imag
    absolute = (x ** 2 + y ** 2) ** 0.5
    return absolute




#Week 3
#ANGULAR SOLUTION
import math
# y= a * b * c * d
# global constants
pi = math.pi
# constants for a
aDict = {
    "a00": np.sqrt(1 / (4 * pi)),
    "a01": np.sqrt(3 / (4 * pi)),
    "a02": np.sqrt(5 / (16 * pi)),
    "a03": np.sqrt(7 / (16 * pi)),
    "a11": np.sqrt(3 / (8 * pi)),
    "a12": np.sqrt(15 / (8 * pi)),
    "a13": np.sqrt(21 / (64 * pi)),
    "a22": np.sqrt(15 / (32 * pi)),
    "a23": np.sqrt(105 / (32 * pi)),
    "a33": np.sqrt(35 / (64 * pi))
}

def a(x1, x2):  # x1 - dictionary input   x2 - m
    x2 = int(x2)

    if (x2 == 1) or (x2 == 3):
        neg = -1
    else:
        neg = 1

    output = neg * aDict[x1]
    return output

# constants for b
def b(x1, x2):  # x1 - ml(str)     x2 - theta(int)
    x2 = float(x2)
    if x1 == "00":
        b00 = float(1)
        return b00
    elif x1 == "01":
        b01 = float(np.cos(x2))
        return b01
    elif x1 == "02":
        b02 = float((3 * (np.cos(x2) ** 2)) - 1)
        return b02
    elif x1 == "03":
        b03 = float((5 * (np.cos(x2) ** 3)) - (3 * np.cos(x2)))
        return b03
    elif x1 == "11":
        b11 = float(1)
        return b11
    elif x1 == "12":
        b12 = float(np.cos(x2))
        return b12
    elif x1 == "13":
        b13 = float((5 * (np.cos(x2)) ** 2) - 1)
        return b13
    elif x1 == "22":
        b22 = float(1)
        return b22
    elif x1 == "23":
        b23 = float(np.cos(x2))
        return b23
    elif x1 == "33":
        b33 = float(1)
        return b33
    else:
        print("variable b error")
        return

def c(x1, x2):  # x1 - m(str)  x2 - theta(int)
    x1 = abs(int(x1))
    output = float((np.sin(x2)) ** x1)
    return output

def d(x1, x2):  # x1 - m(str)     x2 - phi(int)
    x1 = int(x1)
    x = x2 * x1
    output = np.cos(x) + (1j) * round(np.sin(x), 5)
    return output

def angular_wave_func(m, l, theta, phi):
    m = str(m)
    l = str(l)
    ml = m + l
    Ax = "a" + ml
    A = round(a(Ax, m), 5)
    B = round(b(ml, theta), 5)
    C = round(c(m, theta), 5)
    D = round(d(m, phi), 5)

    Y = round(A * B * C * D, 5)
    return Y



#RADIAL SOLUTION
# global constants
import scipy.constants as c
b = c.physical_constants['Bohr radius'][0]  # Bohr's radius
# normalised means just the term a^(-3/2) is 1
a = {
    "10": 2,
    "20": np.sqrt(1 / 2),
    "21": np.sqrt(1 / 24),
    "30": np.sqrt(4 / 19683),
    "31": np.sqrt(64 / 4374),
    "32": np.sqrt(16 / 196830),
    "40": np.sqrt(1 / 16),
    "41": np.sqrt(5 / 768),
    "42": np.sqrt(1 / 20480),
    "43": np.sqrt(1 / 20643840)
}

def bohr(x1, x2):  # x1 - name     x2 - r(float)
    if (x1 == "10"):
        output = 1
        return output
    elif (x1 == "20"):
        output = 1 - (x2 / (2 * b))
        return output
    elif (x1 == "21"):
        output = x2 / b
        return output
    elif (x1 == "30"):
        output = 27 - (18 * (x2 / b)) + (2 * ((x2 / b) ** 2))
        return output
    elif (x1 == "31"):
        output = (1 - (x2 / (6 * b))) * (x2 / b)
        return output
    elif (x1 == "32"):
        output = (x2 / b) ** 2
        return output
    elif (x1 == "40"):
        output = 1 - ((3 / 4) * (x2 / b)) + ((1 / 8) * ((x2 / b) ** 2)) - ((1 / 192) * ((x2 / b) ** 3))
        return output
    elif (x1 == "41"):
        output = (x2 / b) * (1 - ((1 / 4) * (x2 / b)) + ((1 / 80) * ((x2 / b) ** 2)))
        return output
    elif (x1 == "42"):
        output = ((x2 / b) ** 2) * (1 - (1 / 12) * (x2 / b))
        return output
    elif (x1 == "43"):
        output = (x2 / b) ** 3
        return output
    else:
        print("value B error")
        return

def c(x1, x2):  # x1 - name      x2 - r(float)
    x1 = int(x1[0])
    output = np.exp((-1) * (x2 / (x1 * b)))
    return output

def radial_wave_func(n, l, r):
    # a=c.physical_constants['Bohr radius'][0]
    n = str(n)
    l = str(l)
    nl = n + l
    A = a[nl]
    B = bohr(nl, r)
    C = c(nl, r)
    output = round(A * B * C, 5)
    return output




#Week 4
#LINSPACE
def linspace(start, stop, *args, **kwargs):
    if (kwargs == {}) and (args == ()):
        times = 50
    elif (args == ()):
        times = kwargs['num']
    elif (kwargs == {}):
        times = args[0]
    interval = (stop - start) / (times - 1)
    iteratingNum = start - interval
    outputList = []
    for i in range(times):
        iteratingNum = iteratingNum + interval
        outputList.append(round(iteratingNum, 5))
    return outputList



#MESHGRID
def meshgrid(x, y, z):
    inputX = []
    inputY = []
    inputZ = []
    lenx = len(x)
    leny = len(y)
    lenz = len(z)

    def function1(element, elementNum):  # repeats a list in a bigger list
        outputList = []
        for i in range(elementNum):
            outputList.append(element)
        return outputList

    def function2(inputList, listNum):  # repeats the same element in a list
        outputList = []
        for i in inputList:
            outputSublist = []
            for x in range(listNum):
                outputSublist.append(i)
            outputList.append(outputSublist)
        return outputList

    def functionZ(inputList):
        inputList1 = function1(inputList, lenx)
        inputList2 = function1(inputList1, leny)
        return inputList2

    def functionX(inputList):
        inputList1 = function2(inputList, lenz)
        inputList2 = function1(inputList1, leny)
        return inputList2

    def functionY(inputList):
        inputList1 = function2(inputList, lenz)
        inputList2 = function2(inputList1, lenx)
        return inputList2
    for i in x:
        inputX.append(round(float(i), 2))
    for i in y:
        inputY.append(round(float(i), 2))
    for i in z:
        inputZ.append(round(float(i), 2))
    outputTurple = [functionX(inputX), functionY(inputY), functionZ(inputZ)]
    return outputTurple



#Week 5
#EVERY FUCKING THING

def spherical_to_cartesian(r,theta,phi):
    x = round(r * np.sin(theta) * np.cos(phi), 5)
    y = round(r * np.sin(theta) * np.sin(theta), 5)
    z = round(r * np.cos(theta), 5)
    return (x, y, z)

def cartesian_to_spherical(x, y, z):
    smol = 10 ** (-50)
    if (x == 0):
        x = smol
    if (y == 0):
        y = smol
    if (z == 0):
        z = smol
    phi = np.arctan(y / x)
    theta = np.arctan(y / (z * np.sin(phi)))
    r = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    phi = round(phi, 5)
    theta = round(theta, 5)
    r = round(r, 5)
    return (r, theta, phi)

def absolute(cnumber):
    x = cnumber.real
    y = cnumber.imag
    absolute = (x ** 2 + y ** 2) ** 0.5
    return absolute

def angular_wave_func(m,l,theta,phi):
    # y= a * b * c * d
    # global constants
    pi = math.pi
    # constants for a
    aDict = {
        "a00": np.sqrt(1 / (4 * pi)),
        "a01": np.sqrt(3 / (4 * pi)),
        "a02": np.sqrt(5 / (16 * pi)),
        "a03": np.sqrt(7 / (16 * pi)),
        "a11": np.sqrt(3 / (8 * pi)),
        "a12": np.sqrt(15 / (8 * pi)),
        "a13": np.sqrt(21 / (64 * pi)),
        "a22": np.sqrt(15 / (32 * pi)),
        "a23": np.sqrt(105 / (32 * pi)),
        "a33": np.sqrt(35 / (64 * pi))
    }

    def a(x1, x2):  # x1 - dictionary input   x2 - m
        x2 = int(x2)

        if (x2 == 1) or (x2 == 3):
            neg = -1
        else:
            neg = 1

        output = neg * aDict[x1]
        return output

    # constants for b
    def b(x1, x2):  # x1 - ml(str)     x2 - theta(int)
        x2 = float(x2)
        if x1 == "00":
            b00 = float(1)
            return b00
        elif x1 == "01":
            b01 = float(np.cos(x2))
            return b01
        elif x1 == "02":
            b02 = float((3 * (np.cos(x2) ** 2)) - 1)
            return b02
        elif x1 == "03":
            b03 = float((5 * (np.cos(x2) ** 3)) - (3 * np.cos(x2)))
            return b03
        elif x1 == "11":
            b11 = float(1)
            return b11
        elif x1 == "12":
            b12 = float(np.cos(x2))
            return b12
        elif x1 == "13":
            b13 = float((5 * (np.cos(x2)) ** 2) - 1)
            return b13
        elif x1 == "22":
            b22 = float(1)
            return b22
        elif x1 == "23":
            b23 = float(np.cos(x2))
            return b23
        elif x1 == "33":
            b33 = float(1)
            return b33
        else:
            print("variable b error")
            return

    def c(x1, x2):  # x1 - m(str)  x2 - theta(int)
        x1 = abs(int(x1))
        output = float((np.sin(x2)) ** x1)
        return output

    def d(x1, x2):  # x1 - m(str)     x2 - phi(int)
        x1 = int(x1)
        x = x2 * x1
        output = np.cos(x) + (1j) * round(np.sin(x), 5)
        return output

    m = str(m)
    l = str(l)
    ml = m + l
    Ax = "a" + ml
    A = round(a(Ax, m), 5)
    B = round(b(ml, theta), 5)
    C = round(c(m, theta), 5)
    D = round(d(m, phi), 5)

    Y = round(A * B * C * D, 5)
    return Y

def radial_wave_func(n,l,r):
    import scipy.constants as c
    # global constants
    b = c.physical_constants['Bohr radius'][0]  # Bohr's radius
    # normalised means just the term a^(-3/2) is 1
    a = {
        "10": 2,
        "20": np.sqrt(1 / 2),
        "21": np.sqrt(1 / 24),
        "30": np.sqrt(4 / 19683),
        "31": np.sqrt(64 / 4374),
        "32": np.sqrt(16 / 196830),
        "40": np.sqrt(1 / 16),
        "41": np.sqrt(5 / 768),
        "42": np.sqrt(1 / 20480),
        "43": np.sqrt(1 / 20643840)
    }

    def bohr(x1, x2):  # x1 - name     x2 - r(float)
        if (x1 == "10"):
            output = 1
            return output
        elif (x1 == "20"):
            output = 1 - (x2 / (2 * b))
            return output
        elif (x1 == "21"):
            output = x2 / b
            return output
        elif (x1 == "30"):
            output = 27 - (18 * (x2 / b)) + (2 * ((x2 / b) ** 2))
            return output
        elif (x1 == "31"):
            output = (1 - (x2 / (6 * b))) * (x2 / b)
            return output
        elif (x1 == "32"):
            output = (x2 / b) ** 2
            return output
        elif (x1 == "40"):
            output = 1 - ((3 / 4) * (x2 / b)) + ((1 / 8) * ((x2 / b) ** 2)) - ((1 / 192) * ((x2 / b) ** 3))
            return output
        elif (x1 == "41"):
            output = (x2 / b) * (1 - ((1 / 4) * (x2 / b)) + ((1 / 80) * ((x2 / b) ** 2)))
            return output
        elif (x1 == "42"):
            output = ((x2 / b) ** 2) * (1 - (1 / 12) * (x2 / b))
            return output
        elif (x1 == "43"):
            output = (x2 / b) ** 3
            return output
        else:
            print("value B error")
            return

    def c(x1, x2):  # x1 - name      x2 - r(float)
        x1 = int(x1[0])
        output = np.exp((-1) * (x2 / (x1 * b)))
        return output

    # a=c.physical_constants['Bohr radius'][0]
    n = str(n)
    l = str(l)
    nl = n + l
    A = a[nl]
    B = bohr(nl, r)
    C = c(nl, r)
    output = round(A * B * C, 5)
    return output


def linspace(start, stop, *args, **kwargs):
    if (kwargs == {}) and (args == ()):
        times = 50
    elif (args == ()):
        times = kwargs['num']
    elif (kwargs == {}):
        times = args[0]
    interval = (stop - start) / (times - 1)
    iteratingNum = start - interval
    outputList = []
    for i in range(times):
        iteratingNum = iteratingNum + interval
        outputList.append(round(iteratingNum, 5))
    return outputList

def meshgrid(x,y,z):
    inputX = []
    inputY = []
    inputZ = []
    lenx = len(x)
    leny = len(y)
    lenz = len(z)

    def function1(element, elementNum):  # repeats a list in a bigger list
        outputList = []
        for i in range(elementNum):
            outputList.append(element)
        return outputList

    def function2(inputList, listNum):  # repeats the same element in a list
        outputList = []
        for i in inputList:
            outputSublist = []
            for x in range(listNum):
                outputSublist.append(i)
            outputList.append(outputSublist)
        return outputList

    def functionZ(inputList):
        inputList1 = function1(inputList, lenx)
        inputList2 = function1(inputList1, leny)
        return inputList2

    def functionX(inputList):
        inputList1 = function2(inputList, lenz)
        inputList2 = function1(inputList1, leny)
        return inputList2

    def functionY(inputList):
        inputList1 = function2(inputList, lenz)
        inputList2 = function2(inputList1, lenx)
        return inputList2

    for i in x:
        inputX.append(round(float(i), 5))
    for i in y:
        inputY.append(round(float(i), 5))
    for i in z:
        inputZ.append(round(float(i), 5))
    outputTurple = [functionX(inputX), functionY(inputY), functionZ(inputZ)]
    return outputTurple
"""
def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    def numpyArray(max,numberX, numberY, numberZ):
        linspaceOutputX = linspace(0,max,num=numberX)
        linspaceOutputY = linspace(0, max, num=numberY)
        linspaceOutputZ = linspace(0, max, num=numberZ)
        meshgridOutput = meshgrid(linspaceOutputX,linspaceOutputY,linspaceOutputZ)
        print(meshgridOutput)
"""
def numpyArray(max,numberX, numberY, numberZ):
    linspaceOutputX = linspace(-1*max,max,num=numberX)
    linspaceOutputY = linspace(-1*max,max,num=numberY)
    linspaceOutputZ = linspace(-1*max,max,num=numberZ)
    meshgridOutput = meshgrid(linspaceOutputX,linspaceOutputY,linspaceOutputZ)

    def printOutCarteCoordinate(input):
        outputSublist1 = []
        sublistLen1 = len(input[0])
        for i in range(sublistLen1):
            outputSublist2 = []
            sublistLen2 = len(input[0][0])
            for j in range(sublistLen2):
                outputSublist3 = []
                sublistLen3 = len(input[0][0][0])
                for k in range(sublistLen3):
                    outputSublist4 = []
                    for mainLen in range(len(input)):
                        outputSublist4.append(input[mainLen][i][j][k])
                    outputSublist3.append(outputSublist4)
                outputSublist2.append(outputSublist3)
            outputSublist1.append(outputSublist2)
        return outputSublist1

    sortedCoordinate = printOutCarteCoordinate(meshgridOutput)

    def convertToSpherical(input):
        outputSublist1 = []
        sublistLen1 = len(input[0])
        for i in range(sublistLen1):
            outputSublist2 = []
            sublistLen2 = len(input[0][0])
            for j in range(sublistLen2):
                outputSublist3 = []
                sublistLen3 = len(input[0][0][0])
                for k in range(sublistLen3):
                    outputSublist4 = cartesian_to_spherical(input[i][j][k][0],input[i][j][k][1],input[i][j][k][2])

                    outputSublist3.append(outputSublist4)
                outputSublist2.append(outputSublist3)
            outputSublist1.append(outputSublist2)
        return outputSublist1

    def createAbsolute(r,theta,phi):




print(numpyArray(8,3,3,3))