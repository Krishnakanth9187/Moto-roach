#!/usr/bin/env python3
import time
from adafruit_servokit import ServoKit
from adafruit_servokit1 import ServoKit1
def init_driver():
    kit = ServoKit(channels=16)
    kit1 = ServoKit1(channels=16)
def home():
    kit = ServoKit(channels=16)
    kit1 = ServoKit1(channels=16)
    kit1.servo[0].angle = 180
    kit1.servo[1].angle = 120
    kit1.servo[2].angle = 90
    kit1.servo[4].angle = 180
    kit1.servo[5].angle = 120
    kit1.servo[6].angle = 90
    kit1.servo[8].angle = 180
    kit1.servo[9].angle = 120
    kit1.servo[10].angle = 90
    kit.servo[5].angle = 90
    kit.servo[6].angle = 60
    kit.servo[7].angle = 0
    kit.servo[9].angle = 90
    kit.servo[10].angle = 60
    kit.servo[11].angle = 0
    kit.servo[13].angle = 90
    kit.servo[14].angle = 60
    kit.servo[15].angle = 0
    time.sleep(1)
def tripod_forward():
   kit = ServoKit(channels=16)
   kit1 = ServoKit1(channels=16)
   kit.servo[6].angle = 30
   kit.servo[14].angle = 30
   kit1.servo[5].angle = 150
   time.sleep(0.25)
   kit.servo[5].angle = 120
   kit.servo[13].angle = 120
   kit1.servo[6].angle = 60
   time.sleep(0.5)
   kit.servo[6].angle = 60
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 120
   time.sleep(0.5) 
   kit.servo[10].angle = 30
   kit1.servo[1].angle = 150
   kit1.servo[9].angle = 150
   time.sleep(0.5)
   kit.servo[5].angle = 90
   kit.servo[13].angle = 90
   kit1.servo[6].angle = 90
   time.sleep(0.5)
   kit.servo[9].angle = 120
   kit1.servo[2].angle = 60
   kit1.servo[10].angle = 60
   time.sleep(0.5)
   kit.servo[10].angle = 60
   kit1.servo[1].angle = 120
   kit1.servo[9].angle = 120
   time.sleep(0.5)
   kit.servo[6].angle = 30
   kit.servo[14].angle = 30
   kit1.servo[5].angle = 150
   time.sleep(0.5)
   kit.servo[9].angle = 90
   kit1.servo[2].angle = 90
   kit1.servo[10].angle = 90
   time.sleep(0.25)
     
def tripod_backward():
   kit = ServoKit(channels=16)
   kit1 = ServoKit1(channels=16)
   kit.servo[6].angle = 30
   kit.servo[14].angle = 30
   kit1.servo[5].angle = 150
   time.sleep(0.5)
   kit.servo[5].angle = 60
   kit.servo[13].angle = 60
   kit1.servo[6].angle = 120
   time.sleep(1)
   kit.servo[6].angle = 60
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 120
   time.sleep(1) 
   kit.servo[10].angle = 30
   kit1.servo[1].angle = 150
   kit1.servo[9].angle = 150
   time.sleep(1)
   kit.servo[5].angle = 90
   kit.servo[13].angle = 90
   kit1.servo[6].angle = 90
   time.sleep(1)
   kit.servo[9].angle = 60
   kit1.servo[2].angle = 120
   kit1.servo[10].angle = 120
   time.sleep(1)
   kit.servo[10].angle = 60
   kit1.servo[1].angle = 120
   kit1.servo[9].angle = 120
   time.sleep(1)
   kit.servo[6].angle = 30
   kit.servo[14].angle = 30
   kit1.servo[5].angle = 150
   time.sleep(1)
   kit.servo[9].angle = 90
   kit1.servo[2].angle = 90
   kit1.servo[10].angle = 90
   time.sleep(0.5)

def tripod_clockwise():
   kit = ServoKit(channels=16)
   kit1 = ServoKit1(channels=16)
   kit.servo[6].angle = 30
   kit.servo[14].angle = 30
   kit1.servo[5].angle = 150
   time.sleep(0.5)
   kit.servo[5].angle = 120
   kit.servo[13].angle = 120
   kit1.servo[6].angle = 120
   time.sleep(1)
   kit.servo[6].angle = 60
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 120
   time.sleep(1) 
   kit.servo[10].angle = 30
   kit1.servo[1].angle = 150
   kit1.servo[9].angle = 150
   time.sleep(1)
   kit.servo[5].angle = 90
   kit.servo[13].angle = 90
   kit1.servo[6].angle = 90
   time.sleep(1)
   kit.servo[9].angle = 120
   kit1.servo[2].angle = 120
   kit1.servo[10].angle = 120
   time.sleep(1)
   kit.servo[10].angle = 60
   kit1.servo[1].angle = 120
   kit1.servo[9].angle = 120
   time.sleep(1)
   kit.servo[6].angle = 30
   kit.servo[14].angle = 30
   kit1.servo[5].angle = 150
   time.sleep(1)
   kit.servo[9].angle = 90
   kit1.servo[2].angle = 90
   kit1.servo[10].angle = 90
   time.sleep(0.5)

def tripod_anticlockwise():
   kit = ServoKit(channels=16)
   kit1 = ServoKit1(channels=16)
   kit.servo[6].angle = 30
   kit.servo[14].angle = 30
   kit1.servo[5].angle = 150
   time.sleep(0.5)
   kit.servo[5].angle = 60
   kit.servo[13].angle = 60
   kit1.servo[6].angle = 60
   time.sleep(1)
   kit.servo[6].angle = 60
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 120
   time.sleep(1) 
   kit.servo[10].angle = 30
   kit1.servo[1].angle = 150
   kit1.servo[9].angle = 150
   time.sleep(1)
   kit.servo[5].angle = 90
   kit.servo[13].angle = 90
   kit1.servo[6].angle = 90
   time.sleep(1)
   kit.servo[9].angle = 60
   kit1.servo[2].angle = 60
   kit1.servo[10].angle = 60
   time.sleep(1)
   kit.servo[10].angle = 60
   kit1.servo[1].angle = 120
   kit1.servo[9].angle = 120
   time.sleep(1)
   kit.servo[6].angle = 30
   kit.servo[14].angle = 30
   kit1.servo[5].angle = 150
   time.sleep(1)
   kit.servo[9].angle = 90
   kit1.servo[2].angle = 90
   kit1.servo[10].angle = 90
   time.sleep(0.5)



#home()
#while True:
    #tripod_clockwise()
