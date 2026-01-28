import time
import numpy as np
import stretch_body.robot

robot = stretch_body.robot.Robot()
robot.startup()

# Move the arm and gripper back to its stow position
robot.stow()
robot.wait_command()
# Extend the arm and lift all the way out at the same time 
robot.arm.move_to(0.5)
robot.lift.move_to(1.1)

robot.push_command()
robot.wait_command()

# Move the wrist joints
robot.end_of_arm.move_to('wrist_yaw', np.radians(10))
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_pitch', np.radians(10))
robot.push_command()
robot.wait_command()

robot.end_of_arm.move_to('wrist_roll', np.radians(60))
robot.push_command()
robot.wait_command()

# Open the gripper and close it
robot.end_of_arm.move_to('stretch_gripper', 50)
robot.push_command()
robot.wait_command()
robot.end_of_arm.move_to('stretch_gripper', -20)
robot.push_command()
robot.wait_command()

# Rotate RealSense Camera
robot.head.move_by('head_pan', np.radians(45))
robot.head.move_by('head_tilt', np.radians(45))
robot.push_command()
robot.wait_command()

robot.stow()
robot.wait_command()

# Move the robot
robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()
robot.base.rotate_by(np.deg2rad(180))
robot.push_command()
robot.wait_command()
robot.base.translate_by(0.5)
robot.push_command()
robot.wait_command()

robot.stop()