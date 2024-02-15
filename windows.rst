.. ---------------------
.. table-of-contents
.. ---------------------

windows
-------------

terminal screen buffer size::

    properties -> layout -> screen buffer size height 9000

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

wsl python installation:

.. code-block:: console

    sudo apt install python3.11
    sudo apt install python3-pip
    sudo apt install python3-dev
    sudo apt-get install python3-tk 

    python3.11 -m pip install -U pip

    python3.11 -m pip install numpy
    python3.11 -m pip install pandas
    python3.11 -m pip install scikit-learn
    python3.11 -m pip install seaborn
    
    python3.11 -m pip install sqlalchemy
    
    sudo apt install postgresql
    sudo apt install libpq-dev
    sudo apt-get install libatlas-base-dev
    #python3.11 -m pip install psycopg2
    python3.11 -m pip install psycopg2-binary

    python3.11 -m pip install Cython

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

`Choco <https://chocolatey.org/install#individual>`_

`libre office <https://www.libreoffice.org/download/download/>`_

.. code-block:: text

    alt + o + m + o: fit column to size
    alt + s + s + a: new sheet

`windows off screen <https://www.alphr.com/find-recover-off-screen-window-windows-10/>`_

`edge shortcuts <https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad>`_

`add to startup <https://support.microsoft.com/en-us/windows/add-an-app-to-run-automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd>`_

Add program to startmenu:

.. code-block:: text

    #coputer wide
    %ProgramData%\Microsoft\Windows\Start Menu\Programs
    #user
    %AppData%\Microsoft\Windows\Start Menu\Programs

    #apps
    shell:appsfolder

Alt desktop::

    WIN + CTRL + LEFT/RIGHT: Switch to the previous or next desktop.
    WIN + CTRL + D: Create a new desktop.
    WIN + CTRL + F4: Close the current desktop.

`unc path <https://stackoverflow.com/questions/21482825/find-unc-path-of-a-network-drive>`_

powershell scipt/addon::

    #allow script to run
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

    # auto compltete
    Install-Module PSReadLine -Force
    Set-PSReadLineOption -PredictionSource History
    Set-PSReadLineOption -PredictionViewStyle ListView
    
windows terminal

`tute <https://www.hanselman.com/blog/my-ultimate-powershell-prompt-with-oh-my-posh-and-the-windows-terminal>`_

shortcuts for Windows Terminal::

    Ctrl + Shift + T: Open a new tab with the default profile.
    Ctrl + Shift + W: Close the current tab.
    Ctrl + Tab: Switch to the next tab.
    Ctrl + Shift + Tab: Switch to the previous tab.
    Ctrl + Shift + D: Split the pane vertically.
    Ctrl + Shift + Right Arrow: Resize pane to the right.
    Ctrl + Shift + Left Arrow: Resize pane to the left.
    Ctrl + Shift + Up Arrow: Resize pane up.
    Ctrl + Shift + Down Arrow: Resize pane down.
    Alt + Shift + D: Split the pane horizontally.
    Ctrl + Shift + Space: Open the command palette.
    Ctrl + Shift + 1 through Ctrl + Shift + 9: Open a new tab with the profile corresponding to the number.

