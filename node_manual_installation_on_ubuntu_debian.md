Yes you could just execute the automatic bash script from [here](https://nodesource.com/blog/installing-node-js-tutorial-ubuntu/)

But if youre like me and prefer to have more control and oversight over your operating system, this is the way to manually install node from the official repository.

1. Paste this into `/etc/apt/sources.list.d/node.source.list`, replacing 'focal' with whichever distro you have installed

``` bash
deb [arch=amd64 signed-by=/usr/share/keyrings/nodesource.gpg] https://deb.nodesource.com/node_24.x nodistro main
```

2. You will also need to add the nodesource gpg key to allow your system to verify downloads from the new repository youve just added:

``` bash
curl https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/nodesource.gpg
chmod 644 /etc/apt/trusted.gpg.d/nodesource.gpg
```

3. Run:

`sudo apt update`

4. Now youre finally ready to install node:

`sudo apt-get install -y nodejs`
