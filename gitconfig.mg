- When you have multiple git accounts, the following setup automates git to push using the correct git credentials when in the respective folder (eg. githubUsername1Folder/repositoryName1).

- Create an SSH keypair and upload the public key to your github account(s) before setting up this configuration on your local machine

~/.gitconfig:
```
[includeIf "gitdir:~/git/githubUsername1Folder/"]
  path = ~/git/githubUsername1Folder/.gitconfig
[includeIf "gitdir:~/git/githubUsername2Folder/"]
  path = ~/git/githubUsername2Folder/.gitconfig

[filter "lfs"]
      clean = git-lfs clean -- %f
      smudge = git-lfs smudge -- %f
      process = git-lfs filter-process
      required = true
```

~/githubUsername1Folder/.gitconfig:
```
[user]
	name = username1
	email = username1@email.com
[core]
	sshCommand = "ssh -i ~/.ssh/username1privateSSHkey"
```
~/githubUsername2Folder/.gitconfig:
```
[user]
	name = username2
	email = username2@email.com
[core]
	sshCommand = "ssh -i ~/.ssh/username2privateSSHkey"
```