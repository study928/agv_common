#!/usr/bin/env python 

import rospy
from geometry_msgs.msg import Twist

def callback_cmd_vel(msg):
    vx = msg.linear.x
    vth = msg.angular.z
    if vx != 0.0 or vth != 0.0:
        rospy.loginfo('Receved cmd_vel')
    
def lisner():
    rospy.init_node('sub_test', anonymous=True)
    rospy.Subscriber("/cmd_vel", Twist, callback_cmd_vel)
    rospy.spin()

if __name__ == "__main__":
    lisner()
