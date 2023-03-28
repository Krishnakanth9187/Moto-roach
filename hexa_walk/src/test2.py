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
    kit1.servo[0].angle = 180 #tibia1
    kit1.servo[1].angle = 100 #femur1
    kit1.servo[2].angle = 90 #coxa1
    kit1.servo[4].angle = 180
    kit1.servo[5].angle = 100
    kit1.servo[6].angle = 80
    kit1.servo[8].angle = 180
    kit1.servo[9].angle = 100
    kit1.servo[10].angle = 90
    kit.servo[7].angle = 0  #tibia
    kit.servo[6].angle = 80 #femur
    kit.servo[5].angle = 80 #coxa
    kit.servo[11].angle = 0
    kit.servo[10].angle = 80
    kit.servo[9].angle = 80
    kit.servo[15].angle = 0
    kit.servo[14].angle = 90
    kit.servo[13].angle = 80


    time.sleep(1)
def tripod_forward():
   kit = ServoKit(channels=16)
   kit1 = ServoKit1(channels=16)
   kit.servo[6].angle = 50
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 120
   time.sleep(0.5)
   kit.servo[5].angle = 100
   kit.servo[13].angle = 100
   kit1.servo[6].angle = 50
   time.sleep(1)
   kit.servo[6].angle =80
   kit.servo[14].angle = 90
   kit1.servo[5].angle = 100
   time.sleep(1)
   kit.servo[10].angle = 50
   kit1.servo[1].angle = 130
   kit1.servo[9].angle = 130
   time.sleep(1)
   kit.servo[5].angle = 80
   kit.servo[13].angle = 80
   kit1.servo[6].angle = 80
   time.sleep(1)
   kit.servo[9].angle = 100
   kit1.servo[2].angle = 60
   kit1.servo[10].angle = 60
   time.sleep(1)
   kit.servo[10].angle = 80
   kit1.servo[1].angle = 100
   kit1.servo[9].angle = 100
   time.sleep(1)
   kit.servo[6].angle = 50
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 130
   time.sleep(1)
   kit.servo[9].angle = 80
   kit1.servo[2].angle = 90
   kit1.servo[10].angle = 90
   time.sleep(0.5)
     
def tripod_backward():
   kit = ServoKit(channels=16)
   kit1 = ServoKit1(channels=16)
   kit.servo[6].angle = 50
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 130
   time.sleep(0.5)
   kit.servo[5].angle = 50
   kit.servo[13].angle = 50
   kit1.servo[6].angle = 110
   time.sleep(1)
   kit.servo[6].angle = 80
   kit.servo[14].angle = 90
   kit1.servo[5].angle = 100
   time.sleep(1) 
   kit.servo[10].angle = 50
   kit1.servo[1].angle = 130
   kit1.servo[9].angle = 130
   time.sleep(1)
   kit.servo[5].angle = 80
   kit.servo[13].angle = 80
   kit1.servo[6].angle = 80
   time.sleep(1)
   kit.servo[9].angle = 50
   kit1.servo[2].angle = 120
   kit1.servo[10].angle = 120
   time.sleep(1)
   kit.servo[10].angle = 80
   kit1.servo[1].angle = 100
   kit1.servo[9].angle = 100
   time.sleep(1)
   kit.servo[6].angle = 50
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 130
   time.sleep(1)
   kit.servo[9].angle = 80
   kit1.servo[2].angle = 90
   kit1.servo[10].angle = 90
   time.sleep(0.5)

def tripod_clockwise():
   kit = ServoKit(channels=16)
   kit1 = ServoKit1(channels=16)
   kit.servo[6].angle = 50
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 130
   time.sleep(0.5)
   kit.servo[5].angle = 110
   kit.servo[13].angle = 110
   kit1.servo[6].angle = 110
   time.sleep(1)
   kit.servo[6].angle = 80
   kit.servo[14].angle = 90
   kit1.servo[5].angle = 100
   time.sleep(1) 
   kit.servo[10].angle = 50
   kit1.servo[1].angle = 130
   kit1.servo[9].angle = 130
   time.sleep(1)
   kit.servo[5].angle = 80
   kit.servo[13].angle = 80
   kit1.servo[6].angle = 80
   time.sleep(1)
   kit.servo[9].angle = 110
   kit1.servo[2].angle = 120
   kit1.servo[10].angle = 120
   time.sleep(1)
   kit.servo[10].angle = 80
   kit1.servo[1].angle = 100
   kit1.servo[9].angle = 100
   time.sleep(1)
   kit.servo[6].angle = 50
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 130
   time.sleep(1)
   kit.servo[9].angle = 80
   kit1.servo[2].angle = 90
   kit1.servo[10].angle = 90
   time.sleep(0.5)

def tripod_anticlockwise():
   kit = ServoKit(channels=16)
   kit1 = ServoKit1(channels=16)
   kit.servo[6].angle = 50
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 130
   time.sleep(0.5)
   kit.servo[5].angle = 50
   kit.servo[13].angle = 50
   kit1.servo[6].angle = 50
   time.sleep(1)
   kit.servo[6].angle = 80
   kit.servo[14].angle = 90
   kit1.servo[5].angle = 100
   time.sleep(1) 
   kit.servo[10].angle = 50
   kit1.servo[1].angle = 130
   kit1.servo[9].angle = 130
   time.sleep(1)
   kit.servo[5].angle = 80
   kit.servo[13].angle = 80
   kit1.servo[6].angle = 80
   time.sleep(1)
   kit.servo[9].angle = 50
   kit1.servo[2].angle = 60
   kit1.servo[10].angle = 60
   time.sleep(1)
   kit.servo[10].angle = 80
   kit1.servo[1].angle = 100
   kit1.servo[9].angle = 100
   time.sleep(1)
   kit.servo[6].angle = 50
   kit.servo[14].angle = 60
   kit1.servo[5].angle = 130
   time.sleep(1)
   kit.servo[9].angle = 80
   kit1.servo[2].angle = 90
   kit1.servo[10].angle = 90
   time.sleep(0.5)

#hom
#ripod_forward()
#while True:
    #tripod_clockwise()
