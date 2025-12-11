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

### Create a git subtree
Useful for when you want to import some specific folders from another repository (git submodule only allows importing a whole repository)

#### Step 1: Create a split branch in the Source Repository
```bash
# Split out only the specific folder into a new branch
git subtree split --prefix=<source-folder-path> -b <split-branch-name>
git subtree split --prefix=path/to/module -b module-api-only

# Push this new branch to remote
git push <remote-name> <split-branch-name>
git push origin module-api-only
```

#### Step 2: Create a subtree in your Destination Repository
```bash
# Import only the specific folder from the split branch
git subtree add --prefix=<destination-folder-path> <source-repository-url> <split-branch-name> --squash
git subtree add --prefix=path/to/module https://github.com/username/source-repo.git module-api-only --squash
```

#### Troubleshooting:
If you get the following error: `fatal: working tree has modifications.  Cannot add.` then you may have uncommitted changes in your working tree.

#### Step 3: Push changes to the source repo's split branch
Make sure you are on the branch intended
```bash
# Make changes to files in the subtree directory
git add <destination-folder-path>/<modified-file>
git add path/to/module/script.py

git commit -m "Refactor module script to support import"

# Push to your working branch
git push <remote-name> <working-branch-name>
git push origin feature-branch

# Push changes back to the split branch
git subtree push --prefix=<destination-folder-path> <source-repository-url> <split-branch-name>
git subtree push --prefix=path/to/module https://github.com/username/source-repo.git module-api-only
```

#### Step 4: Pull changes from the source repo's split branch into your subtree
```bash
# Pull updates from the split branch into your subtree
git subtree pull --prefix=<destination-folder-path> <source-repository-url> <split-branch-name> --squash
git subtree pull --prefix=path/to/module https://github.com/username/source-repo.git module-api-only --squash
```

#### Step 5: Updating the split branch in the source repo
In the source repo, I have made some changes on a branch and I want to push those changes to that branch's split branch
```bash
git checkout branch_name

git subtree push --prefix=<destination-folder-path> origin <split-branch-name>
git subtree push --prefix=path/to/module origin module-api-only
```

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