# RunNodeConsole
Simple plugin for Sublime Text 3 to run nodejs scripts


## To-Do

1. Add this to Package Manager
2. Add binding to the script on install
3. Instead of opening Nodejs everytime, find its Process ID, close it and re-run


## How to

1. Install:

	Put this script in a plugin directory

	Windows:
		"%APPDATA%\Sublime Text 3\Packages\_insert RunNodeConsole.py here_"

	Linux:
		$HOME/.config/sublime-text-3/Packages/_insert RunNodeConsole.py here_

	OSX:
		~/Library/Application\ Support/Sublime\ Text\ 3/Packages/_insert RunNodeConsole.py here_

2. Binding a key:

	I use F5. In ST3, press Preferences -> Key Bindings
	
	Put that line between brackets:

	```
		[
			{ "keys": ["f5"], "command": "run_node_console"}
		]
	```

3. Use it:
	
	.js file must be open to run. Press F5