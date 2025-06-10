### How to fix this error message

First, list all the GPG keys added to your system.

```
sudo apt-key list
```

So from the line (eg.) “DB08 5A08 CA13 B8AC B917 E0F6 D938 EC0D 0386 51BD”, I’ll take the last 8 characters “0386 51BD”, remove the space and then use it to import the GPG key in its dedicated file under the /etc/apt/trusted.gpg.d directory:

```
sudo apt-key export 038651BD | sudo gpg --dearmour -o /etc/apt/trusted.gpg.d/slack.gpg
```

[source](https://itsfoss.com/key-is-stored-in-legacy-trusted-gpg/)