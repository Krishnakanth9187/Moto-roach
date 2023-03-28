#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from actionlib_msgs.msg import GoalStatusArray
from std_msgs.msg import Float64, String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped




def callback(sub1):
      if len(sub1.status_list) != 0:
          if sub1.status_list[0].text == "Goal reached.":
            # print("l")
             twist_msg = TwistMsg()
             twist = twist_msg.twist
             twist.linear.x = 0
             twist.linear.y = 0
             twist.linear.z = 0
             twist.angular.x = 0
             twist.angular.y = 0
             twist.angular.z = 0
             pub1.publish(twist)

    
def listener():
    rospy.init_node('listener', anonymous=True)
    sub1 = rospy.Subscriber("move_base/status", GoalStatusArray, callback)
    rospy.spin()


if __name__ == '__main__':
    TwistMsg = TwistStamped
    pub1 = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    listener()
