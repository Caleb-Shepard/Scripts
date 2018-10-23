#!/bin/bash
if (( $EUID != 0 )); then
    echo "Are you running as root? Try again."
    exit
fi

read -p "Enter file: " in_file
read -p "Enter destination: " out_file

dc3dd if=$in_file of=$out_file conv=fsync
