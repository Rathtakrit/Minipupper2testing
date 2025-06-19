import time
from MangDang.mini_pupper.HardwareInterface import HardwareInterface
from MangDang.mini_pupper.Config import Configuration

def main():

    # Create config
    config = Configuration()
    hardware_interface = HardwareInterface()
   
    # Example: Move servo 0 to a specific position (e.g., 0.5 radians)
    joint_angles = [0.0] * 12  # 12 servos, all at 0.0
    joint_angles[0] = 0.5      # Move the first servo

    # Send the position to the hardware
    hardware_interface.set_actuator_postions(joint_angles)
    print("Moved servo 0 to 0.5 radians.")

    # Hold position for a few seconds
    time.sleep(2)

    # Return servo to neutral
    joint_angles[0] = 0.0
    hardware_interface.set_actuator_postions(joint_angles)
    print("Returned servo 0 to 0.0 radians.")

if __name__ == "__main__":
    main()

