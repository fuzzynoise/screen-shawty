# screen-shawty

 1. [Overview](#overview)
 2. [Change log](#change-log)
 3. [Install](#install)
 4. [Running it](#running-it)
 5. [Troubles with the app](#troubles-with-the-app)

### Overview
My girlfriend got a video game during a certain summer sale. Unfortunately, the game has no built-in screenshot feature. Using print screen and pasting the contents of the clipboard into an image editor is not convenient for her. Hence, screen-shawty.
### Change log
0.01b

 - Beta version now available.
 - Added error handling for non-existent `~/Pictures/` directory.
 - Changed shebang to use `env python3` for Linux.
 - Added anchor links to README.MD.

0.01a
 - Alpha version now available.
 - Published the minimum viable product.
 - Added a README.MD.
 - Added a LICENSE (MIT).

### Install
You will need to have Python3 installed. It will be helpful to have pip installed as well.
```
git clone https://github.com/fuzzynoise/screen-shawty.git
cd screen-shawty
pip install --user -r requirements.txt
```
### Running it
Either double-click the screen-shawty.py file or run it from CLI with
```
python screen-shawty.py
```
Once the application is running, press the green "Start" button to begin the recording. To take a screenshot, press the print screen key on your keyboard as normal. Images will be automatically saved to `~/Pictures/Screen Shot TIMESTAMP.png` (where `~` represents your home directory). To stop the application and return print screen key function to normal, press the red "Stop" button.
### Troubles with the app
I do plan on adding some error handling at some point but this is a pretty low priority project. If you have some difficulty but are not my girlfriend, do not expect any assistance. Bug fixes are certainly a welcome contribution though.
