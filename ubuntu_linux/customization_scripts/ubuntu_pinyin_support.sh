#!/bin/bash
# add pinyin support for Chinese keyboard in Ubuntu
# https://askubuntu.com/questions/59356/how-do-i-get-chinese-input-to-work

SCHEMA="org.gnome.desktop.input-sources"
KEY="sources"

apt-get install ibus-libpinyin
apt-get install ibus-pinyin
apt-get install ibus-sunpinyin

ibus restart

gsettings set org.gnome.desktop.input-sources sources "$(gsettings get org.gnome.desktop.input-sources sources | sed "s/]/, ('ibus', 'libpinyin')]/")" 

