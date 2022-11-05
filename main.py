# SETTINGS
from config import discord_link, github_link, youtube_link, launch_code

# PACKAGES #
from tkinter import *
from tkinter import ttk, messagebox
import os
import webbrowser

# FILES #
from funcs import button_create, menu_create


root = Tk()
root.title("Theta Quartz Launcher")
root.iconbitmap('ring.ico')
root.option_add('*tearOff', FALSE)
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')

# ========== #
def updates_check():
    messagebox.showinfo(message="Coming Soon(TM).")
def openGithub():
    webbrowser.open('https://github.com/BrazeDaGreat/Zinc-Launcher')
def showAbout():
    messagebox.showinfo(message=f"""
    Theta Launcher Beta 1.0
    ----------------------------------------
    Just... something made in Tkinter.
    Don't forget to create a config.py file.

    TODO:
        * Checking for updates.
    ----------------------------------------
    (Created with <3 by Braze)
    """)
#
menubar = Menu(root)
#
menu_file = menu_create(menubar, 'Launcher...', [
    ('About...', showAbout),
    ('Repository...', openGithub)
])
#
root['menu'] = menubar
# ========== #
frame_update = ttk.LabelFrame(root, text="Updates", padding=16, borderwidth=8)
frame_update.grid(row=0, column=0, padx=6, pady=6)
# 
btn_update = ttk.Button(
    frame_update, text="Check for Updates", command=updates_check, padding=3, width=16
)
btn_update.grid(row=0, column=0)

# ========== #
frame_game = ttk.LabelFrame(root, text="Game", padding=16, borderwidth=8)
frame_game.grid(row=0, column=1, padx=6, pady=6)
# 
btn_launch = ttk.Button(
    frame_game, text="Launch Game", command=launch_code, padding=3, width=16
)
btn_launch.grid(row=0, column=0)

# ========== #
frame_misc = ttk.LabelFrame(root, text="Misc", padding=16, borderwidth=8)
frame_misc.grid(row=1, column=0, padx=6, pady=6, columnspan=2)

btn_disc = button_create(frame_misc, "Join Discord Server...", lambda: webbrowser.open(discord_link), 18)
btn_disc.grid(row=0, column=0, padx=3, pady=3)

btn_git = button_create(frame_misc, "Github Repository...", lambda: webbrowser.open(github_link), 18)
btn_git.grid(row=0, column=1, padx=3, pady=3)

btn_yt = button_create(frame_misc, "YouTube Channel...", lambda: webbrowser.open(youtube_link), 18)
btn_yt.grid(row=1, column=0, padx=3, pady=3)

root.mainloop()
