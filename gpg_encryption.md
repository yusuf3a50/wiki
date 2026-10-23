#### To encrypt a file on disk using GPG (GNU Privacy Guard) with a password, you can follow these steps:

```bash
gpg -c filename
```

The -c option tells GPG to use symmetric encryption, which means it will prompt you for a passphrase.

##### Enter a passphrase:
After running the command, you will be prompted to enter a passphrase. This passphrase will be required to decrypt the file later. Make sure to choose a strong passphrase and remember it.

##### Output file: 
GPG will create an encrypted file with the same name as the original file but with a .gpg extension (e.g., filename.gpg).

##### Decrypting the file: 
To decrypt the file later, you can use the following command:

```bash
gpg filename.gpg
```

You will be prompted to enter the passphrase you used during encryption. After entering the correct passphrase, GPG will create the original file again.