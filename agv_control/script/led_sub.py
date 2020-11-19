#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, time
import RPi.GPIO as GPIO
from std_msgs.msg import String

led_pin = 25

def callback(msg):
    #rospy.loginfo('I heard %s', msg.data)
    curr_value = int(msg.data)

    GPIO.output(led_pin, curr_value)

def listener():
    rospy.init_node('led_sub')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)
    rospy.Subscriber("/cmd_led", String, callback)
    rospy.spin()
    GPIO.cleanup()

if __name__ == "__main__":
    listener()
