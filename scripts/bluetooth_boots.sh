#!/bin/bash
pulseaudio --start
wait
/home/pi/talker-toy/scripts/bluetooth_reconnect.py & > /dev/null 2>&1
python /home/pi/talker-toy/run.py & > /dev/null 2>&1

# Put this file in
# /etc/init.d/talker-toy-bluetooth
# sudo chmod 755 /etc/init.d/talker-toy-bluetooth
# sudo update-rc.d talker-toy-bluetooth defaults