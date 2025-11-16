===============
contents
===============

* `quick setup`_
* `sd card, ssd`_
* `SSH`_
* `headless`_
* `install python from source`_
* `python packages`_
* `python projects`_
* `Anti-virus`_
* `pi os and running status`_

quick setup
-----------------------

::

    #ssh, vnc
    sudo apt update
    sudo apt install realvnc-vnc-server realvnc-vnc-viewer

    #config -> interface option -> enable ssh, vnc
    #config -> change password
    #config -> network -> hostname
    sudo raspi-config

    #find out ether, setup static lease
    ifconfig

anti virus::

    sudo apt install clamav
    sudo nano /root/scanvirus.sh

::

    #!/bin/bash
    LOGNAME="/var/log/clamav/clamav-$(date +'%Y-%m-%d').log";
    DIRTOSCAN="/home";
    
    clamscan -ri "$DIRTOSCAN" &>"$LOGNAME";

::

    sudo crontab -e
    0 0 * * * bash /root/scanvirus.sh

git::

    ssh-keygen -t ed25519 -C "your_email@example.com"
    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519
    #Add the SSH public key to your account on GitHub
    cat ~/.ssh/id_ed25519.pub

    git config --global pull.rebase false
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"


sd card, ssd
-------------

`imaging <https://www.raspberrypi.com/software/>`_

advanced options: ctrl+shift+x

`sd card <https://www.pcguide.com/raspberry-pi/guide/best-sd-card/>`_

usb:

`boot from usb <https://www.pragmaticlinux.com/2021/12/directly-boot-your-raspberry-pi-4-from-a-usb-drive/>`_

`boot from usb config <https://jamesachambers.com/raspberry-pi-4-usb-boot-config-guide-for-ssd-flash-drives/>`_

`fix boot from usb issue <https://www.pragmaticlinux.com/2021/03/fix-for-getting-your-ssd-working-via-usb-3-on-your-raspberry-pi/>`_


SSH
------

Install vnc server:

`official doco vnc server <https://www.raspberrypi.com/documentation/computers/remote-access.html#vnc>`_

Setups: Static lease, ssh, and other ways

`tute of various ways <https://www.thesecmaster.com/five-easiest-ways-to-connect-raspberry-pi-remotely-in-2021/>`_

Various topics:

`putty <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_

`check system arch <https://www.tenforums.com/tutorials/176966-how-check-if-processor-32-bit-64-bit-arm-windows-10-a.html>`_

`vnc <https://raspberrytips.com/use-vnc-raspberry-pi/#:~:text=If%20you%20can%20get%20access%20to%20the%20desktop,done%2C%20click%20on%20%E2%80%9COK%E2%80%9D%20to%20apply%20the%20changes.>`_

`password <https://tutorials-raspberrypi.com/raspberry-pi-default-login-password/>`_

`transfer files <https://howchoo.com/pi/how-to-transfer-files-to-the-raspberry-pi>`_

`ssh from outside lan <https://forums.raspberrypi.com/viewtopic.php?t=20826>`_

`denyhosts <https://www.techrepublic.com/article/how-to-block-ssh-attacks-on-linux-with-denyhosts/amp/>`_


headless
----------------

.. code-block:: console

    cd boot
    touch ssh
    sudo nano wpa_supplicant.conf

::
    
    country=AU
    ctrl_interface=DIR=/var/run/wpa_supplicant
    GROUP=netdev
    update_config=1
    network={
        ssid="your_real_wifi_ssid"
        psk="your_real_password"
        key_mgmt=WPA-PSK
        scan_ssid=1
    }



install python from source
---------------------------

`install from zip <https://aruljohn.com/blog/python-raspberrypi/>`_

`debian install <https://bobcares.com/blog/how-to-install-python-3-9-on-debian-10/>`_

python packages
-----------------

.. code-block:: console

    pip install -U pip
    sudo apt-get install libatlas-base-dev
    python3 -m pip install -U pandas

    sudo apt install python3-dev
    sudo apt install libpq-dev
    pip install psycopg2
    pip install sqlalchemy

    pip install -U jinja2
    pip install streamlit

    pip install duckdb

    sudo apt install build-essential
    pip install Cython

    pip install --upgrade setuptools

packages only::

    pip install -U pandas
    pip install -U psycopg2
    pip install -U sqlalchemy
    pip install -U jinja2
    pip install -U streamlit
    pip install -U matplotlib
    pip install -U loguru
    pip install -U openpyxl


pyarrow issues
^^^^^^^^^^^^^^^^^^^^

Preload libatomic::

    nano ~/.bashrc
    #add to end of file
    export LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0

`cmake <https://lindevs.com/install-cmake-on-raspberry-pi/>`_

::
    
    sudo apt install -y cmake

`streamlit <https://discuss.streamlit.io/t/raspberry-pi-streamlit/2900/68>`_

`arrow installation issue <https://github.com/apache/arrow/issues/35470>`_

`build arrow <https://arrow.apache.org/docs/developers/python.html#python-development>`_

`check if 32 or 64 bit os <https://raspberrypi.stackexchange.com/questions/121938/how-can-i-see-raspberry-pi-os-version-32bit-or-64-bit>`_

python projects
-----------------

`long running scripts <https://www.tomshardware.com/how-to/run-long-running-scripts-raspberry-pi>`_ 

`physical project with python <https://realpython.com/python-raspberry-pi>`_ 

Anti-virus
------------------

`clamscan <https://pimylifeup.com/raspberry-pi-clamav/>`_

.. code-block:: console

    ls /var/log/clamav


pi os and running status
-----------------------------

`config <https://www.raspberrypi.com/documentation/computers/configuration.html>`_

`doco <https://www.raspberrypi.com/documentation/computers/os.html>`_

`upgrade os <https://raspberrytips.com/update-raspberry-pi-latest-version/>`_

`factory reset <https://raspians.com/how-to-reset-raspberry-pi/>`_

`temp monitor <https://raspberrytips.com/raspberry-pi-temperature/>`_

screen dim::

    sudo nano /etc/lightdm/lightdm.conf
    xserver-command=X -s 0 -dpms

.. code-block:: console

    echo check status
    cat /etc/os-release
    vcgencmd measure_temp
    free -m
    df -h
    cat /proc/cpuinfo
    cat /proc/meminfo
    top
    htop
    
    echo config
    sudo raspi-config

    echo update upgrade
    sudo apt update
    sudo apt upgrade
    echo sudo apt full-upgrade

`reboot <https://jamesjdavis.medium.com/how-to-restart-raspberry-pi-safely-and-quickly-488243907fa3>`_

shutdown::

    sudo poweroff
    sudo shutdown -h now
