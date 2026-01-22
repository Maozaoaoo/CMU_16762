import time
import numpy as np
import stretch_body.robot

robot = stretch_body.robot.Robot()
robot.startup()

# Move the arm and gripper back to its stow position
robot.stow()
time.sleep(2)

# Extend the arm and lift all the way out at the same time 
arm_max = robot.arm.status['max']
lift_max = robot.lift.status['max']

robot.arm.move_to(arm_max)
robot.lift.move_to(lift_max)

robot.push_command()
time.sleep(2)

# Move the wrist joints
robot.end_of_arm.move_to('wrist_yaw', np.radians(30))
robot.push_command()
time.sleep(2)

robot.end_of_arm.move_to('wrist_pitch', np.radians(30))
robot.push_command()
time.sleep(2)

robot.end_of_arm.move_to('wrist_roll', np.radians(30))
robot.push_command()
time.sleep(2)

# Open the gripper and close it
robot.end_of_arm.move_to('stretch_gripper', 50)
robot.end_of_arm.move_to('stretch_gripper', -20)
robot.push_command()
time.sleep(2)

# robot.end_of_arm.move_to('stretch_gripper', -20)
# robot.push_command()
# time.sleep(2)

# Rotate RealSense Camera
robot.head.move_by('head_pan', np.radians(45))
robot.head.move_by('head_tilt', np.radians(45))
robot.push_command()
time.sleep(2)

robot.stow()
time.sleep(2)

# Move the robot
robot.base.translate_by(0.5)
robot.base.rotate_by(np.deg2rad(180))
robot.base.translate_by(0.5)
robot.push_command()
time.sleep(5)

robot.stop()