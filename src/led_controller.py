#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 500000, timeout=1) 

def callback(msg):
    print(f"Sending: {msg} to Arduino.")
    data = msg.data + "\n" 
    ser.write(data.encode())  
    time.sleep(0.01)
    ser.flush()

def main():
    rospy.init_node('led_driver_node')

    rospy.Subscriber('/led_pwm', String, callback)

    rospy.spin()

if __name__ == "__main__":
    main()

