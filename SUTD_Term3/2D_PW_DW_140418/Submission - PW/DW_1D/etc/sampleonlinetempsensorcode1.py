# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:37:41 2018

@author: seahe
"""

import os
import time

#collect data for #dur# seconds
dur = 30
#collect data for the target temperature of #true_temperature#
true_temperature = 57
#collect data for run number #run#
run = 2


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
    output = []
    start = time.time()
    while True:
        if read(ds18b20) != None:
            print (time.time()-start)
            print ("Current temperature : %0.3f C" % read(ds18b20)[0])


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
