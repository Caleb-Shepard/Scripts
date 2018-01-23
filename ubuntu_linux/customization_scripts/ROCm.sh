#!/bin/bash
# run as root
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sh -c 'echo deb [arch=amd64] http://repo.radeon.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
apt-get update
apt-get install rocm-*

echo "" > /etc/default/grub
echo "GRUB_DEFAULT=0" >> /etc/default/grub
echo "GRUB_HIDDEN_TIMEOUT=0" >> /etc/default/grub
echo "GRUB_HIDDEN_TIMEOUT_QUIET=true" >> /etc/default/grub
echo "GRUB_TIMEOUT=10" >> /etc/default/grub
echo "GRUB_DISTRIBUTOR=\`lsb_release -i -s 2> /dev/null || echo Debian\`" >> /etc/default/grub
echo "GRUB_CMDLINE_LINUX_DEFAULT=\"quiet splash\"" >> /etc/default/grub
echo "GRUB_CMDLINE_LINUX=\"amdgpu.vm_fragment_size=9\"" >> /etc/default/grub

update-grub 
reboot
