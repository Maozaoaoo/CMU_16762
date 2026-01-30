#!/usr/bin/env python3
import time
import rclpy
import numpy as np
import hello_helpers.hello_misc as hm

class MyNode(hm.HelloNode):
    def __init__(self):
        hm.HelloNode.__init__(self)

    def main(self):
        hm.HelloNode.main(self, 'my_node', 'my_node', wait_for_first_pointcloud=False)
        # my_node's main logic goes here
    
        print("Stowing robot...")
        node.stow_the_robot()

        print("Extending arm and lift...")
        node.move_to_pose({
            'joint_arm': 0.5,
            'joint_lift': 1.1
        }, blocking=True)

        print("Moving wrist joints...")
        node.move_to_pose({'joint_wrist_yaw': 1.0}, blocking=True)
        node.move_to_pose({'joint_wrist_pitch': -0.5}, blocking=True)
        node.move_to_pose({'joint_wrist_roll': 1.0}, blocking=True)

        print("Opening gripper...")
        node.move_to_pose({'joint_gripper_finger_left': 0.1}, blocking=True)
        time.sleep(1)

        print("Closing gripper...")
        node.move_to_pose({'joint_gripper_finger_left': 0.0}, blocking=True)

        print("Moving head...")
        node.move_to_pose({
            'joint_head_pan': 1.0,
            'joint_head_tilt': -0.5
        }, blocking=True)

        print("Stowing again...")
        node.stow_the_robot()
        time.sleep(3)

        print("Driving base...")
        node.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
        node.move_to_pose({'rotate_mobile_base': np.pi}, blocking=True)
        node.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)

        node.destroy_node()
        rclpy.shutdown()
        print("Done!")

node = MyNode()
node.main()
