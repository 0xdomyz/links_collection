---------------------
table-of-contents
---------------------

* `book`_
* `C`_
* `C++`_
* `C sharp`_
* `Chrome extension`_
* `Cloud`_
* `configs`_
* `Container`_
* `Databases`_
* `Docos`_
* `Emails`_
* `ffmpeg`_
* `Image`_
* `julia`_
* `linux`_
* `Other`_
* `Process manager`_
* `R Program`_
* `Rust`_
* `regexp`_
* `sas`_
* `sdelete, winfr, diskpart`_
* `shell`_
* `ssh`_
* `style`_
* `vim`_
* `virtual mach`_
* `visual studio`_
* `web`_
* `windows`_
* `wsl`_

book
------

`clean <https://github.com/sdcuike/Clean-Code-Collection-Books/blob/master/Clean%20Architecture%20A%20Craftsman's%20Guide%20to%20Software%20Structure%20and%20Design.pdf>`_

`cs50 <https://github.com/0xdomyz/cs50>`_

`free prog books <https://github.com/EbookFoundation/free-programming-books>`_

`lisp <https://norvig.com/lispy.html>`_

`pragmatic2 <https://ebin.pub/the-pragmatic-programmer-your-journey-to-mastery-second-edition-20th-anniversary-edition-9780135957059-0135957052.html>`_

`SICP <https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-4.html#%_toc_start>`_

C
---

`the c book <https://publications.gbdirect.co.uk/c_book/>`_

`vscode tute mingw <https://code.visualstudio.com/docs/cpp/config-mingw>`_

`vscode tute wsl <https://code.visualstudio.com/docs/cpp/config-wsl>`_

`a course <https://www.freecodecamp.org/news/learn-c-with-free-31-hour-course/>`_

C++
-------

`c++ ref <https://en.cppreference.com/w/>`_

`zeromq <https://zeromq.org/>`_

`sfml <https://www.sfml-dev.org/tutorials/2.5/start-linux.php>`_

`sfml wsl <https://en.sfml-dev.org/forums/index.php?topic=28293.0>`_

`websocket <https://github.com/zaphoyd/websocketpp>`_

`async <https://solarianprogrammer.com/2012/10/17/cpp-11-async-tutorial/>`_

`sigcpp <https://sigcpp.github.io/>`_

C sharp
------------

`C# fundamental <https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/tutorials/how-to-display-command-line-arguments>`_

`C# doco <https://learn.microsoft.com/en-us/dotnet/csharp/>`_

`vscode C# <https://code.visualstudio.com/docs/csharp/get-started>`_

books:

`headfirst <https://www.amazon.com.au/dp/1491976705?tag=guru99-22&geniuslink=true>`_

`oneday <https://www.amazon.com.au/dp/B016Z18MLG?tag=guru99-22&geniuslink=true>`_

Chrome extension
-----------------

`Doco <https://developer.chrome.com/docs/extensions/mv3/>`_

`Examples <https://github.com/GoogleChrome/chrome-extensions-samples>`_

Cloud
--------

`example <https://gp2mv3.com/python-script-cloud-every-minute-for-free-with-aws-lambda/>`_

`acg aws path developer <https://learn.acloud.guru/learning-path/aws-developer>`_

`acg aws path data <https://learn.acloud.guru/learning-path/aws-data>`_

`acg aws path mach learn <https://learn.acloud.guru/learning-path/aws-ml>`_

`aws console <https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1#>`_

`aws getting started <https://aws.amazon.com/getting-started>`_

`aws hands-on <https://aws.amazon.com/getting-started/hands-on>`_

`aws hands-on sagemaker <https://aws.amazon.com/getting-started/hands-on/build-train-deploy-machine-learning-model-sagemaker/>`_

`aws deepdives <https://aws.amazon.com/getting-started/deep-dive-databases/>`_

configs
-----------
`toml <https://github.com/toml-lang/toml>`_

`yaml tute <https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html>`_

`yaml org <https://yaml.org/>`_

`pyyaml <https://pyyaml.org/wiki/PyYAMLDocumentation>`_

Container
---------------

`docker installation on ubuntu <https://docs.docker.com/engine/install/ubuntu>`_

::

    sudo service --status-all 
    sudo service docker start

`docker cheat sheet <https://github.com/wsargent/docker-cheat-sheet>`_

`acg docker <https://learn.acloud.guru/search?topics%5B0%5D=Containers&cloudProviders%5B0%5D=Docker>`_

`acg docker quick start <https://learn.acloud.guru/course/da6947b1-0901-4f60-a045-c15ec895a3d9>`_

`aws deep dive containers <https://aws.amazon.com/getting-started/deep-dive-containers/>`_

Databases
------------

`windows postgres, oracle xe <https://dwopt.readthedocs.io/en/stable/set_up.html#dwopt.make_test_tbl>`_

`start stop oracle xe <https://docs.oracle.com/en/database/oracle/oracle-database/21/xeinw/starting-and-stopping-oracle-database-xe.html>`_

postgre on raspbery pi:

.. code-block:: console

    sudo apt install postgresql

    sudo nano /etc/postgresql/13/main/pg_hba.conf
    # change "local" is for Unix domain socket connections only method to md5

    sudo pg_ctlcluster 13 main start

postgre on wsl:

.. code-block:: console

    sudo apt install postgresql

    sudo service postgresql restart

    sudo nano /etc/postgresql/12/main/pg_hba.conf
    # change "local" is for Unix domain socket connections only method to md5

    sudo pg_ctlcluster 12 main start

postgre set up db::

    sudo su postgres
    psql
    CREATE DATABASE test_db;
    CREATE USER test_db_user WITH PASSWORD '1234';
    GRANT ALL PRIVILEGES ON DATABASE test_db to test_db_user;
    \q
    exit

postgre::

    psql test_db test_db_user
    help
    
    sudo -u postgres psql
    \l
    \dt

`postgre backup <http://web.archive.org/web/20141108210658/http://www.brownfort.com/2014/10/backup-restore-postgresql/>`_

postgre backup restore::

    pg_dump -h localhost -p 5432 -U postgres -d mydb > backup.sql
    psql -h localhost -p 5432 -U postgres -d mydb < backup.sql

`teradata clearscape <https://www.teradata.com/getting-started/demos/clearscape-analytics>`_

teradata via sqlalchemy::

    pip install teradatasqlalchemy

Docos
-----------

`markdown land cheat sheet <https://markdown.land/markdown-cheat-sheet>`_

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

ffmpeg
------------

`wiki <https://trac.ffmpeg.org/wiki>`_

`capture screen/sound <https://trac.ffmpeg.org/wiki/Capture/Desktop>`_

`stero mix <https://www.howtogeek.com/39532/how-to-enable-stereo-mix-in-windows-7-to-record-audio/>`_

`direct show <https://trac.ffmpeg.org/wiki/DirectShow>`_

commands::

    #capture sound on windows
    ffmpeg -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" aaa.mp3

    #modify volume
    ffmpeg -i input.wav -filter:a "volume=1.5" output.wav
    ffmpeg -i input.mp3 -filter:a "volume=0.8" output.mp3

    #cut end
    ffmpeg -i "audio.mp3" 2>&1 | grep "Duration" | cut -d " " -f 4
    ffmpeg -i "audio.mp3" -acodec mp3 -t 100 "audio_cut.mp3"
    ffmpeg -i "audio.mp3" -acodec mp3 -ss 10 -t 100 "audio_cut.mp3"

    #cut to pieces
    ffmpeg -i "input_audio_file.mp3" -f segment -segment_time 3600 -c copy output_audio_file_%03d.mp3

Image
---------

downsample a picture::

    sudo apt install graphicsmagick-imagemagick-compat
    convert input.jpg -resize 30% output.jpg
    # alternatively use imagemagick-6.q16, imagemagick-6.q16hdri

julia
--------

`install <https://julialang.org/downloads/>`_

`IJulia <https://github.com/JuliaLang/IJulia.jl#quick-start>`_

`course <https://juliaacademy.com/courses/intro-to-julia>`_

`doco <https://docs.julialang.org/en/v1/>`_

linux
-------

`crontab <https://www.adminschoice.com/crontab-quick-reference>`_

`crontab generator <https://crontab-generator.org/>`_

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


`qtorrent <https://www.qbittorrent.org/>`_

Process manager
------------------

To use systemd to manage a Python script, you will need to use the following commands::

    systemctl enable
    systemctl start
    systemctl stop
    systemctl restart
    systemctl status
    journalctl -u
    journalctl -f

`journalctl sizes <https://ngelinux.com/check-journalctl-log-size-and-archive-delete-old-logs/#:~:text=Check%20Journalctl%20Log%20size%20and%20archive%2Fdelete%20old%20logs.,Limiting%20the%20journal%20usage%20using%20below%204%20options.>`_

`systemd manage streamlit <https://fuzzyblog.io/blog/python/2019/11/13/making-a-streamlit-machine-learning-app-into-a-systemd-service.html>`_

R Program
-----------

`r project <https://cloud.r-project.org/>`_

`rstudio <https://www.rstudio.com/products/rstudio/download/#download>`_

`tidyverse <https://www.tidyverse.org/>`_

`dplyr <https://dplyr.tidyverse.org/articles/index.html>`_

`cheatsheets <https://www.rstudio.com/resources/cheatsheets/>`_

`graphic cookbook <https://r-graphics.org/recipe-quick-line>`_

`r4ds <https://r4ds.had.co.nz>`_

`reg weigths <https://alvaroaguado3.github.io/forcing-regression-coefficients-in-r-part-i/>`_

`R kernel for jupyter <https://www.rdocumentation.org/packages/IRkernel>`_:: 

    install.packages("devtools")
    devtools::install_github("IRkernel/IRkernel")
    IRkernel::installspec()

Rust
----------

`rust book <https://doc.rust-lang.org/book/ch00-00-introduction.html>`_

`rustlings <https://github.com/rust-lang/rustlings/>`_

`rust by examples <https://doc.rust-lang.org/stable/rust-by-example/>`_

`rust zeromq <https://github.com/erickt/rust-zmq>`_

regexp
-----------

`spec <https://www.regular-expressions.info/>`_

sas
--------------

`vscodd extn <https://marketplace.visualstudio.com/items?itemName=SAS.sas-lsp>`_

`videos <https://video.sas.com/category/videos/sas-studio>`_

`online studio <https://welcome.oda.sas.com/>`_

sdelete, winfr, diskpart
--------------------------

`sysinternals <https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete>`_

::

    # map to path

    # clean up space
    sdelete64 -p 3 -c c:
    sdelete64 -p 3 -c d:
    sdelete64 -p 3 -c e:

    #delete all files in a folder
    sdelete64 -p 3 -r -s "New folder\*"

`winfr <https://au.pcmag.com/windows-xp/68079/how-to-recover-deleted-files-in-windows-10>`_

::

    # recover files
    winfr C: E:\RecoveryDestination /extensive /n "Users\<username>\Downloads\*.pdf" /n "Users\<username>\Downloads\*.png"
    winfr C: E:\Recovery /regular /n "Users\User\Downloads\*"


`diskpart <https://www.tomshardware.com/how-to/secure-erase-ssd-or-hard-drive>`_

shell
-------

`shell collection <https://github.com/0xdomyz/shell_collection>`_

ssh
---------

`ssh tips from visual studio <https://code.visualstudio.com/docs/remote/troubleshooting#_ssh-tips>`_

example ssh setup::

    #generate and copy
    ssh-keygen -t rsa -b 4096 -C "your_email@exmaple.com"
    #alternatively with diff locations
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f "C:/path/to/your/directory/id_rsa"
    
    # optionally, use ssh-agent to manage passcodes and more
    # ssh-agent is a program to hold private keys used for public key authentication
    eval "$(ssh-agent -s)" # start the ssh-agent in the background
    # Start-Service ssh-agent # windows powershell
    ssh-add ~/.ssh/id_rsa

    # if have ssh-copy-id
    ssh-copy-id user@hostname

    #alternatively, generate then paste into another system
    cat ~/.ssh/id_rsa.pub
    # manually add ssh pub key to remote
    nano ~/.ssh/authorized_keys
    # alternatively, vim
    vim ~/.ssh/authorized_keys
    # paste in, then :wq to save and exit

example ssh setup2::

    ssh-keygen -C {email} -f ~/.ssh/id_rsa_example
    cat ~/.ssh/id_rsa_example.pub

    ls -l ~/.ssh/id_rsa_example*
    cat ~/.ssh/id_rsa_example

    # use the -i option to specify the private key file-
    ssh -i ~/.ssh/id_rsa_example ec2-user@{numbers}.compute-1.amazonaws.com
    ssh -i ~/.ssh/id_rsa_example ec2-user@{ip}

style
-----------

`google style guides <https://google.github.io/styleguide/>`_

vim
---------

`tute <https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/table-of-contents>`_

`cheatsheet <https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/cheatsheet>`_

`set up for python <https://realpython.com/vim-and-python-a-match-made-in-heaven/>`_

virtual mach
----------------

`virtual mach soft <https://windowsreport.com/virtual-machine-software/>`_

`VMWare player <https://www.vmware.com/products/workstation-player.html>`_


visual studio
---------------

`c++ build tools <https://visualstudio.microsoft.com/visual-cpp-build-tools/>`_

web
----------

`mdn <https://developer.mozilla.org/en-US/>`_

`bootstrap <https://getbootstrap.com/>`_

`react <https://create-react-app.dev/>`_

`echarts <https://echarts.apache.org/en/index.html>`_

`chartjs <https://www.chartjs.org/>`_

windows
----------

`windows page <https://github.com/0xdomyz/links_collection/blob/master/windows.rst>`_

wsl
----------

`wsl page <https://github.com/0xdomyz/links_collection/blob/master/wsl.rst>`_


