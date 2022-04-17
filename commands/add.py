#!/usr/bin/env python3

import os
import json
from colorama import Fore, Back, Style
import commands

def add_c():
    config_dir =  commands.config.f_config_dir()
    config_file = os.path.join(config_dir, 'PacMan.json')

    json_data = {}
    try:
        with open(config_file, 'r') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        print("before addition create should happen")
        print("Try help")
    except json.decoder.JSONDecodeError:
        print("before addition create should happen")
        print("Try help")
    else:
        display_name = input("Enter the display name : ")
        GitHub_url = input("GitHub URL: ")
        gh_list = GitHub_url.split('/')
        try:
            user_name = gh_list[3]
            repo_name = gh_list[4]
        except IndexError:
            print(Fore.RED + "GitHub URL is wrong" + Style.RESET_ALL)
            return
        api_url = "https://api.github.com/repos/" + user_name + "/" + repo_name + "/releases/latest"
        current_version = ""
        remote_version = ""
        json_data["entries"].append({"display_name": display_name, "api_url": api_url, "current_version": current_version, "remote_version": remote_version})
        with open(config_file, 'w') as json_file:    
            json.dump(json_data, json_file, indent=4)