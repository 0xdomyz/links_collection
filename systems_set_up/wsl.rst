.. ---------------------
.. table-of-contents
.. ---------------------

`Susbsys for linux <https://docs.microsoft.com/en-us/windows/wsl/install#install>`_

`best practise on environment and other softs on wsl <https://learn.microsoft.com/en-us/windows/wsl/setup/environment>`_

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
    
    ls /mnt/d/

`wsl gui <https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242>`_

`wsl sound <https://www.linuxuprising.com/2021/03/how-to-get-sound-pulseaudio-to-work-on.html>`_

`wsl sound 2 <https://github.com/microsoft/WSL/issues/5816>`_

`wsl sound 3 <https://discourse.ubuntu.com/t/getting-sound-to-work-on-wsl2/11869/8>`_

`wsl bashrc pgsql start <https://www.wanzul.net/2021/07/03/making-postgresql-run-on-first-start-of-wsl-2-terminal/>`_

wsl start pgsql::

     sudo service postgresql status > /dev/null || sudo service postgresql start

wsl python path:

.. code-block:: console

    #remap python symlink, this breaks apt-get
    cd /usr/bin/
    sudo unlink python
    sudo unlink python3
    sudo ln -s python3.9 /usr/bin/python
    sudo ln -s python3.9 /usr/bin/python3

    #update-alternatives
    #map alt python to path

    #add python path to .bashrc
    code .bashrc
    export PATH=”$PATH:/home/{your_linux_username}/.local/bin”

list of chmods::

    # 777: read, write, and execute access for everyone
    chmod 777 -R ~/folder # -R recursive
    # 755: read and execute access for everyone, write access for the owner
    chmod 755 ~/folder 
    # 700: read, write, and execute access for the owner, no access for everyone else
    chmod 700 ~/folder
    # 400: read access for the owner, no access for everyone else
    chmod 400 ~/folder
