# VS Code Usage

[VS Code for Windows](https://code.visualstudio.com/)

- [Kill terminal](https://stackoverflow.com/questions/50569100/vscode-how-to-make-ctrlk-kill-till-the-end-of-line-in-the-terminal)
- [Remote SSH](https://code.visualstudio.com/docs/remote/ssh)
- [C++ config doc](https://code.visualstudio.com/docs/cpp/c-cpp-properties-schema-reference)

**Developer:**

- Toggle developer tools, console

**Extensions:**

- remote development
- copilot
- python
- r
- c++
- rust-analyzer
- gitlens
- docker

[Example settings](https://github.com/0xdomyz/links_collection/blob/master/systems_set_up/vscode_settings.json)

## Preferences: Open Keyboard Shortcuts (JSON)

```json
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
			"value": 20
		},
		"when": "editorTextFocus"
	},
	{
		"key": "ctrl+NumPad0",
		"command": "cursorMove",
		"args": {
			"to": "down",
			"by": "line",
			"value": 20
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
	}
]
```

## VS Code Workspace Setting

```json
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
	]
}
```

## C++ Build Task

```json
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
```
