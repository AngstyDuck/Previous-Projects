import numpy as np
import math
import copy


"""
y= a * b * c * d
where,
a = square root expression together with the need to have '-1'
b = cosine expression
c = sine expression
d = exponential expression

bugs mitigated:
apparently np.sin(math.pi)) != 0
I round this expression to make it zero (in line 102)

"""

#global constants
pi = math.pi




#expression for a
aDict={
"a00":np.sqrt(1/(4*pi)),
"a01":np.sqrt(3/(4*pi)),
"a02":np.sqrt(5/(16*pi)),
"a03":np.sqrt(7/(16*pi)),
"a11":np.sqrt(3/(8*pi)),
"a12":np.sqrt(15/(8*pi)),
"a13":np.sqrt(21/(64*pi)),
"a22":np.sqrt(15/(32*pi)),
"a23":np.sqrt(105/(32*pi)),
"a33":np.sqrt(35/(64*pi))
}
def a(x1,x2): #x1 - dictionary input   x2 - m
    x2 = int(x2)
    
    if (x2==1) or (x2==3):   #to check for the need to multiply expression by -1
        neg = -1
    else:
        neg = 1
        
    output = neg * aDict[x1]
    return output



#expression for b
def b(x1,x2):  #x1 - ml(str)     x2 - theta(int)
    x2 = float(x2)
    if x1 == "00":
        b00 = float(1)
        return b00
    elif x1 == "01":
        b01 = float(np.cos(x2))
        return b01
    elif x1 == "02":
        b02 = float((3*(np.cos(x2)**2))-1)
        return b02
    elif x1 == "03":
        b03 = float((5*(np.cos(x2)**3))-(3*np.cos(x2)))
        return b03
    elif x1 == "11":
        b11 = float(1)
        return b11
    elif x1 == "12":
        b12 = float(np.cos(x2))
        return b12
    elif x1 == "13":
        b13 = float((5*(np.cos(x2))**2) - 1)
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
    

   
#expression for c   
def c(x1,x2):    #x1 - m(str)  x2 - theta(int)
    x1 = abs(int(x1))
    output = float((np.sin(x2))**x1)
    return output



#expression for d
def d(x1, x2):     #x1 - m(str)     x2 - phi(int)
    x1 = int(x1)
    x = x2*x1
    output = np.cos(x) + (1j)*round(np.sin(x),5)   #had to round the sine expression cos of bug(explained on the top)
    return output




#putting everything together
def angular_wave_func(m,l,theta,phi):
    
    m = str(m)
    l = str(l)
    ml = m + l
    Ax = "a" + ml    #to create the name to input into the dictionary involved in function a
    
    A = round(a(Ax,m),5)
    B = round(b(ml,theta),5)
    C = round(c(m, theta),5)
    D = round(d(m, phi),5)
    
    
    Y = round(A*B*C*D,5)
    
    return Y
    
    