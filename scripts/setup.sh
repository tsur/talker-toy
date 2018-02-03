#!/bin/bash
sudo apt-get update
sudo apt-get -y install screen git
sudo apt-get -y install python-pip python-dev
sudo apt-get -y install alsa-tools alsa-utils
sudo apt-get -y install espeak python-espeak
sudo apt-get -y install python-requests python-imaging python-imaging-tk
# if running python3
# sudo apt-get -y install python3-rpi.gpio
sudo pip install --upgrade pip
sudo pip install -r requirements.txt
# Remember to configure aws 
# sudo pip install awsscli
# sudo aws configure

