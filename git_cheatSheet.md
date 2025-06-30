### Info about last commit including timestamp

`git show`

### get the timestamp of the last commit

`git log -1 --format=%cd`

### Oops, I need to delete the last 2 commits:

#### Step 0 - Preparation

Before manipulating the Git history, ensure that your working directory is clean of any changes using the `git status` command.

#### Step 1 - Delete commits locally

To delete commits from a remote server, first, you will need to remove them from your local history.
1.1 For consecutive commits from the top

If the commits you want to remove are placed at the top of your commit history, use the `git reset --hard` command with the HEAD object and the number of commits you want to remove.

- This command will remove the latest commit:
`git reset --hard HEAD~1`

- This command will remove the latest three commits: 
`git reset --hard HEAD~3`

- You can also remove up to a specific commit using a commit’s hash, like so: `git reset --hard <hash>`

#### Step 2 - Delete the commits from remote

To delete commits from remote, you will need to push your local changes to the remote using the git push command.

```git push origin HEAD --force```

Since your local history diverges from the remote history, you need to use the force option.

[source](https://hackernoon.com/how-to-delete-commits-from-remote-in-git)



#### Some more commands
```git status```

```git show```

```git checkout -b new_branch_name```

```git switch main```

##### History:
```git log```

or

```git log --oneline```

##### go to a specific commit

```git checkout <commit-id>```