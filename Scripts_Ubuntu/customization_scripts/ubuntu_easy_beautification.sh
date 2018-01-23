echo "You should install needed drivers before running this script."
echo "This script installs nonfree software. Read before you run."
sleep 1
echo "You may need to install processor microcode. Sleeping execution for 5 seconds ... "
sleep 5

# update package list first and install updates
apt-get -y update
apt-get -y dist-upgrade

# install programs from apt
apt-get install -y vim git zsh tmux fortune lolcat cowsay curl nmap nitrogen autorenamer docky aweather
apt-get install -y away
# install open java development kit from apt
apt-get install -y default-jdk
# install eclipse and cdt
apt-get install -y eclipse eclipse-*
# install evolution with owa support for university email
apt-get install -y evolution
apt-get install -y evolution-ews

# set default shell to zsh
chsh -s /bin/zsh

# download config files
mkdir -p ~/git
cd ~/git && git clone https://github.com/Caleb-Shepard/dotfiles
cp ~/git/dotfiles/configs/.bashrc ~/.bashrc
cp ~/git/dotfiles/configs/.vimrc ~/.vimrc
cp ~/git/dotfiles/configs/.tmux.conf ~/.tmux.conf
# clean up
rm -rf ~/git/Dotfiles/

# install gnome and gnome related programs
apt-get install -y ubuntu-gnome-desktop gparted gnome-tweak-tool

# install Flat-Plat theme for gnome
cd /tmp
curl -sL https://github.com/nana-4/Flat-Plat/archive/v20170515.tar.gz | tar xz
cd materia-theme-20170515 && ./install.sh

# install Flat Remix icon theme for gnome
cd /tmp
git clone https://github.com/daniruiz/Flat-Remix
mkdir -p ~/.icons
mv "Flat-Remix/Flat Remix" ~/.icons

# install powerline fonts
cd ~/git
git clone https://github.com/powerline/fonts.git
cd fonts
./install.sh
# clean up
cd ..
rm -rf fonts

# uncomment the following lines to add nvidia repo
# apt-get update
# apt-get install nvidia-*

# install chromium
apt-get install -y chromium-browser

# install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" && cp ~/git/Dotfiles/.zshrc ~/.zshrc

# remaps
apt-get install -y x11-xkb-utils
# set caps to control in shell profiles
echo setxkbmap -option ctrl:nocaps >> ~/.zshrc
echo setxkbmap -option ctrl:nocaps >> ~/.bashrc
