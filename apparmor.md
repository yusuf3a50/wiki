sudo apt install apparmor-notify apparmor-profiles apparmor-utils

Profiles are stored here:

```
/etc/apparmor.d/
/etc/apparmor.d/tunables/home
/etc/apparmor.d/local/
```

snaps are special, you’ll find snap apparmor profiles here:

`/var/lib/snapd/apparmor/profiles/`

Grant Read-Only Access: To grant read-only permissions to a system folder, you can add a rule to the AppArmor profile that allows read access to the specific folder. The syntax for granting read access is as follows:

`/path/to/folder/ r,`

Reload the Profile: To apply the modified profile, you need to reload the AppArmor profiles. You can do this by running the following command:

`sudo apparmor_parser -r /etc/apparmor.d/<profile_name>`


[Documentation](https://ubuntu.com/server/docs/apparmor)
