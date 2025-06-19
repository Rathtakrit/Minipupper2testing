#!/usr/bin/python
from MangDang.mini_pupper.ESP32Interface import ESP32Interface
import time

# 初始化所有舵机为中立 PWM 值 512
positions = [512] * 12
esp32 = ESP32Interface()

print("  single servo: motor pwm            → example '3 600'")
print("  two servo: motor1 pwm1 motor2 pwm2 → example '3 600 7 580'")
print("enter 'q' to exit program")

while True:
    user_input = input("\nenter > ")

    if user_input.strip().lower() == "q":
        print("exit program")
        break

    try:
        tokens = user_input.strip().split()

        if len(tokens) == 2:
            # single servo mode
            motor = int(tokens[0])
            pwm = int(tokens[1])
            if 1 <= motor <= 12 and 0 <= pwm <= 1023:
                positions[motor - 1] = pwm
                esp32.servos_set_position(positions)
                print(f"✅ set Servo {motor} to PWM = {pwm}")
            else:
                print("❌ motor should be 1~12, PWM should be 0~1023")

        elif len(tokens) == 4:
            # double servo motor mode
            motor1 = int(tokens[0])
            pwm1 = int(tokens[1])
            motor2 = int(tokens[2])
            pwm2 = int(tokens[3])
            if (
                1 <= motor1 <= 12 and 0 <= pwm1 <= 1023 and
                1 <= motor2 <= 12 and 0 <= pwm2 <= 1023
            ):
                positions[motor1 - 1] = pwm1
                positions[motor2 - 1] = pwm2
                esp32.servos_set_position(positions)
                print(f"✅ set Servo {motor1} to PWM = {pwm1}, Servo {motor2} to PWM = {pwm2}")
            else:
                print("❌ motor shoudl be 1~12, PWM should be 0~1023")
        else:
            print("❌ wrong format, enter as '3 600' or '3 600 7 580'")

    except Exception as e:
        print(f"❌ fail to analyze{e}")

    time.sleep(0.05)
