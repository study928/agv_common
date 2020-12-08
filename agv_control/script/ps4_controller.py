#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, actionlib
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from actionlib_msgs.msg import GoalID

class JoyLed():
    def __init__(self):
        self._joy_sub = rospy.Subscriber("/joy", Joy, self.joy_callback, queue_size=1)
        self._vel_pub = rospy.Publisher("/joystick/cmd_vel", Twist, queue_size=1)
        self._led_pub = rospy.Publisher("/cmd_led", String, queue_size=1)
        self._goalid_pub = rospy.Publisher("/move_base/cancel", GoalID, queue_size=1)
        self.set_led("0") # cmd_ledの初期値
        self.set_vel(0.0, 0.0) # cmd_velの初期値

    # cmd_velをjoy_callback関数から受け取ってpublish
    def set_vel(self, vx, vth):
        twist = Twist()
        twist.linear.x = vx
        twist.angular.z = vth

        self._vel_pub.publish(twist)
        del twist

    # cmd_ledをjoy_callback関数から受け取っとpablish
    # cmd_ledが0でled消灯,1で点灯
    def set_led(self, msg):
        message = msg 
        self._led_pub.publish(message)

        del message

    # 実行中のnavigationをキャンセルする
    def set_cancel(self, secs, nsecs):
        goalid = GoalID()
        goalid.stamp.secs = secs
        goalid.stamp.nsecs = nsecs

        self._goalid_pub.publish(goalid)
        del goalid
        
    def joy_callback(self, joy_msg):   
        # ps4の四角ボタンが押された時
        if joy_msg.buttons[0] == 1:
            vx = joy_msg.axes[7] * 0.3 # ps4コントローラの上下 * 0.3
            vth = joy_msg.axes[6] * 3.14 / 4 # ps4コントローラの左右 * 0.3
            self.set_vel(vx, vth)

        # ps4のバツボタンが押された時
        elif joy_msg.buttons[1] == 1:
            msg = str(1) # str型で1を送る
            self.set_led(msg)

        # ps4の丸ボタンが押された時
        elif joy_msg.buttons[2] == 1:
            vx = 0.0
            vth = 0.0
            secs = 0
            necs = 0
            self.set_vel(vx, vth)
            self.set_cancel(secs, necs)

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