# Raspberry Pi 3B v1.2 Hotspot Setup

For Raspberry Pi 3 B v1.2 running **Debian 13 (Trixie)**, setting up a hotspot requires the old manual method due to a WiFi driver encryption bug.

## Known Issue
NetworkManager/nmcli has a bug which means WPA encryption does not work on this hardware. Open WiFi (no encryption) does work with nmcli, but for security reasons we use the manual hostapd method instead.

## Prerequisites

You need three services:
1. **hostapd** - creates the access point
2. **dnsmasq** - provides DHCP and DNS
3. **rc.local workaround** - assigns static IP at boot (dhcpcd doesn't work properly on Trixie)

---

## Installation Steps

### 1. Install and Enable Services

```bash 
sudo apt-get -y install hostapd dnsmasq
sudo systemctl unmask hostapd
sudo systemctl enable hostapd dnsmasq
```

**Unblock WiFi:**
```bash
sudo rfkill unblock wifi
```

### 2. Disable NetworkManager (Important!)

NetworkManager will interfere with hostapd:

```bash
sudo systemctl stop NetworkManager
sudo systemctl disable NetworkManager
```

### 3. Configure dhcpcd (This Won't Work But Is Good Practice)

Edit `/etc/dhcpcd.conf` and add at the bottom:

```bash
denyinterfaces wlan0

interface wlan0
    static ip_address=192.168.5.1/24
    nohook wpa_supplicant
```

**Note:** On Trixie, this configuration is often ignored, which is why we need the rc.local workaround below.

### 4. Configure hostapd

Create `/etc/hostapd/hostapd.conf`:

```bash
sudo nano /etc/hostapd/hostapd.conf
```

Add:

```bash
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

**Security Note:** Change `ssid` and `wpa_passphrase` to your own values!

### 5. Point hostapd to Configuration File

Edit `/etc/default/hostapd`:

```bash
sudo nano /etc/default/hostapd
```

Add or uncomment:

```bash
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

### 6. Configure dnsmasq

Backup the original config and create a new one:

```bash
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.bak
sudo nano /etc/dnsmasq.conf
```

To `/etc/dnsmasq.conf` add:

```bash
interface=wlan0 
listen-address=192.168.5.1
bind-interfaces 
server=8.8.8.8
domain-needed
bogus-priv
dhcp-range=192.168.5.2,192.168.5.20,255.255.255.0,24h
```

### 7. Create rc.local Workaround (Critical!)

Since dhcpcd doesn't properly assign the static IP on Trixie, we use rc.local:

```bash
sudo nano /etc/rc.local
```

Add:

```bash
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

Make it executable:

```bash
sudo chmod +x /etc/rc.local
```

### 8. Optional: Create systemd Wait Override for dnsmasq

This ensures dnsmasq waits for network to be ready:

```bash
sudo mkdir -p /etc/systemd/system/dnsmasq.service.d
sudo nano /etc/systemd/system/dnsmasq.service.d/wait.conf
```

Add:

```bash
[Unit]
After=network-online.target
Wants=network-online.target
```

Reload systemd:

```bash
sudo systemctl daemon-reload
```

### 9. Reboot and Test

```bash
sudo reboot
```

After reboot, verify:

```bash
ip addr show wlan0                    # Should show 192.168.5.1/24
sudo systemctl status hostapd         # Should be active (running)
sudo systemctl status dnsmasq         # Should be active (running)
```

---

## Troubleshooting

### Check if wlan0 has the correct IP:
```bash
ip addr show wlan0
```
Should show `inet 192.168.5.1/24`

### Check services are running:
```bash
sudo systemctl status hostapd
sudo systemctl status dnsmasq
```

### View logs:
```bash
sudo journalctl -u hostapd -n 50
sudo journalctl -u dnsmasq -n 50
```

### Manually assign IP if needed:
```bash
sudo ip addr add 192.168.5.1/24 dev wlan0
sudo systemctl restart dnsmasq
```

---

## Why This Setup Is Needed

- **Debian 13 Trixie** is a testing release with some network management quirks
- **BCM43438 chipset** in Pi 3B v1.2 has known driver issues with WPA encryption in NetworkManager
- **dhcpcd service** doesn't exist or work properly on Trixie, requiring the rc.local workaround
- The **old hostapd + dnsmasq method** is more reliable for this specific hardware/software combination

---

## Network Configuration Summary

- **AP SSID:** MyPiAP (change in `/etc/hostapd/hostapd.conf`)
- **AP Password:** raspberry (change in `/etc/hostapd/hostapd.conf`)
- **AP IP:** 192.168.5.1
- **DHCP Range:** 192.168.5.2 - 192.168.5.20
- **DNS Server:** 8.8.8.8 (Google DNS)
- **WiFi Channel:** 6 (2.4GHz)

