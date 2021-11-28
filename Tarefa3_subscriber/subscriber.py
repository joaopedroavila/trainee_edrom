#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "Dado recebido: %s", data.data)

def ouvinte():
    rospy.init_node('ouvinte', anonymous=True)
    rospy.Subscriber("falando", String, callback)
    rospy.spin()



if __name__ == '__main__':
   ouvinte()
    

