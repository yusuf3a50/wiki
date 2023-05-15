- When you have multiple git accounts, the following setup automates git to push using the correct git credentials when in the respective folder (eg. githubUsername1Folder/repositoryName1).

- Create an SSH keypair `ssh-keygen -t rsa -b 4096` and upload the public key of the pair to your github account(s) before setting up the following configuration on your local machine

~/.gitconfig:
```
[includeIf "gitdir:~/git/githubUsername1Folder/"]
  path = ~/git/githubUsername1Folder/.gitconfig
[includeIf "gitdir:~/git/githubUsername2Folder/"]
  path = ~/git/githubUsername2Folder/.gitconfig

#the following entries are optional and can cause problems
[filter "lfs"]
      clean = git-lfs clean -- %f
      smudge = git-lfs smudge -- %f
      process = git-lfs filter-process
      required = true
```

~/git/githubUsername1Folder/.gitconfig:
```
[user]
	name = FirstName Surname
	email = username1@email.com
	username = username1

[core]
	sshCommand = "ssh -i ~/.ssh/username1privateSSHkey"
```
~/git/githubUsername2Folder/.gitconfig:
```
[user]
	name = FirstName Surname
	email = username2@email.com
	username = username2

[core]
	sshCommand = "ssh -i ~/.ssh/username2privateSSHkey"
```

![tables of git config file locations](gitconfig.png)