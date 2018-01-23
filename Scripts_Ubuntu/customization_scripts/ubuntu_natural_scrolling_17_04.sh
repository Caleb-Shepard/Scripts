# /bin/sh
# run as root
# allows for natural scrolling in 17.04

# remove libinput
apt remove xserver-xorg-input-libinput

touch /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf
echo 'Section "InputClass"' >> /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf
echo '    Identifier "Natural Scrolling Mouses"' >> /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf
echo '    MatchIsPointer "on"' >> /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf
echo '    MatchIsTouchpad "off"' >> /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf
echo '    MatchDevicePath "/dev/input/event*"' >> /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf
echo '    Option "VertScrollDelta" "-1"' >> /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf
echo '    Option "HorizScrollDelta" "-1"' >> /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf
echo '    Option "DialDelta" "-1"' >> /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf
echo 'EndSection' >> /usr/share/X11/xorg.conf.d/20-natural-scrolling-mouses.conf

reboot
