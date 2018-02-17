#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
sudo apt-get -y install screen git
sudo apt-get -y install python-pip python-dev
sudo apt-get -y install python-requests
sudo apt-get -y install pulseaudio pulseaudio-module-bluetooth
# if running python3
# sudo apt-get -y install python3-rpi.gpio
sudo pip install --upgrade pip
sudo pip install -r requirements.txt
# Remember to configure aws 
sudo pip install awscli
sudo aws configure

##### IF WANT TO USE BLUETOOTH: (1)
# follow guide at http://youness.net/raspberry-pi/bluetooth-headset-raspberry-pi