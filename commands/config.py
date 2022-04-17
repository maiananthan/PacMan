#!/usr/bin/env python3

import os
from pathlib import Path

def f_config_dir():
    try:
        with open(os.path.expanduser('~/.config/PacMan_config_dir'), 'r') as config_file:
            g_config_dir = str(config_file.read())
    except FileNotFoundError:
        print("config not completed")
        print("Try help command")
        exit()
    return os.path.expanduser(g_config_dir)

def config_c():
    config_dir = input("Enter the user defined config path: ")
    Path(os.path.expanduser('~/.config')).mkdir(parents=True, exist_ok=True)
    with open(os.path.expanduser('~/.config/PacMan_config_dir'), 'w') as config_file:
        config_file.write(config_dir)
    Path(os.path.expanduser(config_dir)).mkdir(parents=True, exist_ok=True)