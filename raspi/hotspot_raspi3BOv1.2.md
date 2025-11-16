# Raspberry Pi 3B v1.2 Hotspot Setup

For Raspberry Pi 3 B v1.2 running **Debian 13 (Trixie)**, setting up a hotspot requires the old manual method due to a WiFi driver encryption bug.

## Known Issue
NetworkManager/nmcli has a bug which means WPA encryption does not work on this hardware. Open WiFi (no encryption) does work with nmcli, but for security reasons we use the manual hostapd method instead.

## Prerequisites

You need three services:
1. **hostapd** - creates the access point
2. **dnsmasq** - provides DHCP and DNS
3. **rc.local workaround** - assigns static IP at boot (dhcpcd doesn't work properly on Trixie)


Therefore, you need to follow the old method of implementing a hotspot, using the following three services:
1. hostapf
2. dnsmasq
3. dhcpcd ?? maybe? - it doesnt seem to work so we have to implement a workaround for it

### 1. These will need to installed, unmasked, enabled and configured(!) 

``` bash 
sudo apt-get -y install hostapd dnsmasq
sudo systemctl enable --now hostapd dnsmasq
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
```

### 2. Edit /etc/dhcpcd.conf by scrolling to the bottom and adding:
``` bash
denyinterfaces wlan0

interface wlan0
    static ip_address=192.168.5.1/24
    nohook wpa_supplicant
```

### 3. On modern Raspbian/Raspberry Pi OS, the interfaces file is deprecated and often ignored. The system uses dhcpcd to manage network interfaces instead.
Edit `/etc/network/interfaces` and either delete the wlan0 section or comment it out with #.

You will need to unblock wifi(!)
sudo rfkill unblock wifi

### 4. Configure hostapd
We need to set up hostapd to tell it to broadcast a particular SSID and allow WiFi connections on a certain channel. Edit the likely non-existent file `/etc/hostapd/hostapd.conf`:
``` bash
interface=wlan0
driver=nl80211
ssid=MyPiAP
hw_mode=g
channel=6
ieee80211n=1
wmm_enabled=1
ht_capab=[HT40][SHORT-GI-20][DSSS_CCK-40]
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_passphrase=raspberry
rsn_pairwise=CCMP
```

5. 
Unfortunately, hostapd does not know where to find this configuration file, so we need to provide its location to the hostapd startup script. Open /etc/default/hostapd and add the following:
``` bash
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

### 6. Configure dnsmasq
Dnsmasq will help us automatically assign IP addresses as new devices connect to our network as well as work as a translation between network names and IP addresses. The .conf file that comes with Dnsmasq has a lot of good information in it, so it might be worthwhile to save it (as a backup) rather than delete it. After saving it, open a new one for editing:
``` bash
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.bak
sudo nano /etc/dnsmasq.conf
```

``` bash
interface=wlan0 
listen-address=192.168.5.1
bind-interfaces 
server=8.8.8.8
domain-needed
bogus-priv
dhcp-range=192.168.5.2,192.168.5.20,255.255.255.0,24h
```

### 7. You should disable network manager
sudo systemctl stop NetworkManager 2>/dev/null || null
sudo systemctl disable NetworkManager 2>/dev/null || null


/etc/rc.local:

``` bash
#!/bin/sh -e
#
# rc.local
#

# Wait for system to be ready
sleep 5

# Assign static IP to wlan0
ip addr add 192.168.5.1/24 dev wlan0 || true

# Restart dnsmasq to bind to the IP
systemctl restart dnsmasq

exit 0
```
Then you need to make the file executable: `sudo chmod +x /etc/rc.local`

