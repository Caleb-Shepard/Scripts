#!/bin/bash
# with default os settings, run as root
touch test.txt
echo "[device]" >> /etc/NetworkManager/NetworkManager.conf
echo "wifi.scan-rand-mac-address=no" >> /etc/NetworkManager/NetworkManager.conf
service network-manager restart
