#!/bin/bash
sudo apt-get update
sudo apt-get -y install screen git
sudo apt-get -y install python-pip python-dev
sudo apt-get -y install alsa-tools alsa-utils portaudio19-dev pulseaudio
sudo apt-get -y install espeak python-espeak
sudo apt-get -y install python-requests python-imaging python-imaging-tk
# if running python3
# sudo apt-get -y install python3-rpi.gpio
sudo pip install --upgrade pip
sudo pip install -r requirements.txt
# Remember to configure aws 
sudo pip install awscli
sudo aws configure

##### IF WANT TO USE MINI JACK:
# amixer cset numid=3 1 # force headphone (PWM) output

##### IF WANT TO USE BLUETOOTH: (1)
# follow guide at https://raspberrypi.stackexchange.com/questions/53408/automatically-connect-trusted-bluetooth-speaker
# echo 'pulseaudio --start' >> ~/.bashrc
# echo 'wait' >> ~/.bashrc
# echo '/home/py/talker-toy/scripts/bluetooth_reconnect.py' >> ~/.bashrc

##### IF WANT TO USE BLUETOOTH: (2)
# ./talker-toy/scripts/setup_bluetooth.sh