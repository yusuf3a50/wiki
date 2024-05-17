password login to SSH servers is inherently insecure which is why you need to:

### create a key-pair
`ssh-keygen -t rsa -b 4096`

now transfer the public key to the server
and put the private key in your `~/.ssh` folder

change the server's SSH port to something non-standard and above 1024