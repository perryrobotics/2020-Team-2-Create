#!/usr/bin/python
import os, sys
import ctypes
from motion import *
from effectors import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")


ARM_PORT = 3
ARM_D = 1017
ARM_U = 746
ARM_B= 2010
ARM_S = 550
CLAW_PORT = 1
CLAW_O = 1550
CLAW_C = 183
    
def move_servo_slow(port, current_pos, end_pos,step):
	if end_pos < current_pos:
		step = -step
	for pos in range(current_pos, end_pos, step):
		KIPR.set_servo_position(port, pos)
  		KIPR.msleep(40)
	KIPR.set_servo_position(port,end_pos)
            
            
def armup(step):
	move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_U, step)
        
def armdown(step):
	move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_D, step)
        
def armback(step):
	move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_B, step)
  
def armstart(step):
	move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_S, step)
        
def clawopen(step):
	move_servo_slow(CLAW_PORT, KIPR.get_servo_position(CLAW_PORT), CLAW_O, step)
        
def clawclose(step):
	move_servo_slow(CLAW_PORT, KIPR.get_servo_position(CLAW_PORT), CLAW_C, step)
        
        


    
    

    