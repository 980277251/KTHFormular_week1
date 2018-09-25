#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('Wang', String, queue_size=10)
    rospy.init_node('Jane_talker', anonymous=False)
    rate = rospy.Rate(0.05) # 0.05hz
    i = 0 
    while not rospy.is_shutdown():
		
		published_value = str(i*4)	
		rospy.loginfo(published_value)
		pub.publish(published_value)
		rate.sleep()
		i += 1
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

