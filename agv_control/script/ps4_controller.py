#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, time
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class JoyLed():
    def __init__(self):
        self._joy_sub = rospy.Subscriber("/joy", Joy, self.joy_callback, queue_size=1)
        self._vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self._led_pub = rospy.Publisher("/cmd_led", String, queue_size=1)
        self.set_led("0")
        self.set_vel(0.0, 0.0)

    def set_vel(self, vx, vth):
        twist = Twist()
        twist.linear.x = vx
        twist.angular.z = vth

        self._vel_pub.publish(twist)
        del twist

    def set_led(self, msg):
        message = msg 
        self._led_pub.publish(message)

        del message

    def joy_callback(self, joy_msg):
        if joy_msg.buttons[2] == 1:
            msg = str(1)
            self.set_led(msg)
        
        elif joy_msg.buttons[0] == 1:
            vx = joy_msg.axes[7] * 0.3
            vth = joy_msg.axes[6] * 3.14 / 4
            self.set_vel(vx, vth)

        else :
            msg = str(0)
            vx = joy_msg.axes[7] * 0.0
            vth = joy_msg.axes[6] * 0.0

            self.set_led(msg)
            self.set_vel(vx, vth)
            

if __name__ == "__main__":
    rospy.init_node("ps4_controller")
    led_on_off = JoyLed()
    rospy.spin()