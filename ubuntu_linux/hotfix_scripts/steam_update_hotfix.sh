# steam update hotfix
mv ~/.steam/steam/* ~/.local/share/Steam/
rm -rf ~/.steam/steam
ln -s ../.local/share/Steam ~/.steam/steam
rm -rf ~/.steam/bin
