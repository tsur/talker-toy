#!/bin/bash
# bluetoothctl << EOF
# connect 54:E2:56:8B:EB:1A
# EOF
#connect <bt_device_mac_address>
#using aqua bluetooth speaker mac address, el altavoz rojo redondo
echo "Default sink"
pacmd set-default-sink bluez_sink.54_E2_56_8B_EB_1A.a2dp_sink