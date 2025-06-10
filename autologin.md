# Autologin

To get your desktop to autologin rather than display the login prompt upon startup you first need to work out which desktop you have:

# Enable Autologin on XFCE4 Startup

1. Edit `/etc/lightdm/lightdm.conf` (create if missing):


`sudo nano /etc/lightdm/lightdm.conf`

Add or modify under `[Seat:*]`:

```
[Seat:*]
autologin-user=<your-username>
autologin-user-timeout=0
```

Save and reboot.