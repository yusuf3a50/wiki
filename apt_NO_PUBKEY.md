This is a fix for the following error message:

W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://dl.google.com/linux/chrome/deb stable InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY E88979FB9B30ACF2


```
gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys E88979FB9B30ACF2
gpg --export --armor E88979FB9B30ACF2 | sudo apt-key add -
```