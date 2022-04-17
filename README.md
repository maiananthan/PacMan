# PacMan

## Windows Setup

- Checkout the code
- Install python3.8
- Install pip dependencies from `requirements.txt`
    - for Windows, run `.\setup.ps1` to install pycurl library
- To build the executable using  pyinstaller
``` powershell
pyinstaller --onefile .\PacMan.py .\commands\__init__.py .\commands\add.py .\commands\color.py .\commands\config.py .\commands\create.py .\commands\display.py .\commands\remove.py .\commands\update.py .\commands\upgrade.py
```
- After successfull build, find executable in `dist` folder