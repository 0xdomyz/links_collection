pi os
----------

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

sd card, ssd
-------------

`imaging <https://www.raspberrypi.com/software/>`_

`sd card <https://www.pcguide.com/raspberry-pi/guide/best-sd-card/>`_

`boot from usb <https://www.pragmaticlinux.com/2021/12/directly-boot-your-raspberry-pi-4-from-a-usb-drive/>`_

`boot from usb config <https://jamesachambers.com/raspberry-pi-4-usb-boot-config-guide-for-ssd-flash-drives/>`_

`fix boot from usb issue <https://www.pragmaticlinux.com/2021/03/fix-for-getting-your-ssd-working-via-usb-3-on-your-raspberry-pi/>`_

SSH
------

`doco <https://www.raspberrypi.com/documentation/computers/remote-access.html#vnc>`_

`tute <https://www.thesecmaster.com/five-easiest-ways-to-connect-raspberry-pi-remotely-in-2021/>`_

`processor <https://winaero.com/check-if-processor-is-32-bit-64-bit-or-arm-in-windows-10/>`_

`putty <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_

`vnc <https://raspberrytips.com/use-vnc-raspberry-pi/#:~:text=If%20you%20can%20get%20access%20to%20the%20desktop,done%2C%20click%20on%20%E2%80%9COK%E2%80%9D%20to%20apply%20the%20changes.>`_

`password <https://tutorials-raspberrypi.com/raspberry-pi-default-login-password/>`_

`transfer files <https://howchoo.com/pi/how-to-transfer-files-to-the-raspberry-pi>`_

`ssh from outside lan <https://forums.raspberrypi.com/viewtopic.php?t=20826>`_

`denyhosts <https://www.techrepublic.com/article/how-to-block-ssh-attacks-on-linux-with-denyhosts/amp/>`_

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

Preload libatomic::

    nano ~/.bashrc
    #add to end of file
    export LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0

`cmake <https://lindevs.com/install-cmake-on-raspberry-pi/>`_

::
    
    sudo apt install -y cmake

`streamlit <https://discuss.streamlit.io/t/raspberry-pi-streamlit/2900/68>`_

python projects
-----------------

`long running scripts <https://www.tomshardware.com/how-to/run-long-running-scripts-raspberry-pi>`_ 

`physical project with python <https://realpython.com/python-raspberry-pi>`_ 

Anti-virus
------------------

`clamscan <https://pimylifeup.com/raspberry-pi-clamav/>`_

.. code-block:: console

    ls /var/log/clamav

