#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32, String

def talker():
    rospy.init_node('talker', anonymous=True)
    
    pub_main = rospy.Publisher('/my_topic', Int32, queue_size=10)
    pub_overflow = rospy.Publisher('/overflow_topic', String, queue_size=10)
    
    rate = rospy.Rate(10)  # 10 Hz

    count = 0
    while not rospy.is_shutdown():
        msg_num = Int32()
        msg_num.data = count
        pub_main.publish(msg_num)
        rospy.loginfo("Talker: Published %d", count)

        if count >= 100:
            alert_msg = String()
            alert_msg.data = f"Overflow! Count reached {count}. Resetting to 0."
            pub_overflow.publish(alert_msg)
            rospy.logwarn(alert_msg.data)
            count = 0  # Сброс
        else:
            count += 2

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
