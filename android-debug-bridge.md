#### 1. install android-debug-bridge:
```
apt update
apt install android-tools-adb
```

#### 2. add rules to your PC's firewall to allow an ADB connection to the phone:
```
iptables -I OUTPUT 2 -o lo -p tcp --dport 5037 -j ACCEPT
iptables -I OUTPUT 2 -o lo -p udp --dport 5037 -j ACCEPT
ip6tables -I OUTPUT 2 -o lo -p icmpv6 -j ACCEPT
```

i. enable android debugging on your android device

ii. plug your PC into your android device

iii. start adb service and check for devices:
    ```
    adb devices
    ```

iv. (prompt on android device:)
    allow device with fingerprint..

#### 3. sideload installation of apk
```
adb install app_file.apk
```