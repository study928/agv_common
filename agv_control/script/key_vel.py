#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node("keyboard_cmd_led")
pub = rospy.Publisher("/cmd_led", String, queue_size=10)

while not rospy.is_shutdown():
    direction = raw_input("1: on, return: off >")
    if "1" in direction: msg = "1"
    else: msg = "0"
    print msg
    pub.publish(msg)