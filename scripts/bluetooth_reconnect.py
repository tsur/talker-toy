#!/usr/bin/python

# Monitor removal of bluetooth reciever
import os
import sys
import subprocess
import time

# def blue_it():
#     status = subprocess.call('ls /dev/input/event0 > /dev/null 2>&1', shell=True)
#     while status == 0:
#         # print("Bluetooth UP")
#         # print(status)
        
#         time.sleep(15)
#         status = subprocess.call('ls /dev/input/event0 > /dev/null 2>&1', shell=True)
#     else:
#         waiting()

# def waiting():
#     subprocess.call('pulseaudio --kill', shell=True)
#     time.sleep(3)
#     subprocess.call('pulseaudio --start', shell=True)
#     time.sleep(2)
#     status = subprocess.call('ls /dev/input/event0 > /dev/null 2>&1', shell=True)  
#     while status == 2:
#         # print("Bluetooth DOWN")
#         # print(status)
#         subprocess.call('/home/pi/talker-toy/scripts/bluetooth_autopair.sh', shell=True)
#         time.sleep(15)
#         status = subprocess.call('ls /dev/input/event0 > /dev/null 2>&1', shell=True)
#     else:
#         blue_it() 

def blue_it():
    while True:
        time.sleep(15)
        subprocess.call('/home/pi/talker-toy/scripts/bluetooth_autopair.sh', shell=True)

blue_it()