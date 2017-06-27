#!/bin/bash

# remove the service
sudo systemctl disable BrightnessMonitor.service
sudo rm /lib/systemd/system/BrightnessMonitor.service
sudo systemctl daemon-reload

# add service
sudo wget https://raw.githubusercontent.com/BrightnessMonitor/BrightnessMonitorClient/master/Scripts/BrightnessMonitor.service -O /lib/systemd/system/BrightnessMonitor.service
sudo chmod 644 /lib/systemd/system/BrightnessMonitor.service
sudo systemctl daemon-reload
sudo systemctl enable BrightnessMonitor.service
sudo systemctl start BrightnessMonitor.service

# update from the git repo
sudo pip install git+git://github.com/BrightnessMonitor/BrightnessMonitorClient.git --upgrade --force
