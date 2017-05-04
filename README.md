# BrightnessMonitorClient

## Install

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