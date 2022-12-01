vscode
---------------

`windows <https://code.visualstudio.com/>`_

`kill terminal <https://stackoverflow.com/questions/50569100/vscode-how-to-make-ctrlk-kill-till-the-end-of-line-in-the-terminal>`_

`remote-ssh <https://code.visualstudio.com/docs/remote/ssh>`_

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