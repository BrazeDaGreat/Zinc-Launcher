from tkinter import Menu
from tkinter import ttk

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