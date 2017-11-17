# Script to install sPoNgEbOb.c
# Written by Tiger Sachse
# sPoNgEbOb.c by Caleb Shepard

# Change this variable to change the name of the folder created during install
DOWNLOAD_FOLDER="temp-download-spongebob"

git clone https://github.com/Caleb-Shepard/Scripts.git $DOWNLOAD_FOLDER
cd $DOWNLOAD_FOLDER
sudo gcc sPoNgEbOb.c -o sponge
mv sponge /usr/bin/sponge
cd ..
sudo rm -r $DOWNLOAD_FOLDER

# Dorky stuff to print at the end :P
echo
echo
echo \#########################################################
echo Installation Successful! Try this command to get started:
echo \$ sponge \"who lives in a pineapple under the sea?\"
echo
