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
        
        time.sleep(1)
        
        print("Stowing robot...")
        self.stow_the_robot()
        time.sleep(1)

        print("Extending arm and lift...")
        self.move_to_pose({
            'joint_arm': 0.5,
            'joint_lift': 1.1
        }, blocking=True)

        print("Moving wrist joints...")
        self.move_to_pose({'joint_wrist_yaw': 1.0}, blocking=True)
        self.move_to_pose({'joint_wrist_pitch': -0.5}, blocking=True)
        self.move_to_pose({'joint_wrist_roll': 1.0}, blocking=True)

        print("Opening gripper...")
        self.move_to_pose({'joint_gripper_finger_left': 0.1}, blocking=True)
        time.sleep(1)

        print("Closing gripper...")
        self.move_to_pose({'joint_gripper_finger_left': 0.0}, blocking=True)
        time.sleep(1)

        print("Moving head...")
        self.move_to_pose({
            'joint_head_pan': 1.0,
            'joint_head_tilt': -0.5
        }, blocking=True)

        print("Stowing again...")
        self.stow_the_robot()
        time.sleep(2)

        print("Driving base...")
        self.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
        time.sleep(0.5)

        self.move_to_pose({'rotate_mobile_base': np.pi}, blocking=True)
        time.sleep(0.5)
        
        self.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
        time.sleep(1)

        print("Done!")
        self.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    node = MyNode()
    node.main()