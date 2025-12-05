## Git Əmirləri

```bash
FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation
$ git add .
fatal: not a git repository (or any of the parent directories): .git

FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation
$ git init
Initialized empty Git repository in C:/Users/FUJITSU/OneDrive/Documents/FlaskInstallation/.git/

FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation (master)
$ git add .

FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation (master)
$ git commit -m "initial commit"
[master (root-commit) b5f3cc8] initial commit
 4 files changed, 42 insertions(+)
 create mode 100644 README.md
 create mode 100644 Readme1.md
 create mode 100644 start.py
 create mode 100644 templates/index.html

FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation (master)
$ git remote add origin https://github.com/Heyyam0855/Procekt.git

FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation (master)
$ git push -u origin master
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 963 bytes | 192.00 KiB/s, done.
Total 7 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Heyyam0855/Procekt.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.

FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation (master)
$ git add . && git commit -m "Flask project start"
[master d5536e0] Flask project start
 1 file changed, 18 insertions(+)
 create mode 100644 .gitignore

FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation (master)
$ git add .

FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation (master)
$ git push -u origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 502 bytes | 251.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Heyyam0855/Procekt.git
   b5f3cc8..d5536e0  master -> master
branch 'master' set up to track 'origin/master'.

FUJITSU@DESKTOP-B7QS1QG MINGW64 ~/OneDrive/Documents/FlaskInstallation (master)
```