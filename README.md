# bd2gps
坐标转换工具 PyQt界面封装

# build
## python2 + PyQt4
```sh
py -3 -m venv .venv
.venv\Scripts\activate.bat
```

install PyQt4, PyInstaller

```sh
pyuic4 ui_main.ui -o ui_main4.py
pyinstaller bd2gps.py -w -i app.ico --add-data "app.ico;."
```

## python3 + PyQt5
```
py -3 -m venv .venv
.venv\Scripts\activate.bat
pip install -r requestments.txt
pyuic5 ui_main.ui -o ui_main5.py
python cx_freeze.py build
```

#转换算法
https://github.com/wandergis/coordTransform_py

# PyInstaller command
```
pyinstaller bd2gps.py --icon app.ico --no-console --add-data "app.ico;."
```
