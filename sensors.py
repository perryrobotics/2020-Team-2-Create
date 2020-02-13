#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
  
    
def analog_avg(port, num):
	total = 0
	for reading in range(num):
		total += KIPR.analog(port)
	return total/num