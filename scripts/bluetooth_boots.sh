#!/bin/bash
pulseaudio --start
wait
/home/pi/talker-toy/scripts/bluetooth_reconnect.py & > /dev/null 2>&1
sudo python /home/pi/talker-toy/run.py

# Put this file in
# /etc/init.d/talker-toy-bluetooth
# sudo chmod 755 /etc/init.d/talker-toy-bluetooth
# sudo update-rc.d talker-toy-bluetooth defaults