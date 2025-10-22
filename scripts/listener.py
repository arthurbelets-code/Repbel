#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo("Listener: Received number %d", msg.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/my_topic', Int32, callback)
    rospy.loginfo("Listener started. Waiting for numbers...")
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
