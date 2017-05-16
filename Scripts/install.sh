#!/bin/bash

# Install programm
sudo pip install git+git://github.com/BrightnessMonitor/BrightnessMonitorClient.git

# create user
sudo adduser --system --no-create-home --group brightnessmonitor

# create config file
read -p "Enter host [localhost]: " host
host=${host:-localhost}
read -p "Enter protocol [https]: " protocol
protocol=${host:-https}
read -p "Enter token [YourUserToken]: " token
token=${host:-YourUserToken}
read -p "Enter uuid [DeviceUUID]: " uuid
uuid=${uuid:-DeviceUUID}

sudo sh -c "echo '[Login]' >> /etc/brightnessmonitorclient.conf"
sudo sh -c "echo 'host = $hostname' > /etc/brightnessmonitorclient.conf"
sudo sh -c "echo 'protocol = $protocol' > /etc/brightnessmonitorclient.conf"
sudo sh -c "echo 'token = $token' > /etc/brightnessmonitorclient.conf"
sudo sh -c "echo 'uuid = $uuid' > /etc/brightnessmonitorclient.conf"

# touch database & set write permission
sudo mkdir /var/db/
sudo touch /var/db/BrightnessMonitor.sqlite
chown brightnessmonitor:brightnessmonitor /var/db/BrightnessMonitor.sqlite

# add service
sudo wget https://raw.githubusercontent.com/BrightnessMonitor/BrightnessMonitorClient/master/Scripts/BrightnessMonitor.service -O /lib/systemd/system/BrightnessMonitor.service
sudo chmod 644 /lib/systemd/system/BrightnessMonitor.service
sudo systemctl daemon-reload
sudo systemctl enable BrightnessMonitor.service
sudo systemctl start BrightnessMonitor.service