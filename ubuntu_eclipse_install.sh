# this is an easy install of eclipse neon for Ubuntu
# you should update packages before running this if you are running it as a standalone script

# housekeeping
apt-get update
apt-get install default-jdk wget
mkdir -p ~/Downloads

# download package
cd ~/Downloads && wget https://www.eclipse.org/downloads/download.php?file=/oomph/epp/neon/R3/eclipse-inst-linux64.tar.gz&mirror_id=492

# move package
mv ~/Downloads/eclipse-standard-kepler-SR2-linux-gtk-x86_64.tar.gz /opt/eclipse-standard-kepler-SR2-linux-gtk-x86_64.tar.gz

# checksum; continues anyway if bad sum
cd /opt && sha512sum -c "b2bde9d9485696f7a86ff7b1effa7022ccf517c6f81ea1df937fe464338a98af43898125e78f2110a7a9592a67ce8b99a38c27b1ae214ef6b636f9a968269ff3  eclipse-inst-linux64.tar.gz"

# extract package
tar -xvf eclipse-standard-kepler-SR2-linux-gtk-x86_64.tar.gz

# make and install desktop file
cd /usr/share/applications
touch eclipse.desktop
echo [Desktop Entry] >> eclipse.desktop
echo Name=Eclipse >> eclipse.desktop
echo Type=Application >> eclipse.desktop
echo Exec=/opt/eclipse/eclipse >> eclipse.desktop
echo Terminal=false >> eclipse.desktop
echo Icon=/opt/eclipse/icon.xpm >> eclipse.desktop
echo Comment=Integrated Development Environment >> eclipse.desktop
echo NoDisplay=false >> eclipse.desktop
echo Categories=Development;IDE; >> eclipse.desktop
echo Name[en]=eclipse.desktop >> eclipse.desktop
desktop-file-install eclipse.desktop

# make a symlink
ln -s /opt/eclipse/eclipse /usr/local/bin
