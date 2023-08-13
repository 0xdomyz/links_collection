.. ---------------------
.. table-of-contents
.. ---------------------


git/hub
-----------

`git <https://docs.github.com/en/get-started/quickstart/set-up-git>`_

`ssh <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_

change permission if drop ssh into .ssh::

    chmod 600 ~/.ssh/id_ed25519

::

    git config --global pull.rebase false
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"

make branch, push, set tracking to origin same branch::

    git branch -C dev
    git checkout dev
    git push origin HEAD
    git branch --set-upstream-to=origin/dev dev

use a branch from github, set up local tracking branch::

    git checkout --track origin/branch-name

`git bash <https://stackoverflow.com/questions/17302977/how-to-launch-git-bash-from-windows-command-line>`_

`pro git <https://git-scm.com/book/en/v2>`_

`gitignore <https://github.com/github/gitignore>`_

ignore binaries::

    # Ignore all
    *
    # Unignore all with extensions
    !*.*
    # Unignore all dirs
    !*/

.. code-block:: console

    git clean -n
    git clean -f
    $ git commit --amend -m "New commit message"

