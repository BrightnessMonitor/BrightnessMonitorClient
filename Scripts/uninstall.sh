#!/bin/bash

# remove the python package
sudo pip uninstall BrightnessMonitorClient

# remove the service
sudo systemctl disable BrightnessMonitor.service
sudo systemctl daemon-reload
sudo rm /lib/systemd/system/BrightnessMonitor.service

# rm database
sudo rm /var/db/BrightnessMonitor.sqlite

# remove user & group
sudo userdel brightnessmonitor
sudo groupdel brightnessmonitor