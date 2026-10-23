# gpg_verification.md

### Check a keyserver to see if it has the key with a given key ID:
```
curl -fsSL "https://keys.openpgp.org/vks/v1/by-keyid/[KEY ID HERE]" | gpg --show-keys --keyid-format long -
```

### Search by email, name, or key ID with GnuPG:
```
gpg --keyserver hkps://keyserver.ubuntu.com --search-keys 'name@example.com'
```

### Check a keyserver to see who has signed the key with a given key ID. Exclude extraneous entries where the User ID is not found.
```
curl -fsSL "https://keys.openpgp.org/vks/v1/by-keyid/[KEY ID HERE]" | gpg --list-sigs | grep -v "User ID not found"
```

### Import a key into gpg directly from a URL rather than a keyserver:
```
curl -fsSL 'https://example.com/key.asc' | gpg --import
```