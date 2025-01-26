- MS2109 - bought
idVendor=534d, idProduct=2109, bcdDevice=21.00
strings: Mfr=1, Product=2, SerialNumber=0
Manufacturer: MACROSILICON
Found UVC 1.00 device USB Video (534d:2109)
hid-generic 0003:534D:2109.0006: hiddev0,hidraw2: USB HID v1.10 Device [MACROSILICON USB Video] on usb-0000:00:14.0-1.1/input4

- MS2130 chipset is primarily designed for USB 2.0 interfaces

- MS2131 chipset is an evolution of the MS2130, offering potential improvements in performance and video quality while still primarily operating within the constraints of USB 2. MS2131 may offer improved performance over the MS2130 in terms of video quality, frame rates, and possibly lower latency. [Review here](https://www.eevblog.com/forum/reviews/4k-ultrahd-usb3-0-1080p-60fps-hdmi-capture-card-on-macrosilicon-ms2131-chip/)


MS2130, a HD video and audio capture chip that’s compatible with USB 3.2 Gen 1.


MS2133, 
MS2135, and 
MS2136


finding info about a card you have:

```
sudo apt install v4l-utils
v4l2-ctl --list-devices
v4l2-ctl --device=/dev/video2 --all
```
