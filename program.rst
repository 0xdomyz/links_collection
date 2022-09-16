
book
------

`SICP <https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-4.html#%_toc_start>`_

`lisp <https://norvig.com/lispy.html>`_

`clean <https://github.com/sdcuike/Clean-Code-Collection-Books/blob/master/Clean%20Architecture%20A%20Craftsman's%20Guide%20to%20Software%20Structure%20and%20Design.pdf>`_

`pragmatic2 <https://ebin.pub/the-pragmatic-programmer-your-journey-to-mastery-second-edition-20th-anniversary-edition-9780135957059-0135957052.html>`_

`cs50 <https://github.com/0xdomyz/cs50>`_

C
---

`vscode tute mingw <https://code.visualstudio.com/docs/cpp/config-mingw>`_

`vscode tute wsl <https://code.visualstudio.com/docs/cpp/config-wsl>`_

Chrome extension
-----------------

`Doco <https://developer.chrome.com/docs/extensions/mv3/>`_

`Examples <https://github.com/GoogleChrome/chrome-extensions-samples>`_

Cloud
--------

`example <https://gp2mv3.com/python-script-cloud-every-minute-for-free-with-aws-lambda/>`_

`docker <https://hub.docker.com/>`_

configs
-----------
`toml <https://github.com/toml-lang/toml>`_

`yaml tute <https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html>`_

`yaml org <https://yaml.org/>`_

`pyyaml <https://pyyaml.org/wiki/PyYAMLDocumentation>`_

Databases
------------

`windows postgres, oracle xe <https://dwopt.readthedocs.io/en/stable/set_up.html#dwopt.make_test_tbl>`_

`start stop oracle xe <https://docs.oracle.com/en/database/oracle/oracle-database/21/xeinw/starting-and-stopping-oracle-database-xe.html>`_

postgre on raspbery pi:

.. code-block:: console

    sudo apt install postgresql

    sudo nano /etc/postgresql/13/main/pg_hba.conf
    # change "local" is for Unix domain socket connections only method to md5

    pg_ctlcluster 13 main start

postgre on wsl:

.. code-block:: console

    sudo apt install postgresql

    sudo service postgresql restart

    sudo nano /etc/postgresql/12/main/pg_hba.conf
    # change "local" is for Unix domain socket connections only method to md5

    sudo pg_ctlcluster 12 main start

Emails
-----------------

`yahoo <https://login.yahoo.com>`_

`gmail <https://mail.google.com/>`_

`outlook <https://outlook.live.com/>`_

`burner <https://burnermail.io/premium>`_

`yandex <https://yandex.ru/>`_

`proton <https://protonmail.com/>`_

`sina <https://mail.sina.com.cn/>`_

`burner phone <https://quackr.io/>`_

git/hub
-----------

`git <https://docs.github.com/en/get-started/quickstart/set-up-git>`_

`ssh <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_

`git bash <https://stackoverflow.com/questions/17302977/how-to-launch-git-bash-from-windows-command-line>`_

`pro git <https://git-scm.com/book/en/v2>`_

`gitignore <https://github.com/github/gitignore>`_

.. code-block:: console

    git clean -n
    git clean -f

julia
--------

`install <https://julialang.org/downloads/>`_

`IJulia <https://github.com/JuliaLang/IJulia.jl#quick-start>`_

`course <https://juliaacademy.com/courses/intro-to-julia>`_

`doco <https://docs.julialang.org/en/v1/>`_

linux
-------
  
`shell tute <https://www.youtube.com/watch?v=BMGixkvJ-6w&t=621s&ab_channel=SkillsFactory>`_

Shortcuts:

.. code-block:: text

    ZDLAEUKWYPN
    ctrl + alt + T

`environment varible <https://askubuntu.com/questions/58814/how-do-i-add-environment-variables>`_

`background process <https://www.howtogeek.com/440848/how-to-run-and-control-background-processes-on-linux/amp/>`_

`supervisor <http://supervisord.org/introduction.html#overview>`_

Other
------------------

`Password safe <https://www.pwsafe.org/>`_

`Rapid api <https://rapidapi.com/hub>`_

`exit nano <https://bitlaunch.io/blog/how-to-exit-nano/>`_

`virtual mach <https://windowsreport.com/virtual-machine-software/>`_

`qtorrent <https://www.qbittorrent.org/>`_

R
-------

`R <https://cloud.r-project.org/>`_

`rstudio <https://www.rstudio.com/products/rstudio/download/#download>`_

`tidyverse <https://www.tidyverse.org/>`_

`dplyr <https://dplyr.tidyverse.org/articles/index.html>`_

`cheatsheets <https://www.rstudio.com/resources/cheatsheets/>`_

`graphic cookbook <https://r-graphics.org/recipe-quick-line>`_

`r4ds <https://r4ds.had.co.nz>`_

`package book <https://r-pkgs.org/>`_

`pkg tute <http://web.mit.edu/insong/www/pdf/rpackage_instructions.pdf>`_

`pkg website <https://pkgdown.r-lib.org/>`_

`reg weigths <https://alvaroaguado3.github.io/forcing-regression-coefficients-in-r-part-i/>`_

Rust
----------

`rust book <https://doc.rust-lang.org/book/ch00-00-introduction.html>`_

regexp
-----------

`spec <https://www.regular-expressions.info/>`_

shell
-------

`shell collection <https://github.com/0xdomyz/shell_collection>`_

vim
---------

`tute <https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/table-of-contents>`_

`cheatsheet <https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/cheatsheet>`_

`set up for python <https://realpython.com/vim-and-python-a-match-made-in-heaven/>`_

visual studio
---------------

`c++ build tools <https://visualstudio.microsoft.com/visual-cpp-build-tools/>`_

vscode
----------

`windows <https://code.visualstudio.com/>`_

`kill terminal <https://stackoverflow.com/questions/50569100/vscode-how-to-make-ctrlk-kill-till-the-end-of-line-in-the-terminal>`_

vscode user setting:

.. code-block:: json

    {
        "editor.renderWhitespace": "all",
        "editor.mouseWheelZoom": true,
        "python.terminal.activateEnvironment": false,
        "editor.rulers": [90],
        "explorer.confirmDelete": false,
        "terminal.explorerKind": "external",
        "workbench.startupEditor": "none",
        "terminal.integrated.defaultProfile.windows": "Command Prompt",
        "terminal.integrated.profiles.windows": {
            "PowerShell": {
                "source": "PowerShell",
                "icon": "terminal-powershell"
            },
            "Command Prompt": {
                "path": [
                    "${env:windir}\\Sysnative\\cmd.exe",
                    "${env:windir}\\System32\\cmd.exe"
                ],
                "args": [],
                "icon": "terminal-cmd"
            },
            "Git Bash": {
                "source": "Git Bash"
            }
        },
        "terminal.integrated.enableMultiLinePasteWarning": false
    }


vscode shortcut:

.. code-block:: json

    // Place your key bindings in this file to override the defaults
    [
        {
            "key": "ctrl+f6",
            "command": "workbench.action.terminal.kill",
            "when": "terminalFocus"
        },
        
        {
            "key": "ctrl+f7",
            "command": "workbench.action.toggleMaximizedPanel",
            "when": "terminalFocus"
        }
    ]

`remote-ssh <https://code.visualstudio.com/docs/remote/ssh>`_

web
----------

`mdn <https://developer.mozilla.org/en-US/>`_

`bootstrap <https://getbootstrap.com/>`_

`react <https://create-react-app.dev/>`_

`echarts <https://echarts.apache.org/en/index.html>`_

`chartjs <https://www.chartjs.org/>`_

windows
----------

`Susbsys for linux <https://docs.microsoft.com/en-us/windows/wsl/install#install>`_

Access from files explorer:

.. code-block:: text
    \\wsl$
    \\wsl$\Ubuntu\home\user

Access wsl from cmd:

.. code-block:: text

    wsl
    cd ~

Access file explorer, edge from wsl:

.. code-block:: text

    explorer.exe .
    wslview index.html

Move files:

.. code-block:: console

    cp /mnt/c/Users/user/{file} ~/{file}

wsl python installation:

.. code-block:: console

    sudo apt install python3.9 python3-pip       
    sudo apt install python3-dev python3.9-dev

    #remap python symlink
    cd /usr/bin/
    sudo unlink python
    sudo unlink python3
    sudo ln -s python3.9 /usr/bin/python
    sudo ln -s python3.9 /usr/bin/python3

    #check pip
    cd /usr/bin/
    code pip

    #add python path to .bashrc
    code .bashrc
    export PATH=”$PATH:/home/{your_linux_username}/.local/bin”
    
    python3.9 -m pip install -U pip

    pip install numpy
    pip install pandas
    pip install sklearn
    pip install seaborn
    
    pip install sqlalchemy
    
    sudo apt install postgresql
    sudo apt install libpq-dev
    pip install psycopg2

`Choco <https://chocolatey.org/install#individual>`_

`libre office <https://www.libreoffice.org/download/download/>`_

`windows off screen <https://www.alphr.com/find-recover-off-screen-window-windows-10/>`_

Add program to startmenu:

.. code-block:: text

    %ProgramData%\Microsoft\Windows\Start Menu\Programs
    %AppData%\Microsoft\Windows\Start Menu\Programs


