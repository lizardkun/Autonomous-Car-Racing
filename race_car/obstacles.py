#!/usr/bin/env python
import rospy
import random
from std_msgs.msg import String



rospy.init_node('obstacle_publisher', anonymous=True)
obstacle_pub = rospy.Publisher('/obstacle', String, queue_size=10)
def obstacle_publisher():

    rate = rospy.Rate(1)  
    while not rospy.is_shutdown():
        block_width = 80
        block_height = 20
        block_x = random.randrange(100, 380 - block_width)
        block_y = -100

        obstacle_msg = f"{block_x},{block_y},{block_width},{block_height}"
        rospy.loginfo(obstacle_msg)
        obstacle_pub.publish(obstacle_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        # obstacle_publisher()
        obstacle_publisher()
    except rospy.ROSInterruptException:
        pass
