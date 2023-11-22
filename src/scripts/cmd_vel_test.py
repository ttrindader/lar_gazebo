#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

def publish_twist():
    rospy.init_node('twist_publisher_node', anonymous=True)
    rate = rospy.Rate(10)  # 1 Hz

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    twist = Twist()
    twist.linear.x = 0.0
    twist.angular.z = 0.0

    max_linear = 1.0
    max_angular = 2.0

    while not rospy.is_shutdown():

        if twist.linear.x >= max_linear and twist.angular.z >= max_angular:
            time.sleep(1.0)
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            
        else:
            time.sleep(0.2)
            twist.linear.x = min(twist.linear.x + 0.01, max_linear)
            twist.angular.z = min(twist.angular.z + 0.02, max_angular)    
            
        pub.publish(twist)            


        rate.sleep()

if __name__ == '__main__':
    try:
        publish_twist()
    except rospy.ROSInterruptException:
        pass
