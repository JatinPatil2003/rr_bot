#!/usr/bin/env python3
import rospy
import math
from sensor_msgs.msg import JointState

def control_joints(angles):
    joint_state = JointState()
    joint_state.header.stamp = rospy.Time.now()
    joint_state.name = ['Revolute 4', 'Revolute 5']

    joint_state.position = angles

    joint_publisher.publish(joint_state)
    rate.sleep()

rospy.init_node('joint_control_node', anonymous=True)
joint_publisher = rospy.Publisher('/joint_states', JointState, queue_size=10)
rate = rospy.Rate(50)

while not rospy.is_shutdown():
    input_str = input("Enter angle of arm1 and arm2 (angle1 angle2) in [-180:180] : ")
    position = input_str.split(" ")
    position = list(map(int, position))
    position = list(map(math.radians, position))
    
    control_joints(position)
