#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import csv

def write_file():
    # write the information from the sensor into a file
    with open('temperatures.csv', 'wb') as csvfile:
        tempwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        tempwriter.writerow(['Temperature','Humidity','Year','Month','Day','Hour','Minute'])

        while True:
            humidity, temperature = get_data()
            t = time.localtime()
            tempwriter.writerow([temperature,humidity,t[0],t[1],t[2],t[3],t[4]])
            time.sleep(1800) # 30 min

def get_data():
    # get sensor-data from the raspberry
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return (humidity, temperature)

#main function
write_file()
