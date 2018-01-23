#!/bin/bash
# From the guide at https://www.reddit.com/r/EtherMining/wiki/software/apps/linux
# Scripted

# Change the wallet to your address and pick a pool that is right for you
# Your MINER_NAME can be anything that you want it to be
POOL_ADDRESS="us1.ethermine.org:4444"
YOUR_WALLET="0x1E7b423065F423e9a7B21D313540B65abfd09D53"
MINER_NAME=$(hostname)

# Uncomment to install ssh
sudo apt-get update
# sudo apt-get install openssh-server

# Put current user in video group
sudo usermod -a -G video $LOGNAME

# Install AMD drivers
cd ~/Downloads
wget --referer=http://support.amd.com https://www2.ati.com/drivers/linux/ubuntu/amdgpu-pro-17.10-414273.tar.xz
tar -Jxvf amdgpu-pro-17.10-414273.tar.xz
cd amdgpu-pro-17.10-414273
./amdgpu-pro-install -y

# Install Claymore
cd ~/Downloads
wget https://github.com/nanopool/Claymore-Dual-Miner/releases/download/v9.5/Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner.v9.5.-.LINUX.tar.gz
sudo mkdir /usr/local/claymore95
sudo tar -xvf Claymore.s.Dual.Ethereum.Decred_Siacoin_Lbry_Pascal.AMD.NVIDIA.GPU.Miner.v9.5.-.LINUX.tar.gz -C /usr/local/claymore95

# Create mining script
cd /usr/local/claymore95
chmod u+s ethdcrminer64
touch mine.sh

echo "" > mine.sh
echo $(echo -n "#!"; echo "/bin/bash") >> mine.sh
# The next two lines deal with 64BIT option. Choose your preference if you would like.
echo "#Uncomment below according to your preference" >> mine.sh
echo "#export GPU_FORCE_64BIT_PTR=0" >> mine.sh
echo "export GPU_MAX_HEAP_SIZE=100" >> mine.sh
echo "export GPU_USE_SYNC_OBJECTS=1" >> mine.sh
echo "export GPU_MAX_ALLOC_PERCENT=100" >> mine.sh
echo "export GPU_SINGLE_ALLOC_PERCENT=100" >> mine.sh
echo "/usr/local/claymore95/ethdcrminer64 -epool $POOL_ADDRESS -ewal $YOUR_WALLET.$MINER_NAME -epsw x -mode 1 -tt 68 -allpools 1" >> mine.sh

chmod +x mine.sh

# Uncomment to install screen
# apt install screen

# Create launcher

cd ~
touch minestart.sh
echo "" > minestart.sh

echo $(echo -n "#!"; echo "/bin/bash") >> minestart.sh
echo "DEFAULT_DELAY=0" >> minestart.sh
echo "if [ \"x\$1\" = \"x\" -o \"x\$1\" = \"xnone\" ]; then" >> minestart.sh
echo "DELAY=\$DEFAULT_DELAY" >> minestart.sh
echo "else" >> minestart.sh
echo "DELAY=\$1" >> minestart.sh
echo "fi" >> minestart.sh
echo "sleep \$DELAY" >> minestart.sh
echo "cd /usr/local/claymore95" >> minestart.sh
echo "su USERNAME -c \"screen -dmS ethm ./mine.sh\"" >> minestart.sh

chmod +x minestart.sh

# Create job
echo "" > /etc/rc.local
echo "/home/$(whoami)/minestart.sh 15 &" >> /etc/rc.local
echo "exit 0" >> /etc/rc.local

echo "Minestart is a job for $(whoami). This should be root, but if you want it to be another user you may change this."
echo "sudo \$EDITOR /etc/rc.local"
echo "Done. Try running \`/bin/bash /usr/local/claymore95/mine.sh\`"
