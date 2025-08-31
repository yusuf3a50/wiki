# Crypsetup

### change password
[Link to article on the subject](https://www.cyberciti.biz/security/how-to-change-luks-disk-encryption-passphrase-in-linux/)

``` bash
sudo su
cat /etc/crypttab
cryptsetup luksDump /dev/sdax
cryptsetup --verbose open --test-passphrase /dev/sdax
cryptsetup luksChangeKey /dev/sdax -S 0
cryptsetup --verbose open --test-passphrase /dev/sdax
```