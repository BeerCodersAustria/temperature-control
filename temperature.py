#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import csv

def write_file():
    # write the information from the sensor into a file
    while True:
        checkday = time.localtime()
        filename = str(checkday[0])+'_'+str(checkday[1])+'_'+str(checkday[2])+'.csv'
        
        with open(filename, 'wb') as csvfile:
            tempwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            tempwriter.writerow(['Temperature','Humidity','Year','Month','Day','Hour','Minute'])
            t = time.localtime()
            
            # check if it is still the same day
            while checkday[2] == t[2]:
                humidity, temperature = get_data()
                t = time.localtime()
                tempwriter.writerow([temperature,humidity,t[0],t[1],t[2],t[3],t[4]])
                time.sleep(3600) # 60 min

def get_data():
    # get sensor-data from the raspberry
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return (humidity, temperature)

#main function
write_file()
