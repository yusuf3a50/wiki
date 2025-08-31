# Snap

### Install snap:
To install Snap in Linux Mint, first remove or rename the file named `nosnap.pref` located in `/etc/apt/preferences.d/`. Then, update your package list and install Snap by running `sudo apt install snapd` in the terminal

``` bash
sudo snap refresh
sudo snap install hello-world
```

### List installed snaps:

`snap list`

### Install a specific version of a package:
``` bash
snap info zoom-client
sudo snap install ubports-installer --channel=latest/edge
```

### Remove old versions of installed snaps:

#### You can list all installed snaps by the following command:
	
``` bash
snap list --all
```

#### You can view free disk space by the following command:
	
``` bash
df -ha
```

#### The following commands will remove all old versions of installed snaps:
``` bash
sudo su
snap list --all | while read snapname ver rev trk pub notes; do if [[ $notes = *disabled* ]]; then snap remove "$snapname" --revision="$rev"; fi; done
```

The above script was found [here](https://superuser.com/questions/1310825/how-to-remove-old-version-of-installed-snaps)