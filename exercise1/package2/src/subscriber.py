#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float32

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    global a
    a = int(data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Jane_getter', anonymous=True)

    rospy.Subscriber("Wang", String, callback)
    pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
    #rate = rospy.Rate(0.05) # 0.05hz

    while not rospy.is_shutdown():
    	global a
    	rospy.wait_for_message('Wang',Float32)
    	published_value = a/0.15
    	rospy.loginfo(published_value)
    	pub.publish(published_value)
    	#rate.sleep()
		
    # spin() simply keeps python from exiting until this node is stopped
    # rospy.spin()

if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass

