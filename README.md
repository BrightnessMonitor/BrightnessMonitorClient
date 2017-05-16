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

## Usage

### CLI
```bash
brightnessmonitorclient
```

### add as a Cronjob

Open crontab

```bash
crontab -e
```

And add for execute every 15 minutes:

```bash
*/15 * * * * python /usr/local/lib/python2.7/dist-packages/brightnessmonitorclient
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