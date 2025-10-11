======================
table-of-contents
======================

#. `set up`_
#. `new local repo`_
#. `configs`_
#. `example usages`_
#. `ignore`_
#. `references`_


set up
-----------

`git <https://docs.github.com/en/get-started/quickstart/set-up-git>`_

`ssh <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_

change permission if drop ssh into .ssh::

    chmod 600 ~/.ssh/id_ed25519 # 600 means only you can read and write


new local repo
-------------------

.. code-block:: console

    mkdir test
    cd test
    git init

    #linux
    touch README.md
    #windows
    type nul > README.md

    git add .
    git commit -m "first commit"
    git branch -M main

    #add remote repo
    git remote add origin <remote repository URL>
    git push -u origin main

make branch, push, set tracking to origin same branch::

    git branch -C dev
    git checkout dev
    git push origin HEAD
    git branch --set-upstream-to=origin/dev dev

use a branch from github, set up local tracking branch::

    git checkout --track origin/branch-name

create a fork, then add original as a remote::

    # create a fork on github, then clone it, cd into it

    # Add the original repository as a remote named 'upstream'
    git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git

    # Fetch the branches and their commits from the 'upstream'
    git fetch upstream

    # Switch to your local 'main' or 'master' branch
    git checkout main

    # Merge the changes from 'upstream/main' into your local 'main' branch
    git merge upstream/main

configs
-------------
basic::

    git config --global pull.rebase false
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"

open and edit::
    
    git config --global --edit
    # show config file location
    git config --list --show-origin

custom shortcut::

    git config --global alias.s status
    git config --global alias.c '!git add -A && git commit -m'

content

.. code-block:: console

    [pull]
        rebase = false
    [user]
        email = sdf@outlook.com
        name = sdf
    [alias]
        s = status
        p = pull
        c = !git add . && git commit -m
        ps = push
        l = log --oneline --graph --decorate


example usages
-------------------

a::

    git add .
    git add -A
    git add -u

b::

    git branch
    git branch -a
    git branch -d branch-name
    git branch -D branch-name
    git branch -m old-name new-name

    #make branch, push, set tracking to origin same branch
    git branch -C dev
    git checkout dev
    git push origin HEAD
    git branch --set-upstream-to=origin/dev dev

    #bisect
    git bisect start
    git bisect bad
    git bisect good 1.0
    git bisect reset

c::

    git -C /path/to/repo status

    git checkout branch-name
    git checkout -b branch-name
    git checkout -b branch-name origin/branch-name
    #switch to previous branch
    git checkout -

    #use a branch from github, set up local tracking branch
    git checkout -t origin/branch-name
    git checkout --track origin/branch-name

    #amend
    git commit --amend -m "New commit message"

    #undo last commit
    git clean -n # show what will be removed
    git clean -f # remove
    $ git commit --amend -m "New commit message"

    #add file to last commit
    git add .
    git commit --amend --no-edit

    #undo last commit
    git clean -n
    git clean -f

    #apply a particular commit on current branch
    git cherry-pick 123456

d::

    git diff
    git diff --cached
    git diff --staged

f::

    git fetch
    git fetch --all
    git fetch --all --prune
    git fetch --prune
    git fetch --tags

l::

    git log
    git log --oneline
    git log --oneline --graph
    git log --oneline --graph --decorate

    #reflog
    git reflog

m::

    git merge branch-name
    git merge --abort

p::

    git pull
    git pull --rebase
    git pull --rebase origin branch-name

    # make a patch file from a commit
    git format-patch -1 
    git format-patch -1 0123456

r::

    git remote -v
    git remote add origin

    #reset to a cloud commit
    git fetch origin
    git reset --hard origin/master
    git clean -df

    #interactive rebase to reorgansie commits
    git rebase -i 01482b4
    #reorganise via cmds: pick, squash, edit, reword, fixup, exec, drop

    # squash and reorder example
    git rebase -i 0000000
    # pick 0000002
    # squash 0000003
    # pick 0000001

    #auto squash commits
    git commit -m "fix: fix bug"
    git commit --squash 123456
    git rebase -i --autosquash

    #revert last commit
    git revert HEAD
    #revert but preserve changes
    git revert HEAD --no-commit

s::

    git status
    git status -s
    git status -sb

    #save a stash and apply it
    git stash
    git stash pop

    #save a stash with a message
    git stash save part1
    git stash list
    git stash apply 0

t::

    git tag
    git tag -a v1.0 -m "version 1.0"
    git tag -d v1.0
    git tag -l "v1.*"
    git tag -v v1.0

w::

    git worktree add ../branch-name branch-name
    git worktree list
    git worktree prune
    git worktree remove ../branch-name

git diff
^^^^^^^^^

Usage::

    git diff topic master    # (1) Changes between the tips of the topic and the master branches.
    git diff topic..master   # (2) Same as above.
    git diff topic...master  # (3) Changes that occurred on the master branch since when the topic branch was started off it.


Example in powershell::

    # Create a new master branch
    git init git-diff-example
    cd git-diff-example
    echo "Hello" > hello.txt
    echo "World" > world.txt
    git add .
    git commit -m "Initial commit"

    # Create a new branch and make some changes
    git checkout -b topic
    echo "Hello World" > hello.txt
    echo "modified" > world.txt
    git add .
    git commit -m "Modified hello.txt and world.txt"

    # Switch back to master and make some changes
    git checkout master
    echo "Master" > master.txt
    echo "Master hello" > hello.txt
    git add .
    git commit -m "Added master.txt and modified hello.txt"

git diff topic master::

    --- a/hello.txt
    +++ b/hello.txt
    -Hello World
    +Master hello

    --- /dev/null
    +++ b/master.txt
    @@ -0,0 +1 @@
    +Master

    --- a/world.txt
    +++ b/world.txt
    @@ -1 +1 @@
    -modified
    +World

git diff topic...master::

    --- a/hello.txt
    +++ b/hello.txt
    -Hello
    +Master hello

    --- /dev/null
    +++ b/master.txt
    @@ -0,0 +1 @@
    +Master


git stash
^^^^^^^^^^^

Interrupted workflow::

    # Create a new repository
    git init
    echo "Hello" > hello.txt
    git add hello.txt
    git commit -m "Initial commit"

    # Make some changes that are WIP
    echo "World" > world.txt
    echo "Goodbye" >> hello.txt
    
    # stash the working dir and index, make some changes, then pop the stash to continue
    # untracked files are not stashed
    git stash
    echo "!" >> hello.txt
    git commit -a -m "Fix in a hurry"
    git stash pop

ignore
-------------

`gitignore <https://github.com/github/gitignore>`_

ignore binaries::

    # Ignore all
    *
    # Unignore all with extensions
    !*.*
    # Unignore all dirs
    !*/
    

references
-------------

`git bash <https://stackoverflow.com/questions/17302977/how-to-launch-git-bash-from-windows-command-line>`_

`pro git <https://git-scm.com/book/en/v2>`_
