from tkinter import *
from tkinter import ttk
import os
import webbrowser

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

# ========== #
def button_create(master, text, command, width=16):
    return ttk.Button(
        master, text=text, command=command, padding=3, width=width
    )
# ========== #
def menu_create(master, label, cmds):
    menu = Menu(master)
    for x in cmds:
        menu.add_command(label=x[0], command=x[1])
    master.add_cascade(menu=menu, label=label)
    return menu
#
menubar = Menu(root)
#
menu_file = menu_create(menubar, 'Launcher...', [
    ('About...', updates_check),
    ('Repository...', lambda: webbrowser.open('https://www.github.com/BrazeDaGreat'))
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

btn_disc = button_create(frame_misc, "Join Discord Server...", updates_check, 18)
btn_disc.grid(row=0, column=0, padx=3, pady=3)

btn_git = button_create(frame_misc, "Github Repository...", updates_check, 18)
btn_git.grid(row=0, column=1, padx=3, pady=3)

btn_yt = button_create(frame_misc, "YouTube Channel...", updates_check, 18)
btn_yt.grid(row=1, column=0, padx=3, pady=3)

root.mainloop()
