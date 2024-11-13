## systemd commands to review and disable background services:

### 1. Currently running

#### 1.1 Gives a list of services which are currently running:

`sudo systemctl --type service --state running`

#### 1.2 stops service from running:

`systemctl stop some-service`

### 2. Currently set to autostart

#### 2.1 list all services that are set to autostart on boot using systemd:

`systemctl list-unit-files --type=service --state=enabled`

#### 2.2 disables it from autostarting:

`sudo systemctl disable some-service`
