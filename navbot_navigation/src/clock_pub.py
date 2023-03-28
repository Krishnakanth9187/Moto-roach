#!/usr/bin/env python3

#from beginner_tutorials.srv import TimeDiff, TimeDifResponse

from std_msgs.msg import Time

import rospy
import roslib

pub = rospy.Publisher('clock', Time, queue_size=10)
#CurrentTime= rospy.Time.now()

def setupPublisher():
    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5) # 5hz

    while not rospy.is_shutdown():

        global CurrentTime
        CurrentTime= rospy.Time.now()
        pub.publish(CurrentTime)
        rate.sleep()

if __name__ == "__main__":
    setupPublisher()
