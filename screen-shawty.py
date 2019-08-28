#!/usr/bin/env python3

#################
r'''eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
S           .'|                     _     _   .-.          .-
 C         <  |               /\    \\   //  .|\ \        / /
  R         | |             __`\\  //\\ // .' |_\ \      / /
   e     _  | | .'--.   .:--.'.\`//  \'/.'     |\ \    / /
    e .' |  | |/.'-. \ / |   \ |\|   |/'--.  .-' \ \  / /
    .N  | /|  /    | | `" __ | | '        |  |    \ `  /
  .'.'| |//| |     | |  .'.''| |          |  |     \  /
.'.'.-'  / | |     | | / /   | |_         |  '.'   / /
.'   \_.'  | '.    | '.\ \._,\ '/         |   /|`-' /
           '---'   '---'`--'  `"          `'-'  '..'''
#################
import tkinter as tk
import keyboard

from sys import platform
from time import time
from time import sleep
from pathlib import Path

# This is hacky, but has to be done to handle display scaling
# This should be handled upstream by PIL
# It also may need to be called BEFORE the import of PIL.ImageGrab
if platform == 'win32':
    from ctypes import windll
    user32 = windll.user32
    user32.SetProcessDPIAware()

from PIL import ImageGrab

#################

'''
Takes a Path object or defaults to a file named sshawty.conf
in the same directory as the application. Parses the file and
sets button color, save path, locale/language and that kinda junk.
'''
def parse_config(config = Path('./sshawty.conf')):
    config = config
    if config.exists():
        pass
    else:
        try:
            config.mkdir(parents = True, exist_ok = True)
        except Exception as e:
            print(e)

def start_stop(ON = 'green', OFF = 'red'):
    global is_running

    if toggle_button['text'] == 'Start':
        is_running = True
        toggle_button.config(text = "Stop", bg = OFF)
    else:
        is_running = False
        toggle_button.config(text = "Start", bg = ON)

def take_screen_shot():
    # time() returns a float, but we need to use it in a filename
    current_time = str(time()).replace('.','_')

    # Literally ~/Pictures/
    picture_dir = Path.home().joinpath('Pictures')

    # State of the art error handling!
    if not picture_dir.exists():
        try:
            picture_dir.mkdir(parents = True, exist_ok = True)
        except Exception as e:
            print(e) #TODO: implement logging module

    save_path = picture_dir.joinpath(f'Screen Shot {current_time}.png')

    screen_shot = ImageGrab.grab()
    screen_shot.save(save_path)

    # We sleep here to allow user to release print screen
    sleep(0.2)

def shot_loop():
    if is_running:
        if keyboard.is_pressed('print screen'):
            take_screen_shot()
    main_frame.after(POLL_DELAY, shot_loop)

#################

VERSION = '0.2' # TODO: __init__
POLL_DELAY = 150 # ~6.66 polls for keyboard per second.
HEIGHT = 350
WIDTH = 350

is_running = False # Is the app polling keyboard input?


main_frame = tk.Tk()

main_frame.title(f"screen-shawty {VERSION}")
main_frame.geometry(f"{WIDTH}x{HEIGHT}")

app = tk.Frame(main_frame)
app.pack(expand = True, fill = 'both')

toggle_button = tk.Button(
    app, text = "Start", bg = 'green',
    font = (1), command = start_stop)

toggle_button.pack(expand = True, fill = 'both')

main_frame.after(POLL_DELAY, shot_loop)
main_frame.mainloop()
