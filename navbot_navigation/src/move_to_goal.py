#!/usr/bin/env python3
import rospy
import actionlib  #http://wiki.ros.org/actionlib
import sys
import copy
#import moveit_commander
#import moveit_msgs.msg
from geometry_msgs.msg import Pose,Quaternion
import rospkg
import geometry_msgs.msg
from math import pi 
from std_msgs.msg import String
#from moveit_commander.conversions import pose_to_list
from math import radians
from tf.transformations import quaternion_from_euler,euler_from_quaternion
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal  #http://wiki.ros.org/move_base_msgs
from time import sleep

def movebase_client(pose):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move forward along the x and y axis of the "map" coordinate frame(in meter)
    goal.target_pose.pose.position.x = pose.position.x
    
    goal.target_pose.pose.position.y = pose.position.y
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.x = pose.orientation.x
    goal.target_pose.pose.orientation.y = pose.orientation.y
    goal.target_pose.pose.orientation.z = pose.orientation.z
    goal.target_pose.pose.orientation.w = pose.orientation.w
    
   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available

    if wait:
        sleep(2)
        # moveit_poses()

    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()



if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        #get the location of saved text file using ros argument
        rospack = rospkg.RosPack()
        file_path = rospack.get_path('waypoints')
        print(file_path)
        f = open(file_path+"/waypoints/points.txt", "r")
        # iterate through points in file and save as (long,lat) tuple in list points
        points = []
        for lines in f :
            points.append(tuple(map(float,lines.split())))

       
        n = -1
        rate = rospy.Rate(1)
        while n < len(points) -1:
            n+=1
            x = points[n][0]
            y = points[n][1]
            Y = points[n][2]
            
            pose = Pose()
            pose.position.x= x
            pose.position.y= y
            (qx,qy,qz,qw)= quaternion_from_euler(0,0,Y)
            pose.orientation.x= qx
            pose.orientation.y= qy
            pose.orientation.z= qz
            pose.orientation.w= qw
            q =Quaternion()
            q.x=qx
            q.y=qy
            q.z=qz
            q.w=qw
            pose.orientation = q
            result = movebase_client(pose)
            
               
       # moveit_commander.roscpp_shutdown()
        result = movebase_client(pose)
        
        if result:
            rospy.loginfo("Goal execution done!")
            sleep(2)
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
