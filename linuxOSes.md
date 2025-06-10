# LinuxOSes
## A non-exhaustive list of Linux operating systems

### Alpine Linux

Installation instructions: [1](https://wiki.alpinelinux.org/wiki/Installation#Custom_Installation_Instructions), [2](https://wiki.alpinelinux.org/wiki/Tutorials_and_Howtos#Virtualization), [3](https://wiki.alpinelinux.org/wiki/Setup-desktop)

you may need to add these lines to `/etc/apk/repositories`:
``` bash
https://dl-cdn.alpinelinux.org/alpine/v3.22/main
https://dl-cdn.alpinelinux.org/alpine/v3.22/community
```

To install certain software which is only available in testing, add this line to `/etc/apk/repositories`
``` bash
https://dl-cdn.alpinelinux.org/alpine/edge/testing
```

Cons: Doesnt support .deb packages.

### PureOS
Debian lightweight security hardened OS
!DOES NOT have any cryptographic signature verification methods!

### AntiX
### MX Linux
