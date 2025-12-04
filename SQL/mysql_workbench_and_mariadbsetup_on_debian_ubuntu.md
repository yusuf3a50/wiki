## Installation instructions for mysql-workbench and mariadb on debian

### Step 0: Install mysql-server
This is buggy as hell as not fully FOSS so I avoid it in favour of mariadb-server

### Step 1: Install mariadb

`sudo apt install mariadb-server`

Check that the mariadb service is running:

`sudo service mariadb status`

Enter into the mariadb console:

`sudo mariadb`

Create a new user:

`MariaDB [(none)]> create user 'user'@'localhost' identified by 'pass_word';`

Allow full control to that user:

`MariaDB [(none)]> GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';`

Reload the privileges tables
```
MariaDB [(none)]> FLUSH PRIVILEGES;
MariaDB [(none)]> exit
```

### Step 2: Install mysql-workbench
#### Method A: Direct download with GPG signature
1. Download the package for your system [here](https://downloads.mysql.com/archives/workbench/) along with the corresponding signature

2. Verify with the key:
```
gpg:                using RSA key BCA43417C3B485DD128EC6D4B7B3B788A8D3785C
gpg: Good signature from "MySQL Release Engineering <mysql-build@oss.oracle.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: BCA4 3417 C3B4 85DD 128E  C6D4 B7B3 B788 A8D3 785C
```

3. Install:
```
sudo dpkg -i packageName.deb
sudo apt --fix-broken install
sudo dpkg -i packageName.deb
```

##### Working examples:
1. `Linux Mint 21.1 (vera)`, 
Install: `sudo dpkg -i mysql-workbench-community_8.0.36-1ubuntu22.04_amd64.deb`

2. `Linux Mint 21.3`
N.B. I did not find a working method for this distro so I upgraded mint to 22 to avoid dependency hell(!)
Please let me know if you find any

2. Distro: `Linux Mint 22 (wilma)`, 
Dependency: `sudo apt install libodbc2`, 
Install: `sudo dpkg -i mysql-workbench-community_8.0.38-1ubuntu24.04_amd64.deb`, 
N.B.: despite the website stating that the correct install version for this distro is 8.0.36, this resulted in an unresolvable dependency (AFAIK)

#### Method B: Repositories
##### Warning:
This method does not support many versions of ubuntu. Either the .deb package doesnt have a corresponding GPG signature in the repo or the dependencies cant be resolved for the download (wrong ubuntu version)

##### Installation:

#### Method C: Snap 
##### Warning: see 'Issue' below:
Because snap there are issues with workbench connecting to mysql/mariadb installed on the base system/outside of snap. The recommended fixes did not work for me and I researched this issue quite extensively

##### Installation:
We will use snap to install workbench. However, Debian comes configured to not use snap. Remove this preference by removing the following config file:

`sudo rm /etc/apt/preferences.d/nosnap.pref`


Install snap, workbench and mariadb:

```
sudo apt update
sudo apt install snapd mariadb-server

sudo snap install mysql-workbench-community
```



Run workbench with:

`mysql-workbench-community`

In workbench, create and configure a new connection using the new user you just created:
1. Next to MYSQL Connections, click the '+' icon
2. Connection name: user
3. Username: user
4. Leave everything else as it is
5. Click OK
6. Click the new connection you just setup
7. If you get the following error follow this step:
"Cannot Connect to Database Server.. An AppArmor profile prevents this sender from sending this message to this recipient...."

`sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service`  ([instructions for this step are from here](https://blockdev.io/mysql-workbench-ubuntu-20-04-and-app-armor/))

8. Enter the password you used when setting up the new user, eg. pass_word
9. When you first enter workbench, you will get a "Connection Warning" message saying that "Incompatible/nonstandard server version or connection detected..". This is just because you setup workbench with mariadb instead of mysql. Click the "Dont show this message again" and now you can finally get busy using workbench!

N.B. Cant find the Output Area? Its definitely not hidden in View > Panels > Hide Output Area ? Try dragging up from just under the vertical scroll bar of the main area. And I mean about two pixels beneath(!) Behold you have discovered the Output Area! See the cursors location and icon in the image below:
![workbench secret output area](https://user-images.githubusercontent.com/95235745/197411327-64fe298d-ab43-4880-99b8-7248b7ad2625.png)


#### Issue:
on step 6, rather than connecting, error message:
    Your connection attempt for user 'user' to the MySQL server at 127.0.0.1:3306:
    user interaction failed
