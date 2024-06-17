### Installation instructions for mysql-workbench and mariadb on debian

We will use snap to install workbench. However, Debian comes configured to not use snap. Remove this preference by removing the following config file:

`sudo rm /etc/apt/preferences.d/nosnap.pref`


Install snap, workbench and mariadb:

```
sudo apt update
sudo apt install snapd mariadb-server

sudo snap install mysql-workbench-community
```


Check that the mariadb service is running:

`sudo service mariadb status`

Enter into the mariadb console:

`sudo mariadb`

Create a new user:

`MariaDB [(none)]> create user 'user'@'localhost' identified by 'pass_word';`


Allow full control to that user:

`MariaDB [(none)]> GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';`

Reloading the privileges tables
```
MariaDB [(none)]> FLUSH PRIVILEGES;
MariaDB [(none)]> exit
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
