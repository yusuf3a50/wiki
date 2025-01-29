To encrypt a file on disk using GPG (GNU Privacy Guard) with a password, you can follow these steps:

Install GPG: If you haven't already installed GPG, you can do so using your package manager. For example:
    On Ubuntu/Debian: sudo apt install gnupg
    On macOS: brew install gnupg
    On Windows, you can download it from the GnuPG website.
Encrypt the file: Use the following command to encrypt a file with a password:


```bash
gpg -c filename
```

Replace filename with the name of the file you want to encrypt. The -c option tells GPG to use symmetric encryption, which means it will prompt you for a passphrase.

Enter a passphrase: After running the command, you will be prompted to enter a passphrase. This passphrase will be required to decrypt the file later. Make sure to choose a strong passphrase and remember it.

Output file: GPG will create an encrypted file with the same name as the original file but with a .gpg extension (e.g., filename.gpg).

Decrypting the file: To decrypt the file later, you can use the following command:

```bash
gpg filename.gpg
```

You will be prompted to enter the passphrase you used during encryption. After entering the correct passphrase, GPG will create the original file again.