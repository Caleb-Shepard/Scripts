# install a gui to view and modify changes graphically, script should also work on Fedora
# the gui will help with viewing os dependent changes without getting into the weeds
sudo apt install -y dconf-editor

# commands that should work on gnome recognized touchpad and mouse devices
gsettings set org.gnome.desktop.peripherals.mouse natural-scroll true
gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll true
gsettings set org.gnome.settings-daemon.peripherals.mouse natural-scroll true
gsettings set org.gnome.settings-daemon.peripherals.touchpad natural-scroll true
