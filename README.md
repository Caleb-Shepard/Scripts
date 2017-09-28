# Scripts
A collection of scripts to automate the boring stuff and bring fun tools to your workstation.

## Getting Started
For the lazy:
```
mkdir -p ~/Scripts && cd
git clone https://github.com/Caleb-Shepard/Scripts
```

### Prerequisites
You should have Python3, sh, and a C compiler on your system
xmodmap is needed for ctrl_alt_esc_swap.xmod
```
sudo apt-get install xmodmap
```

### Installing
```
cd ~/Scripts
cc -o sPoNgEbOb.c sponge
#rm sPoNgEbOb.c
```

### Usage
Read the scripts that you plan to run before you run them, as a safe practice.

**sponge**
This is a simple C program that converts strings into sassy spongebob talk.
```
./sponge "This is a string"
```

**ubuntu_natural_scrolling_17_04.sh**
```
# This should be run with root privileges
sudo ubuntu_natural_scrolling_17_04.sh
```

**ubuntu_easy_beautification.sh**
```
# This will run the script as root. Read the script before trying this!
chmod +x ~/Scripts/ubuntu_easy_beautification.sh
sudo ~/Scripts/ubuntu_easy_beautification.sh
```
After running the script successfully, log into a gnome session and open
```
# this is the command to open gnome-tweak
gnome-tweak-tool
```
enable user shell themes, then restart gnome-tweak (you may use the command again)
```
gnome-tweak-tool
```
Your settings should look like this when you are done
![beautified_gnome3](/relative/path/to/img.jpg?raw=true "Gnome")

### Authors
    Caleb Shepard

### Acknowledgments
    A special thank you to nana-4 for the flat plat theme included in the beautification script
    Thanks to daniruiz for the Flat-Remix icon theme, which makes the shell theme look cohesive

    See https://github.com/daniruiz/Flat-Remix to support daniruiz

### License
This project is licensed under the GPLv2
