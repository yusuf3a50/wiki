### Establish chroot into the root volume
mount the root partition first then:
```
for dir in /proc /sys /dev /dev/pts /run; do sudo mount --bind $dir /mnt/$dir; done
sudo chroot /mnt bash
```
