#!/bin/sh
# works on 2012 macbook air and most laptops after clean install
echo "" > /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf

echo "[connection]" >> /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
echo "wifi.powersave=2" >> /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
