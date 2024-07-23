### Install a specific version of a package:
```
snap info zoom-client
sudo snap install ubports-installer --channel=latest/edge
```

### Remove old versions of installed snaps:

#### You can list all installed snaps by the following command:
	
	`snap list --all`

#### You can view free disk space by the following command:
	
	`df -ha`

#### The following commands will remove all old versions of installed snaps:
	```
	sudo su
	snap list --all | while read snapname ver rev trk pub notes; do if [[ $notes = *disabled* ]]; then snap remove "$snapname" --revision="$rev"; fi; done
	```

The above script was found [here](https://superuser.com/questions/1310825/how-to-remove-old-version-of-installed-snaps)


