#!/bin/sh
brew install reattach-to-user-namespace --with-wrap-pbcopy-and-pbpaste
echo "set-option -g default-command "reattach-to-user-namespace -l zsh"" >> ~/.tmux.conf

