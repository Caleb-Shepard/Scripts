# Scripts
A collection of scripts to automate the boring stuff and bring fun tools to your workstation.

## Getting Started
For the lazy:
```
mkdir -p ~/Scripts && cd
git clone https://github.com/Caleb-Shepard/Scripts
```
if Scripts is a directory, you may need to specify a valid destination for
your clone, and move the scripts into your ~/Scripts directory

### Prerequisites
You should have Python2.7, sh, and a C compiler on your system;
xmodmap is needed for ctrl_alt_esc_swap.xmod
```
sudo apt-get install xmodmap
```

### Installing
```
cd ~/Scripts
cc -o sPoNgEbOb.c sponge
# use the following lines if you like to clean up
rm sPoNgEbOb.c
rm img/ubuntu_beautified.png
rmdir img
```

### Usage
Read the scripts that you plan to run before you run them, as a safe practice.

**sponge**
```
% ./sponge "This is a sassy string"
tHiS iS a SaSsY sTrInG
```

**ubuntu_natural_scrolling_17_04.sh**
```
# This should be run with root privileges
chmod +x ~/Scripts/ubuntu_natural_scrolling_17_04.sh
sudo ~/Scripts/ubuntu_natural_scrolling_17_04.sh
```

**ubuntu_easy_beautification.sh**
```
# Installs custom shell themes and some desktop applications
# This should be run with root privileges
# modify as you wish before running
chmod +x ~/Scripts/ubuntu_easy_beautification.sh
sudo ~/Scripts/ubuntu_easy_beautification.sh
```
After running the script successfully, log into a Gnome3 session and open
```
# this is the command to open gnome-tweak
gnome-tweak-tool
```
enable user shell themes, then restart gnome-tweak (you may use the command again)
```
gnome-tweak-tool
```
Your settings should look like this when you are done
![beautified_gnome3](img/ubuntu_beautified.png?raw=true "Gnome3")

### Authors
    Caleb Shepard

### Acknowledgments
    A special thank you to nana-4 for the flat plat theme included in the beautification script
    Thanks to daniruiz for the Flat-Remix icon theme, which makes the shell theme look cohesive

    Visit the flat remix repository to support daniruiz
    
    [Flat Remix](https://github.com/daniruiz/Flat-Remix)
    [nana-4](https://github.com/nana-4)
    
### Notables
    [Wireless SSID refresher for Gnome Shell](https://extensions.gnome.org/extension/905/refresh-wifi-connections/)

### License
This project is licensed under the GPLv2
