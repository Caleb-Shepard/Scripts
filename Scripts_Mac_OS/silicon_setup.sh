#!/bin/bash

# installs rosetta2, arm homebrew (brew), 64-bit homebrew (brew64)
# installs homebrew packages
# turns on strict firewall

# turn on strict firewall
sudo defaults write /Library/Preferences/com.apple.alf globalstate -int 2    

# install rosetta2
/usr/sbin/softwareupdate --install-rosetta --agree-to-license

# install 64-bit homebrew
arch --x86_64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# install arm homebrew
cd ~/Downloads
mkdir homebrew
curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
sudo mv homebrew /opt/homebrew

# add a function to launch brew in 64 bit, add homebrew to path
ZSH_POSTSCRIPT=$(cat <<EOF
function brew64() {
   arch --x86_64 /usr/local/bin/brew $@
}

if [ -d "/opt/homebrew/bin" ]; then
    export PATH="/opt/homebrew/bin:\$PATH”
fi
EOF
) 

# push changes to the .zshrc and refresh profile
echo $ZSH_POSTSCRIPT >> ~/.zshrc
source ~/.zshrc
