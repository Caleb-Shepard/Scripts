# Script to install aesthetic.c

gcc -o /usr/local/bin/aesthetic ../sources/aesthetic.c
rm install_aesthetic.sh
rmdir ../installers

# Dorky stuff to print at the end :P
echo
echo
echo \#########################################################
echo Installation Successful! Try this command to get started:
echo \$ asethetic \"aesthetic\"
echo
