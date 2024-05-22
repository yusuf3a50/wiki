password login to SSH servers is inherently insecure which is why you need to:

### create a key-pair

`ssh-keygen -t rsa -b 4096`

now transfer the public key to the server
and put the private key in your `~/.ssh` folder

#### Private keys begin with:

`-----BEGIN OPENSSH PRIVATE KEY-----`

#### Public keys (RSA) begin with:

`ssh-rsa`


change the server's SSH port to something non-standard and above 1024

#### Private key permissions
When importing a private key you may need to set the permissions of the key file to be minimal before you can run SSH

`chmod 0400` is the most minimal functioning permissions but `0700` also works


#### to login to server:
`ssh -i .ssh/privateKey root@192.168.1.1 -p [non-standard port number]`