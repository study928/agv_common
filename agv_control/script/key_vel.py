#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

rospy.init_node("keyboard_cmd_vel")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

while not rospy.is_shutdown():
    vel = Twist()
    direction = raw_input("8: go, 2: back, 6: right, 4: left, return: stop >")
    if "8" in direction: vel.linear.x = 0.05
    if "2" in direction: vel.linear.x = -0.05
    if "6" in direction: vel.angular.z = 3.14/4
    if "4" in direction: vel.angular.z = -3.14/4
    print vel
    pub.publish(vel)