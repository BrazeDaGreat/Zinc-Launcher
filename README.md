    Zinc Launcher
A game launcher written in Python using tkinter, with (WiP) support of auto-updating from Github Repository.

    Usage
First of all, create a `config.py` file, with the following contents:

```py
update_ver   = 1 # TEMPORARILY HERE

discord_link = 'LINK_HERE'
github_link  = 'LINK_HERE'
youtube_link = 'LINK_HERE'
def launch_code(root):
    root.quit
    # Code to execute your game here.
```

## Auto-Update (To-Do)
The `github_link` stores repository for the game, the launcher fetches Releases from the repository, and then checks their update number then proceeds to download new updates.
### Update Number
This number is `0` at initial and increases with each release, independent of semantic versioning.