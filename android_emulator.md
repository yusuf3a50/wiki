### Run an android VM from a custom location:
1. Make sure the required SDK is installed:
Android Studio > Tools > SDK manager:
    SDK Platforms: make sure the Android SDK Platform 31 version which the android VM uses is installed corresponding to your API level, eg. Android 12.0 corresponding to API level 31
        Androi

I have imported the android VM .ini file from /media/user/backups/.android/avd/ to /home/$USER/.android/avd/
It looks like this:

```
avd.ini.encoding=UTF-8
path=/home/$USER/.android/avd/Pixel_6_Pro_API_31_fresh.avd
path.rel=avd/Pixel_6_Pro_API_31_fresh.avd
target=android-31
```

then i change line 2 to reflect the location of my avd files:

```
path=/media/user/backups/.android/avd/Pixel_6_Pro_API_31_fresh.avd
```

but then there are also the following files which maybe need reconfiguring as well:
 - `/media/user/backups/.android/avd/Pixel_6_Pro_API_31_fresh.avd/hardware-qemu.ini`
 - `/media/user/backups/.android/avd/Pixel_6_Pro_API_31_fresh.avd/config.ini`

what about this line?:
`android.avd.home = /home/user/.android/avd`

this line looks okay:
`disk.dataPartition.path = /media/user/backups/AndroidVMs/.android/avd/Pixel_6_Pro_API_31_fresh.avd/userdata-qemu.img`