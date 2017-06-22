# BrightnessMonitorClient

## Install

### via install script

```bash
bash <(wget -qO- https://raw.githubusercontent.com/BrightnessMonitor/BrightnessMonitorClient/master/Scripts/install.sh)
```

### via Git

```bash
sudo pip install git+git://github.com/BrightnessMonitor/BrightnessMonitorClient.git
```

### Download and install localy

```bash
git clone git@github.com:BrightnessMonitor/BrightnessMonitorClient.git
pip install BrightnessMonitorClient --upgrade
```

## update

### via install script

```bash
bash <(wget -qO- https://raw.githubusercontent.com/BrightnessMonitor/BrightnessMonitorClient/master/Scripts/update.sh)
```

### via Git

```bash
sudo pip install git+git://github.com/BrightnessMonitor/BrightnessMonitorClient.git --upgrade --force
```

## Uninstall

```bash
bash <(wget -qO- https://raw.githubusercontent.com/BrightnessMonitor/BrightnessMonitorClient/master/Scripts/uninstall.sh)
```

## Usage

### CLI
```bash
sudo brightnessmonitorclient
```

## Config

To edit:

```bash
sudo nano /etc/brightnessmonitorclient.conf
```

Example:

```bash
[Login]
host = localhost
protocol = https
token = YourUserToken
uuid = DeviceUUID
```
