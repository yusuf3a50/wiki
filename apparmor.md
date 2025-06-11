# AppArmor

AppArmor (Application Armor) is a Linux kernel security module that provides a framework for restricting the capabilities of programs based on predefined security profiles. It is designed to enhance the security of the operating system by enforcing access control policies that limit what resources applications can access, thereby reducing the risk of security breaches.

`sudo apt install apparmor-notify apparmor-profiles apparmor-utils`

For Alpine linux [the setup instructions are here](https://wiki.alpinelinux.org/wiki/AppArmor)

## To check the status, issue the below command:

``` bash
sudo apparmor_status
##OR
sudo aa-status
```

## Profiles, whether enabled or disabled, are stored here:

``` bash
/etc/apparmor.d/
/etc/apparmor.d/tunables/home
/etc/apparmor.d/local/
```

## Snaps ...
..are annoying, you’ll find snap apparmor profiles here:

`/var/lib/snapd/apparmor/profiles/`

If a non-existent snap profile is haunting you after youve uninstalled the snap app, restart your computer

## Grant Read-Only Access: 
To grant read-only permissions to a system folder, you can add a rule to the AppArmor profile that allows read access to the specific folder. The syntax for granting read access is as follows:

`/path/to/folder/ r,`


## Disabling or re-enabling a profile

The /etc/apparmor.d/disable directory can be used along with the apparmor_parser -R option to disable a profile:
``` bash
sudo ln -s /etc/apparmor.d/profile.name /etc/apparmor.d/disable/
# -R, --remove		Remove apparmor definitions
sudo apparmor_parser -R /etc/apparmor.d/profile.name
```

## Reload the Profile: 
To apply the modified profile, you need to reload the AppArmor profiles. You can do this by running the following command:

``` bash
# -r, --replace		Replace apparmor definitions
sudo apparmor_parser -r /etc/apparmor.d/<profile_name>
```

## Creating a profile
1. Find the location of the binary you want to create a profile for:
`which program_name`
2. Start generating the profile:
`aa-genprof /path/to/binary`

## Modes
### 1. Enforce Mode
- Actively restrict processes according to defined rules.
- Unauthorized actions (e.g., accessing restricted files or network resources) are blocked, and violations are logged (typically to `/var/log/messages` or `/var/log/syslog`)`.
- Used for production environments to secure applications.
- Example command to set: `sudo aa-enforce /usr/bin/code`
### 2. Complain Mode (also called Learning Mode)
- Monitor processes but do not restrict actions.
- Violations of profile rules are logged (e.g., to `/var/log/messages`) without blocking, allowing profile refinement.
- Ideal for testing or developing profiles to identify required permissions.
- Example command: `sudo aa-complain /usr/bin/code`
### 3. Disabled/Unconfined Mode
- Profiles are not loaded or applied, leaving processes unrestricted by AppArmor.
- Profiles remain in `/etc/apparmor.d/` but are not active unless moved to `/etc/apparmor.d/disable/` (optional in some distributions).
- Processes may still be subject to other system security mechanisms (e.g., Linux permissions).
- Can be set by unloading profiles: `sudo aa-disable /usr/bin/code` or removing them from the kernel.

## Which permissions is apparmor capable of managing?
### 1. File Permissions

Control access to files: read (r), write (w), execute (x with ix, px, ux), memory mapping (m), linking (l), and locking (k).

### 2. Directory Permissions

Manage directory access: read (r) for listing, write (w) for creating/deleting contents, and recursive access with wildcards (e.g., /### ).

### 3. Network Permissions

Restrict network access by protocol (e.g., tcp, udp) and address family (e.g., inet for IPv4, inet6 for IPv6), including port-specific rules.

### 4. Capability Permissions

Limit Linux capabilities (e.g., chown, dac_override) to control privileged operations like changing file ownership or bypassing access checks.

### 5. Mount Permissions

Regulate mounting and unmounting filesystems (e.g., mount, umount) to prevent unauthorized filesystem modifications.

### 6. Signal Permissions

Control sending/receiving signals between processes (e.g., signal (send) peer=profile_name) to restrict inter-process communication.

### 7. Ptrace Permissions

Manage process tracing/debugging (e.g., ptrace (read, trace) peer=profile_name) to limit debugging or inspection of other processes.

### 8. Unix Socket Permissions

Restrict Unix domain socket operations (e.g., unix (connect, listen)) for local inter-process communication.

### 9. Change Profile Permissions

Allow processes to switch to another AppArmor profile (e.g., change_profile) for dynamic security policy changes.

### 10. Deny Rules

Explicitly block specific permissions (e.g., deny /etc/** rw) to override broader allow rules and enhance security.

## Tips:
After setting apparmor to complain mode:

`aa-complain /usr/share/code`

You can then watch dmesg for apparmor logs about permissions contraventions with this command:

`watch 'dmesg | grep apparmor=\"DENIED | tail -f'`

## Further resources:
- [Ubuntu documentation](https://ubuntu.com/server/docs/apparmor)
- [Apparmor gitlab wiki](https://gitlab.com/apparmor/apparmor/-/wikis/home)
- [Alpine linux apparmor documentation](https://wiki.alpinelinux.org/wiki/AppArmor)
- See the [AppArmor Administration Guide](http://www.novell.com/documentation/apparmor/apparmor201_sp10_admin/index.html?page=/documentation/apparmor/apparmor201_sp10_admin/data/book_apparmor_admin.html) for advanced configuration options.
- For details using AppArmor with other Ubuntu releases see the [AppArmor Community Wiki](https://help.ubuntu.com/community/AppArmor) page.
- The [OpenSUSE AppArmor page](http://en.opensuse.org/SDB:AppArmor_geeks) is another introduction to AppArmor.
- https://wiki.debian.org/AppArmor is another introduction and basic how-to for AppArmor.

## Example apparmor profile:
``` bash

# /etc/apparmor.d/usr.share.code.bin.code

# Define the syntax and features used in the profile as that of: 
#AppArmor Application Binary Interface (ABI) version 3.0
abi <abi/3.0>,

# 0. Include statements
# 0.1 The profile can use predefined variables like @{HOME} (e.g., /home/*) or other tunables defined in /etc/apparmor.d/tunables/global
# If you comment out the following line then you must hardcode paths (e.g., /home/user/ instead of @{HOME}), which reduces portability across systems.
#include <tunables/global>

/usr/share/code/bin/code flags=(enforce) {
    # 0.2 inherit common permissions from /etc/apparmor.d/abstractions/base
    #include <abstractions/base>

    # 1. File Permissions

    # Allow execution of binaries
    /usr/bin/dash mrix,
    /usr/bin/env ix,
    /usr/share/code/bin/code r,

    # 2. Directory Permissions

    # Allow reading VS Code’s own files
    /usr/share/code/** r,

    # Allow read/write only in the specific folder
    /home/user/git/ r,
    /home/user/git/** rw,

    # Allow configuration access (needed for VS Code settings)
    /home/user/.config/Code/ r,
    /home/user/.config/Code/** rw,

    # Deny write access to other sensitive areas
    deny /home/user/** w,
    deny /etc/** rw,
    deny /root/** rw,

    # 3. Network Permissions
    network inet,
    network inet6,

    # Explicitly lock down all other permissions:

    # 4. Capability Permissions
    deny capability chown,
    deny capability dac_override,
    # 5. Mount Permissions
    deny mount,
    deny umount,
    # 6. Signal Permissions
    deny signal (send,receive),
    # 7. Ptrace Permissions
    deny ptrace (read,trace),
    # 8. Unix Socket Permissions
    deny unix (connect,listen),
    # 10. Deny Rules
    deny change_profile,
    deny /etc/** rw,
}

# Steps to apply:
# 1. Load Profile
# sudo apparmor_parser /etc/apparmor.d/usr.share.code.bin.code
# 2. Set Enforce Mode
# sudo aa-enforce /usr/share/code/bin/code
# 3. Verify Logs: Check for blocked actions
# cat /var/log/messages | grep apparmor

```