#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def falando():
    pub = rospy.Publisher('conversando', String, queue_size=20)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        msg= "Bola visualizada %s" % rospy.get_time()
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        falando()
    except rospy.ROSInterruptException:
        pass

