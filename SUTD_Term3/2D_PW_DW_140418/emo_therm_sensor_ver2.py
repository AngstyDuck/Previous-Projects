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
    """
    Searches directory and returns position of temperature sensor

    Input:
    None

    Output:
    Position of temperature sensor

    Modules:
    os,

    """

    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20



 
def read(ds18b20):
    """
    This function outputs the temperature recorded by the Rpi sensor

    Input:
    None

    Output:
    A turple, first element is temperature in celcius, second element is
    temperature in farenheit

    """
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
    """
    Asks for the actual temperature of the water (ranging from 10 to 60 degrees
    in 5 degree intervals). Records instance of time and temperature recorded by sensor
    at that instance and saves everything in a text file within a folder. Each experiment
    where the temperature of the water is the same, would be stored within the same folder.
    Instance of time and temperature will be recorded whenever possible, hence the interval
    between recordings is slightly irregular.

    Input:
    Location of sensor

    Output:
    Textfile. Every experiment would be represented by a string where the first number
    represents the actual temperature of the water, and subsequent numbers are the instance
    of time, and the temperature recorded. All these numbers are separated by string.
    e.g.
    '(temperature of water) (first instance of time) (temperature recorded at first instance)
     (second instance of time) (temperature recorded at second instance) ... (last
     instance of time) (temperature recorded at last instance)\n'

    Functions:
    read,

    Modules:
    Time,

    """

    while True:
        counter = 1
        output = ""
        input_temp = input("Pweez input ze temperaturez! XDXD: ")
        output += "{0} ".format(input_temp)
        start = time.time()
        while time.time()-start < 30:
            if read(ds18b20) != None:
                output += "{0} {1} ".format(time.time()-start,read(ds18b20)[0])
            counter += 1
            print('.')
        print('str: {0}'.format(output))
        with open('data_real_2.txt', 'a') as myfile:
            myfile.write('{0}\n'.format(output))
        print("Wow we're donez!! So fast rawr XDXDXD")
        print("---------------------------------------------------------")
        
            


def kill():
    quit()
 
if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()
