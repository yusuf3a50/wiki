Some commands to review and disable background services from autostarting and running in the background.

1. gives a proper list of services which are currently running:

`sudo systemctl --type service --state running`

2. stops service from running:

`systemctl stop some-service`

3. disables it from autostarting:

`systemctl disable some-service`
