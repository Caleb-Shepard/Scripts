#!/bin/bash
# with default os settings, run as root
touch /etc/NetworkManager/conf.d/mac_anchor.conf
echo "[device]" >> /etc/NetworkManager/conf.d/mac_anchor.conf
echo "wifi.scan-rand-mac-address=no" >> /etc/NetworkManager/conf.d/mac_anchor.conf
service network-manager restart
