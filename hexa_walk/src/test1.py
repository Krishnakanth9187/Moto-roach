#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time
from adafruit_servokit import ServoKit
from adafruit_servokit1 import ServoKit1
from test2 import init_driver, home, tripod_forward, tripod_backward, tripod_clockwise, tripod_anticlockwise 

def callback(data):
    print(data.linear.x,data.angular.z)
    if data.linear.x > 0 and data.angular.z == 0:
        print("tripod_forward")
        tripod_forward()
    elif data.linear.x < 0 and data.angular.z == 0:
        print("tripod_backward")	
        tripod_backward()
    elif data.linear.x == 0 and data.angular.z < 0:
        print("tripod_clockwise")
        tripod_clockwise()
    elif data.linear.x == 0 and data.angular.z > 0:
        print("tripod_anticlockwise")
        tripod_anticlockwise()
    elif data.linear.x == 0 and data.angular.z == 0:
        print("home")
        home()
    else:
        print("curve")
        tripod_forward()
    

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("cmd_vel", Twist, callback, queue_size = 1)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    init_driver()
    listener()
