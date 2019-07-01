#!/usr/bin/env python3

#################
r'''
S           .'|                     _     _   .-.          .-
 C         <  |               /\    \\   //  .|\ \        / /
  R         | |             __`\\  //\\ // .' |_\ \      / /
   e     _  | | .'--.   .:--.'.\`//  \'/.'     |\ \    / /
    e .' |  | |/.'-. \ / |   \ |\|   |/'--.  .-' \ \  / /
    .N  | /|  /    | | `" __ | | '        |  |    \ `  /
  .'.'| |//| |     | |  .'.''| |          |  |     \  /
.'.'.-'  / | |     | | / /   | |_         |  '.'   / /
.'   \_.'  | '.    | '.\ \._,\ '/         |   /|`-' /
           '---'   '---'`--'  `"          `'-'  '..'
'''
#################

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
import tkinter as tk

#################

VERSION = '0.02b' # TODO: __init__
POLL_DELAY = 150 # ~6.66 polls for keyboard per second.
running = False # Is the application polling keyboard input?

#################

def start_stop():
    global running

    if toggle_button['text'] == 'Start':
        running = True
        toggle_button.config(text="Stop", bg='red')
    else:
        running = False
        toggle_button.config(text="Start", bg='green')

def take_screen_shot():
    # time() returns a float, but we need to use it in a filename
    current_time = str(time()).replace('.','_')

    # Literally ~/Pictures/ (we'll see if it exists later...)
    picture_dir = Path.home().joinpath('Pictures')

    # State of the art error handling!
    if not picture_dir.exists():
        try:
            picture_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(e) #TODO: implement logging module

    save_path = picture_dir.joinpath(f'Screen Shot {current_time}.png')

    screen_shot = ImageGrab.grab()
    screen_shot.save(save_path)

    # We sleep here not to be lazy but to anticipate button_up
    sleep(0.2)

def shot_loop():
    if running:
        if keyboard.is_pressed('print screen'):
            take_screen_shot()
    root.after(POLL_DELAY, shot_loop)

#################

root = tk.Tk()

root.title(f"screen-shawty {VERSION}")
root.geometry("300x300")

app = tk.Frame(root)
app.pack(expand=True, fill='both')

toggle_button = tk.Button(app, text="Start", bg='green', font=(50), command=start_stop)

toggle_button.pack(expand=True, fill='both')

root.after(POLL_DELAY, shot_loop)
root.mainloop()
