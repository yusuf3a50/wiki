# Virtualbox

## 1. Installation:
To have a virtualbox installation that supports x86_64/64 bit VMs, install virtualbox from the oracle repositories:

``` bash
wget -qO- https://www.virtualbox.org/download/oracle_vbox_2016.asc | sudo gpg --dearmor -o /etc/apt/keyrings/oracle-virtualbox.gpg
echo "deb [signed-by=/etc/apt/keyrings/oracle-virtualbox.gpg] http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
sudo apt update

sudo apt update
sudo apt install virtualbox7.1
```

Install whichever version of virtualbox you require but dont install package named `virtualbox` because this is the ubuntu/debian repo version of the package and it doesnt support 64bit VMs.

## 2. Setup
Select: 'New'

#### Ensure HVM is selected:
Settings > Expert (tab) > System > Acceleration > Hardware virtualization: Enabled


## Debian setup:

### WARNING: 
**NetInstall + virtualbox combination is very difficult to make work!**
- do not install from netinst. Install from exisiting desktop iso such as the LXDE desktop version

### VBox guest additions
Install VirtualBox Guest Additions (for better screen resolution and clipboard sharing):

    In VirtualBox, go to Devices > Insert Guest Additions CD image.
    Mount the CD in the VM:
    bash

sudo mount /dev/cdrom /mnt
Install dependencies and Guest Additions:
bash
sudo apt-get install build-essential dkms linux-headers-$(uname -r)
sudo sh /mnt/VBox_GAs_*/VBoxLinuxAdditions.run

### resize root fs

### LXDE desktop setup

sudo apt install lxde-core lightdm --no-install-recommends