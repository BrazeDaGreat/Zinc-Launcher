from config import discord_link, github_link, youtube_link # SETTINGS

# PACKAGES #
from tkinter import *
from tkinter import ttk
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
    webbrowser.open('https://www.google.com.pk')
#
def game_launch():
    pass
#
menubar = Menu(root)
#
menu_file = menu_create(menubar, 'Launcher...', [
    ('About...', updates_check),
    ('Repository...', lambda: webbrowser.open('https://github.com/BrazeDaGreat/Zinc-Launcher'))
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
    frame_game, text="Launch Game", command=game_launch, padding=3, width=16
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
