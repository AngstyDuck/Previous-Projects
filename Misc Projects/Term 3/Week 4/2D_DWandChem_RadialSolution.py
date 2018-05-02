import scipy.constants as c
import numpy as np 
import math

#global constants
b = c.physical_constants['Bohr radius'][0]    #Bohr's radius


#normalised means just the term a^(-3/2) is 1
a = {
"10":2,
"20":np.sqrt(1/2),
"21":np.sqrt(1/24),
"30":np.sqrt(4/19683),
"31":np.sqrt(64/4374),
"32":np.sqrt(16/196830),
"40":np.sqrt(1/16),
"41":np.sqrt(5/768),
"42":np.sqrt(1/20480),
"43":np.sqrt(1/20643840)
}

def bohr(x1,x2):     #x1 - name     x2 - r(float)
    if (x1=="10"):
        output = 1
        return output
    elif (x1=="20"):
        output = 1 - (x2/(2*b))
        return output
    elif (x1=="21"):
        output = x2/b
        return output
    elif (x1=="30"):
        output = 27 - (18*(x2/b)) + (2*((x2/b)**2))
        return output
    elif (x1=="31"):
        output = (1 - (x2/(6*b)))*(x2/b)
        return output
    elif (x1=="32"):
        output = (x2/b)**2
        return output
    elif (x1=="40"):
        output = 1 - ((3/4)*(x2/b)) + ((1/8)*((x2/b)**2)) - ((1/192)*((x2/b)**3))
        return output
    elif (x1=="41"):
        output = (x2/b)*(1 - ((1/4)*(x2/b)) + ((1/80)*((x2/b)**2)))
        return output
    elif (x1=="42"):
        output = ((x2/b)**2)*(1-(1/12)*(x2/b))
        return output
    elif (x1=="43"):
        output = (x2/b)**3
        return output
    else:
        print("value B error")
        return

    
def c(x1,x2):     #x1 - name      x2 - r(float)
    x1 = int(x1[0])
    output = np.exp((-1)*(x2/(x1*b)))
    return output
    



def radial_wave_func(n,l,r):
    #a=c.physical_constants['Bohr radius'][0]
    n = str(n)
    l = str(l)
    nl = n+l
    
    A = a[nl]
    B = bohr(nl,r)
    C = c(nl,r)
    
    output = round(A * B * C,5)
    return output