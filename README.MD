# screen-shawty

### Overview
My girlfriend got a video game during a certain summer sale. Unfortunately, the game has no built-in screenshot feature. Using print screen and pasting the contents of the clipboard into an image editor is not convenient for her. Hence, screen-shawty.
### Install
```
git clone https://github.com/fuzzynoise/screen-shawty.git
cd screen-shawty
pip install --user -r requirements.txt
```
### Running it
Either double-click the screen-shawty.py file or run it from CLI with
```
python screen-shawty
```
Once the application is running, press the "Start" button to begin the recording. To take a screenshot, press the print screen key on your keyboard as normal. Currently, images will be automatically saved to `~/Pictures/Screen Shot TIMESTAMP.png` (where `~` represents your home directory).
### Troubles with the app
I do plan on adding some error handling at some point but this is a pretty low priority project. If you have some difficulty but are not my girlfriend, do not expect any assistance. Bug fixes are certainly a welcome contribution, however.
