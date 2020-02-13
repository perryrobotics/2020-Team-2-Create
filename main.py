#!/usr/bin/python
import os, sys
import ctypes
from motion import *
from effectors import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

    
#starting arm position is 2047
def main():
	print ("Hello Cruel Botball World")
	KIPR.enable_servos()
	KIPR.create_connect()
	CCW(75, 50)
	forward(75, 1000)
	backward(100, 50)
	CCW(75, 90)
	forward(100, 750)
	backward(100, 200)
	CW(75, 45)
	armup(1000)
	
        
	
	KIPR.create_disconnect()


        
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
