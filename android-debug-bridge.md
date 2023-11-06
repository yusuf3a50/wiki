#### 1. install android-debug-bridge:
```
sudo apt update
sudo apt install android-tools-adb
```

#### 2. add rules to your PC's firewall to allow an ADB connection to the phone:
```
sudo iptables -I OUTPUT 2 -o lo -p tcp --dport 5037 -j ACCEPT
sudo iptables -I OUTPUT 2 -o lo -p udp --dport 5037 -j ACCEPT
sudo ip6tables -I OUTPUT 2 -o lo -p icmpv6 -j ACCEPT
```

#### 3. start adb service:
```
adb start-server
```

this will take a few minutes(!)

#### 4. enable android debugging on your android device: 
settings > developer options > debugging > USB debugging - debug mode when USB is connected: toggle to enable

#### 5. plug your android device into your computer
- be sure you are using a data capable USB cable that is not faulty
- your android device should give you a prompt asking whether you would like to allow access by your PC and give a fingerprint your computer is using. You must allow this access to proceed

#### 6. Check whether adb detects your android device
```
adb devices
```

If a device is displayed, then youre good to go!

#### 7. sideload installation of apk
Be sure to take any steps you can to verify the APK before installing it to your device. Eg. PGP verification or using `apksigner`
```
adb install app_file.apk
```