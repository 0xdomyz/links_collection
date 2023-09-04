vscode
---------------

`windows <https://code.visualstudio.com/>`_

`kill terminal <https://stackoverflow.com/questions/50569100/vscode-how-to-make-ctrlk-kill-till-the-end-of-line-in-the-terminal>`_

`remote-ssh <https://code.visualstudio.com/docs/remote/ssh>`_

Developer: toggle developer tools, console

Extensions:

- remote development
- copilot
- python
- r
- c++
- rust-analyzer
- gitlens
- docker

preferences open user settings (json):

.. code-block:: json

    {
        "[python]": {
            "editor.defaultFormatter": "ms-python.black-formatter"
        },
        "editor.formatOnSave": true,
        "editor.inlineSuggest.enabled": true,
        "editor.insertSpaces": true,
        "editor.mouseWheelZoom": true,
        "editor.renderWhitespace": "all",
        "editor.rulers": [
            90
        ],
        "editor.stickyScroll.enabled": true,
        "editor.tabSize": 4,
        "explorer.confirmDelete": false,
        "explorer.confirmDragAndDrop": false,
        "git.confirmSync": false,
        "git.enableSmartCommit": true,
        "git.openRepositoryInParentFolders": "never",
        "github.copilot.enable": {
            "*": true,
            "plaintext": true,
            "markdown": false,
            "scminput": false
        },
        "gitlens.codeLens.enabled": false,
        "gitlens.currentLine.enabled": false,
        "gitlens.hovers.currentLine.over": "line",
        "remote.SSH.remotePlatform": {
            "192.168.0.251": "linux"
        },
        "security.workspace.trust.untrustedFiles": "open",
        "terminal.explorerKind": "external",
        "terminal.integrated.defaultProfile.windows": "Command Prompt",
        "terminal.integrated.enableMultiLinePasteWarning": false,
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
        "workbench.startupEditor": "none",
    }

Vscode shortcuts::

    ctrl + p # command palette
    ctrl + p > # settings
    ctrl + shift + p # settings
    ctrl + shift + . # find file
    ctrl + p @ # symbol
    ctrl + p {file name} # open file
    ctrl + p :{line number} # open file at line number
    shift + arrow # select
    ctrl + arrow # move cursor
    ctrl + d # select next
    ctrl + h # replace
    alt + click # select multiple
    ctrl + x # cut line
    alt + arrow # move line
    alt + shift + arrow # copy line
    ctrl + l # select line
    ctrl + / # comment line
    ctrl + \ # split
    ctrl + ` # toggle terminal
    ctrl + shift + p task # run task
    ctrl + shift + p snippet # insert snippet
    shift + alt + f12 # show all references
    right click, find all references, rename symbol

preferences open keyboard shortcuts (json):

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
        },
        {
            "key": "shift+alt+-",
            "command": "workbench.action.decreaseViewSize"
        },
        {
            "key": "shift+alt+=",
            "command": "workbench.action.increaseViewSize"
        },
        {
            "key": "ctrl+NumPad1",
            "command": "cursorMove",
            "args": {
                "to": "up",
                "by": "line",
                "value": 20,
            },
            "when": "editorTextFocus"
        },
        {
            "key": "ctrl+NumPad0",
            "command": "cursorMove",
            "args": {
                "to": "down",
                "by": "line",
                "value": 20,
            },
            "when": "editorTextFocus"
        },
        {
            "key": "ctrl+NumPad7",
            "command": "cursorMove",
            "args": {
                "to": "prevBlankLine"
            },
            "when": "editorTextFocus"
        },
        {
            "key": "ctrl+NumPad4",
            "command": "cursorMove",
            "args": {
                "to": "nextBlankLine"
            },
            "when": "editorTextFocus"
        },
    ]

vscode workspace setting:

.. code-block:: json

    {
        "[python]": {
            "editor.codeActionsOnSave": {
                "source.organizeImports": true
            }
        },
        "editor.formatOnSave": true,
        "python.formatting.provider": "black",
        "python.sortImports.args": [
            "--profile",
            "black"
        ],
    }

Cpp build task:

.. code-block:: json

    {
        "version": "2.0.0",
        "tasks": [
            {
                "type": "cppbuild",
                "label": "C/C++: g++ build active dir",
                "command": "/usr/bin/g++",
                "args": [
                    "-std=c++2a",
                    "-fdiagnostics-color=always",
                    "-g",
                    "${fileDirname}/*.cpp",
                    "-o",
                    "${fileDirname}/${fileBasenameNoExtension}"
                ],
                "options": {
                    "cwd": "${fileDirname}"
                },
                "problemMatcher": [
                    "$gcc"
                ],
                "group": "build",
                "detail": "compiler: /usr/bin/g++"
            }
        ]
    }
