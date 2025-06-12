## How to fix this error message

### Method 1

First, list all the GPG keys added to your system.

```
sudo apt-key list
```

So from the line (eg.) “DB08 5A08 CA13 B8AC B917 E0F6 D938 EC0D 0386 51BD”, I’ll take the last 8 characters “0386 51BD”, remove the space and then use it to import the GPG key in its dedicated file under the /etc/apt/trusted.gpg.d directory:

``` bash
sudo apt-key export 038651BD | sudo gpg --dearmour -o /etc/apt/trusted.gpg.d/slack.gpg
```

[source](https://itsfoss.com/key-is-stored-in-legacy-trusted-gpg/)

### Method 2:

Here is the same but starting from pulling the key down from a keyserver:
``` bash
gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys E88979FB9B30ACF2 && gpg --export E88979FB9B30ACF2 | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/keyname.gpg
```

### Method 3:

Here is another method with a different repo:

``` bash
wget -qO- https://www.virtualbox.org/download/oracle_vbox_2016.asc | sudo gpg --dearmor -o /etc/apt/keyrings/oracle-virtualbox.gpg

echo "deb [signed-by=/etc/apt/keyrings/oracle-virtualbox.gpg] http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
sudo apt update
```