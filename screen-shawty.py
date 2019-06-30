#!/usr/bin/env python3

import keyboard

from PIL import ImageGrab

from time import sleep
from time import time

from pathlib import Path

import tkinter as tk

VERSION = '0.01b'
running = False # The application is stopped/not listening in background.

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
    current_time = str(time()).replace('.','')
    picture_dir = Path.home().joinpath('Pictures')

    # State of the art error handling!
    if not picture_dir.exists():
        try:
            picture_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(e)

    save_path = picture_dir.joinpath(f'Screen Shot {current_time}.png')

    screen_shot = ImageGrab.grab()
    screen_shot.save(save_path)

def shot_loop():
    if running:
        if keyboard.is_pressed('print screen'):
            take_screen_shot()
    root.after(150, shot_loop)

#################

root = tk.Tk()

root.title(f"screen-shawty {VERSION}")
root.geometry("250x250")

app = tk.Frame(root)
app.pack(expand=True, fill='both')

toggle_button = tk.Button(app, text="Start", bg='green', font=(50), command=start_stop)

toggle_button.pack(expand=True, fill='both')

root.after(150, shot_loop)
root.mainloop()
