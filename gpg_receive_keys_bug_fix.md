This wiki post is a fix for the following ubiquitous bug:
```
gpg: key 4AEE18F83AFDEB23: new key but contains no user ID - skipped
gpg: Total number processed: 1
gpg:           w/o user IDs: 1
```

1. This first keyserver usually works fine:

`gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys 0x<key ID>`

2.But if not, try these other keyservers

`gpg --keyserver hkps://pgp.surf.nl --recv-keys 0x<key ID> # (ex-SKS pool)`

`gpg --keyserver hkp://pgp.rediris.es --recv-keys 0x<key ID> # (ex-SKS pool)`
