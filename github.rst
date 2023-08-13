======================
table-of-contents
======================

#. `set up`_
#. `configs`_
#. `example usages`_
#. `ignore`_
#. `references`_


set up
-----------

`git <https://docs.github.com/en/get-started/quickstart/set-up-git>`_

`ssh <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_

change permission if drop ssh into .ssh::

    chmod 600 ~/.ssh/id_ed25519



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

    git config --global alias.st status
    git config --global alias.ac '!git add -A && git commit -m'

content

.. code-block:: console

    aa


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

c::

    git checkout branch-name
    git checkout -b branch-name
    git checkout -b branch-name origin/branch-name

    #use a branch from github, set up local tracking branch
    git checkout --track origin/branch-name

    #amend
    git commit --amend -m "New commit message"

    #add file to last commit
    git add .
    git commit --amend --no-edit

    #undo last commit
    git clean -n
    git clean -f


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

m::

    git merge branch-name
    git merge --abort

p::

    git pull
    git pull --rebase
    git pull --rebase origin branch-name

r::

    git remote -v
    git remote add origin

s::

    git status
    git status -s
    git status -sb

    git stash
    git stash pop

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