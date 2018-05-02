import os
import time
import numpy as np
"""
This program controls the sensor and appends its data into a file 'data.txt'
which is found in the same folder as it.
The data is in a form of a list in the format [actual temperature, first reading
time, first reading, second reading time, second reading, ... , sixth reading
time, sixth reading]

To use:
-Turn on program
-When the temperature of an actual thermometer reaches a temperature we want,
type that temperature into the input, put the sensor into the hot water bottle
and press enter
-When the program has recorded the data it needs, and outputs a long dotted line
we could remove the sensor from the hot water, and wait till thermometer reaches
favourable temperature again.

"""



def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20



 
def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit



 
def loop(ds18b20):
    while True:
        counter = 1
        output = []
        input_temp = input("Pweez input ze temperaturez! XDXD: ")
        output.append(input_temp)
        start = time.time()
        if read(ds18b20) != None:
            output.append(str(time.time()-start))
            output.append(read(ds18b20)[0])
        while counter < 7:
            while time.time() - start < 5*counter:
                pass
            if read(ds18b20) != None:
                output.append(str(time.time()-start))
                output.append(read(ds18b20)[0])
            counter += 1
            print('.')
        print('Dict: {0}'.format(output))
        
        with open('data.txt', 'a') as myfile:
            myfile.write('{0}\r'.format(output))
        print("Wow we're donez!! So fast rawr XDXDXD")
        print("---------------------------------------------------------")
        
            
        



"""
def write(l):
    string = ""
    for pair in l:
        string = string + str(pair[0]) + " " + str(pair[1]) + "\n"
    fout = open("%s_%s_temperature_readings.txt"%(true_temperature,run),"w")
    fout.write(string)
    fout.close()
"""

def kill():
    quit()
 
if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()
