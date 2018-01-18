# Script to install sPoNgEbOb.c
# Written by Tiger Sachse
# sPoNgEbOb.c by Caleb Shepard

# Change this variable to change the name of the folder created during install
DOWNLOAD_FOLDER="temp-download-spongebob"

cd
git clone https://github.com/Caleb-Shepard/Scripts.git $DOWNLOAD_FOLDER
cd $DOWNLOAD_FOLDER
gcc sPoNgEbOb.c -o /usr/local/bin/sponge
cd ..
rm -rf $DOWNLOAD_FOLDER

# Dorky stuff to print at the end :P
echo
echo
echo \#########################################################
echo Installation Successful! Try this command to get started:
echo \$ sponge \"who lives in a pineapple under the sea?\"
echo
