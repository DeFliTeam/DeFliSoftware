#!/bin/bash

sudo apt update && sudo apt upgrade -y

aptDepends=( 
               python3-pip 
               wget
               netcat
           )

pipDepends=(
               PyQt5
               requests
           )
sudo apt install -y "${aptDepends[@]}" && sudo pip3 install -y "${pipDepends[@]}"
sudo bash -c "$(wget -O - https://github.com/wiedehopf/adsb-scripts/raw/master/readsb-install.sh)"
sudo bash -c "$(curl -L -o - https://github.com/wiedehopf/adsb-scripts/raw/master/autogain-install.sh)"  hash -r
sudo bash -c "$(curl -L -o - https://github.com/wiedehopf/graphs1090/raw/master/install.sh)"

sudo cp "$HOME"/Defli_Installer/FirstSetup/defli_gui.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable defli_gui.service
sudo systemctl start defli_gui.service

sudo reboot