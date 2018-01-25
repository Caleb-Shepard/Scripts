# Script to install ohce.c

gcc -o /usr/local/bin/ohce .../sources/ohce.c
rm install_ohce.sh
rmdir ../installers

# Dorky stuff to print at the end :P
echo
echo
echo \#########################################################
echo Installation Successful! Try this command to get started:
echo \$ ohce \"?aes eht rednu elppaenip a ni sevil ohw\"
echo
