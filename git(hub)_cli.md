# Git CLI

## Clone repository

**Clone** from HTTPS link:
```bash
git clone <repo-link>.git
```

To perform git operations in the repository:
```bash
cd <new-repository-folder>
```

Get **status** of git:
```bash
git status
```

## Basic Push

**Add** all modified instances:
```bash
git add -A 
```

Some specific files can be added with:
```bash
git add <file>
```

This command takes the modified file in your working directory and places the modified version in a staging area.

**Commit** changes with:
```bash
git commit -m "<message>"
```

Takes everything from the staging area and makes a permanent snapshot of the current state of your repository that is associated with a unique identifier.

Commit message should be informative and help understand the changes and why.

If you have configured git to use your favorite text editor (via git config --global core.editor your-fav-editor-here), then you can open that editor to write your commit message

**Push** with:
```bash
git push
```

:warning: **Login** information is described as such:
 - username: GitHub username of the account
 - password: access token generated on the platform (Developer tools-> Personal access tokens -> Tokens (classic))


## Undo Add and Commit

**Undo** commit:
```bash
git reset HEAD~
```
undo last commit while leaving your working tree (files on disk) untouched.

To **undo** commit for a repo and specific branch:
```bash
git reset --hard <repo>/<branch>
```

