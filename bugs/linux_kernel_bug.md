check the current kernel version running on your host machine.

`uname -r`


view list of installed linux kernels:

`dpkg --list | grep linux-image`

Remove the image and headers of the kernel which you want to remove:

```
sudo apt-get purge linux-image-3.19.0-15
sudo apt-get purge linux-headers-3.19.0-15
```

After removing the unused kernel, update the GRUB configuration.

`sudo update-grub2`

There's a script called 'purge-old-kernels' which available in the byobu package:

```
apt-get install byobu
purge-old-kernels
```
You can specify how many kernels to keep excluding the current in-use kernel:

`purge-old-kernels --keep 2`

Put this in cron if you need.