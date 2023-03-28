#!/usr/bin/env python3

"""
   diff_tf.py - follows the output of a wheel encoder and
   creates tf and odometry messages.
   some code borrowed from the arbotix diff_controller script
   A good reference: http://rossum.sourceforge.net/papers/DiffSteer/
   
    Copyright (C) 2012 Jon Stephan. 
     
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
   
   ----------------------------------
   Portions of this code borrowed from the arbotix_python diff_controller.
   
diff_controller.py - controller for a differential drive
  Copyright (c) 2010-2011 Vanadium Labs LLC.  All right reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:
      * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.
      * Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.
      * Neither the name of Vanadium Labs LLC nor the names of its 
        contributors may be used to endorse or promote products derived 
        from this software without specific prior written permission.
  
  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  DISCLAIMED. IN NO EVENT SHALL VANADIUM LABS BE LIABLE FOR ANY DIRECT, INDIRECT,
  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
  OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
  OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
  ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

import rospy
import roslib
#roslib.load_manifest('differential_drive')
from math import sin, cos, pi

from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist, Pose2D
from nav_msgs.msg import Odometry
from tf.broadcaster import TransformBroadcaster
from std_msgs.msg import Int32

from tf.transformations import euler_from_quaternion, quaternion_from_euler

#############################################################################
class DiffTf:
#############################################################################

    #############################################################################
    def __init__(self):
    #############################################################################
        rospy.init_node("diff_tf")
        self.nodename = rospy.get_name()
        rospy.loginfo("-I- %s started" % self.nodename)
        
        #### parameters #######
        self.rate = rospy.get_param('~rate',10.0)  # the rate at which to publish the transform

        
        self.base_frame_id = rospy.get_param('~base_frame_id','base_link') # the name of the base frame of the robot
        self.odom_frame_id = rospy.get_param('~odom_frame_id', 'wheelodom') # the name of the odometry reference frame
        
      
        self.t_delta = rospy.Duration(1.0/self.rate)
        self.t_next = rospy.Time.now() + self.t_delta
        
        self.x = 0                  # position in xy plane 
        self.y = 0
        self.th = 0
        self.dx = 0                 # speeds in x/rotation
        self.dr = 0
        self.then = rospy.Time.now()

        rospy.Subscriber("pose2D", Pose2D, self.odomposecallback)
        self.odomPub = rospy.Publisher("odom", Odometry,queue_size=10)
        self.odomBroadcaster = TransformBroadcaster()
        
    #############################################################################
    def spin(self):
    #############################################################################
        r = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
           # self.update()
            r.sleep()

    def odomposecallback(self, msg):
       # print("vazha reached callback")
        print(msg.x, msg.y, msg.theta)
        self.x = msg.x
        self.y = msg.y
        now = rospy.Time.now()
        if now > self.t_next:
            elapsed = now - self.then
            self.then = now
            elapsed = elapsed.to_sec()

            # calculate velocities
            self.dx = msg.x / elapsed
            self.dr = msg.y / elapsed
            
            
            quat = quaternion_from_euler (0, 0, msg.theta)
            
            # publish the odom information
            quaternion = Quaternion()
            quaternion.x = 0.0
            quaternion.y = 0.0
            quaternion.z = quat[2]
            quaternion.w = quat[3]

        

            #self.odomBroadcaster.sendTransform(
            #    (self.x, self.y, 0),
             #   (quaternion.x, quaternion.y, quaternion.z, quaternion.w),
              #  rospy.Time.now(),
             #   self.base_frame_id,
              #  self.odom_frame_id
                #)


            odom = Odometry()
            odom.header.stamp = now
            odom.header.frame_id = self.odom_frame_id
            odom.pose.pose.position.x = msg.x
            odom.pose.pose.position.y = msg.y
            odom.pose.pose.position.z = 0
            odom.pose.pose.orientation = quaternion
            odom.child_frame_id = self.base_frame_id
            odom.twist.twist.linear.x = self.dx
            odom.twist.twist.linear.y = 0
            odom.twist.twist.angular.z = self.dr
            self.odomPub.publish(odom)
            

#############################################################################
#############################################################################
if __name__ == '__main__':
    """ main """
    diffTf = DiffTf()
    diffTf.spin()
    
    
   
