.. ---------------------
.. table-of-contents
.. ---------------------

terminal screen buffer size::

    properties -> layout -> screen buffer size height 9000

`Choco <https://chocolatey.org/install#individual>`_

`libre office <https://www.libreoffice.org/download/download/>`_

.. code-block:: text

    alt + o + m + o: fit column to size
    alt + s + s + a: new sheet

`windows off screen <https://www.alphr.com/find-recover-off-screen-window-windows-10/>`_

`close excel right panel <https://answers.microsoft.com/en-us/msoffice/forum/msoffice_excel-msoffice_unknown-mso_subother/keyboard-shortcuts-for-moving-between-application/11dd8df2-ff0a-4a05-95f5-4ebe181661ad?messageId=8e404492-4d86-49bd-b064-ef04d675d33b>`_

`edge shortcuts <https://support.microsoft.com/en-us/microsoft-edge/keyboard-shortcuts-in-microsoft-edge-50d3edab-30d9-c7e4-21ce-37fe2713cfad>`_

`prtsc key <https://www.msn.com/en-us/news/technology/a-useless-button-no-way-print-screen-on-your-keyboard-actually-does-a-lot/ar-BB1hqywD>`_

Add program to startmenu:

.. code-block:: text

    #coputer wide
    %ProgramData%\Microsoft\Windows\Start Menu\Programs
    #user
    %AppData%\Microsoft\Windows\Start Menu\Programs

    #apps
    shell:appsfolder # then make shortcut then drag to startmenu folder

`add to startup <https://support.microsoft.com/en-us/windows/add-an-app-to-run-automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd>`_

Alt desktop::

    WIN + CTRL + LEFT/RIGHT: Switch to the previous or next desktop.
    WIN + CTRL + D: Create a new desktop.
    WIN + CTRL + F4: Close the current desktop.

`unc path <https://stackoverflow.com/questions/21482825/find-unc-path-of-a-network-drive>`_

powershell scipt/addon::

    #allow script to run
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

    #profile
    code $PROFILE

    #icon color
    Import-Module -Name Terminal-Icons

    # auto compltete
    Install-Module PSReadLine -Force
    # in profile
    Set-PSReadLineOption -PredictionSource History
    Set-PSReadLineOption -PredictionViewStyle ListView

windows terminal

`terminal tute <https://www.hanselman.com/blog/my-ultimate-powershell-prompt-with-oh-my-posh-and-the-windows-terminal>`_

`zsh tute <https://github.com/christianlempa/videos/tree/main/windows-terminal-powerlevel10k>`_

`ohmyposh <https://ohmyposh.dev/docs>`_

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


