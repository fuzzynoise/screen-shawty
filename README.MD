# screen-shawty
 1. [Overview](#overview)
 2. [Change log](CHANGES.MD)
 3. [Install](#install)
 4. [Running it](#running-it)
 5. [Known Bugs](#known-bugs)
 6. [Troubles with the app](#troubles-with-the-app)
### Overview
My girlfriend got a video game during a certain summer sale. Unfortunately, the game has no built-in screenshot feature. Using print screen and pasting the contents of the clipboard into an image editor is not convenient for her. Hence, screen-shawty.

As it turns out, this works well for instant local capture of screenshots of
any application that does not have this built-in functionality.

[Return to top](#screen-shawty)
### Install

#### Windows
  - Download the [Windows .exe file](https://github.com/fuzzynoise/screen-shawty/raw/master/screen-shawty.exe)
  - Scan the file for malware using the right-click context menu in Windows.
  - Verify it?
```
> Get-FileHash .\screen-shawty.exe -Algorithm SHA256 | Select-Object Hash

Hash
----
9E97652FED28AF69CA2F4F25E52782C493C06FEA696D72D48695A6D215D76DAC
```
  - Try it out.
#### Unix-like / Developers
You will need to have Python3 installed. It will be helpful to have pip installed as well.
```
git clone https://github.com/fuzzynoise/screen-shawty.git
cd screen-shawty
pip install --user -r requirements.txt
```
If you want to build an exe, currently they're built for Windows using auto-py-to-exe and you can set that up with:
```
pip install auto-py-to-exe
auto-py-to-exe
```
[Return to top](#screen-shawty)
### Running it
Either double-click the executable/screen-shawty.py file or run it from CLI with
```
python screen-shawty.py
```
Once the application is running, press the green "Start" button to begin the recording. To take a screenshot, press the print screen key on your keyboard as normal. Images will be automatically saved to `~/Pictures/Screen Shot TIMESTAMP.png` (where `~` represents your home directory). To stop the application and return print screen key function to normal, press the red "Stop" button.

[Return to top](#screen-shawty)
### Known bugs
  - Proper Linux is not supported yet.
  - When multiple displays are connected there can be some wonky behavior.
  - On Windows 10: display scaling can cause a partial ImageGrab. This can potentially happen with any display scale other than 100%. As a workaround try:
```
Go to the Windows Start Menu.
Choose Settings.
Select System.
Select Display.
Look for Scale and Layout.
Set it to 100%.
```
  - If you get a "Search for app in the Store" dialog on Windows10: press Yes or No. It doesn't seem to matter which you press, screen-shawty will still launch and function as expected.

[Return to top](#screen-shawty)
### Troubles with the app
I do plan on adding some error handling at some point but this is a pretty low priority project. If you have some difficulty but are not my girlfriend, do not expect any assistance. Bug fixes are certainly a welcome contribution though.

[Return to top](#screen-shawty)
