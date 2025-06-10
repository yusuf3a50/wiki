AppArmor

AppArmor (Application Armor) is a Linux kernel security module that provides a framework for restricting the capabilities of programs based on predefined security profiles. It is designed to enhance the security of the operating system by enforcing access control policies that limit what resources applications can access, thereby reducing the risk of security breaches.

`sudo apt install apparmor-notify apparmor-profiles apparmor-utils`

#### To check the status, issue the below command:

```
sudo apparmor_status
##OR
sudo aa-status
```

#### Profiles are stored here:

```
/etc/apparmor.d/
/etc/apparmor.d/tunables/home
/etc/apparmor.d/local/
```

#### snaps are annoying, you’ll find snap apparmor profiles here:

`/var/lib/snapd/apparmor/profiles/`

If a non-existent snap profile is haunting you after youve uninstalled the snap app, restart your computer

#### Grant Read-Only Access: 
To grant read-only permissions to a system folder, you can add a rule to the AppArmor profile that allows read access to the specific folder. The syntax for granting read access is as follows:

`/path/to/folder/ r,`


#### Disabling or re-enabling a profile

The /etc/apparmor.d/disable directory can be used along with the apparmor_parser -R option to disable a profile:
```
sudo ln -s /etc/apparmor.d/profile.name /etc/apparmor.d/disable/
sudo apparmor_parser -R /etc/apparmor.d/profile.name
```


#### Reload the Profile: 
To apply the modified profile, you need to reload the AppArmor profiles. You can do this by running the following command:

`sudo apparmor_parser -r /etc/apparmor.d/<profile_name>`


[Documentation](https://ubuntu.com/server/docs/apparmor)
