#!/bin/bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
sudo apt-get -y install screen git
sudo apt-get -y install python-pip python-dev
sudo apt-get -y install alsa-tools alsa-utils portaudio19-dev
sudo apt-get -y install python-requests

amixer cset numid=3 1 # force headphone (PWM) output

sudo pip install --upgrade pip
sudo pip install -r requirements.txt

# Remember to configure aws 
sudo pip install awscli
sudo aws configure
