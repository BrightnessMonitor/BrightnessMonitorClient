#!/bin/bash

# remove the python package
sudo pip uninstall BrightnessMonitorClient

# remove the service

echo "Waiting for service to stop"
sudo systemctl stop BrightnessMonitor.service
sudo systemctl disable BrightnessMonitor.service
sudo rm /lib/systemd/system/BrightnessMonitor.service
sudo systemctl daemon-reload

# rm database
sudo rm /var/db/BrightnessMonitor.sqlite

# remove user & group
sudo userdel brightnes
sudo groupdel brightnes
