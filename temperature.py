#!/usr/bin/python
import sys
import Adafruit_DHT

loop_nr = 0
while True:
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	loop_nr += 1
	print 'Temp: {0:0.1f} C Humidity: {1:0.1f} % Loop: {2}'.format(temperature, humidity, loop_nr)

