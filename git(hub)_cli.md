# Git CLI



## Basic Push

**Add** all modified instances:
```bash
git add -A 
```

Some specific files can be added with:
```bash
git add < file >
```


**Commit** changes with:
```bash
git commit -m "< message >"
```

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

To remove from a repo and specific branch:
```bash
git reset --hard <repo>/<branch>
```

