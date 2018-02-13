# Script to install sPoNgEbOb.c
# Written by Tiger Sachse
# Modified by Caleb Shepard 2018.01.18
# sPoNgEbOb.c by Caleb Shepard

# Change this variable to change the name of the folder created during install

gcc -o /usr/local/bin/sponge ../sources/sPoNgEbOb.c
rm install_sponge.sh
rmdir ../installers

# Dorky stuff to print at the end :P
echo
echo
echo \#########################################################
echo Installation Successful! Try this command to get started:
echo \$ sponge \"who lives in a pineapple under the sea?\"
echo
