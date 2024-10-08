vscode
---------------

`windows <https://code.visualstudio.com/>`_

`kill terminal <https://stackoverflow.com/questions/50569100/vscode-how-to-make-ctrlk-kill-till-the-end-of-line-in-the-terminal>`_

`remote-ssh <https://code.visualstudio.com/docs/remote/ssh>`_

`cpp config doco <https://code.visualstudio.com/docs/cpp/c-cpp-properties-schema-reference>`_

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

`example settings <https://github.com/0xdomyz/links_collection/blob/master/vscode_settings.json>`_

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
    ctrl + shift + - # split editor
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
