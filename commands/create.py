#!/usr/bin/env python3

import os
import json
from colorama import Fore, Back, Style
import commands

def create_c():
    config_dir =  commands.config.f_config_dir()
    config_file = os.path.join(config_dir, 'PacMan.json')

    # check for config_file
    if os.path.isfile(config_file) and os.access(config_file, os.R_OK):
        print("Config file " + Fore.GREEN + config_file + Style.RESET_ALL + " exists already")
        # config_file is there
        with open(config_file, 'r') as json_file:
            print(os.stat(config_file).st_size)
            if os.stat(config_file).st_size != 0:
                json_data = json.loads(json_file.read())
                # check for the contents 
                if json_data["pc_name"]:
                    print("All set to go !!!")
            else:
                pc_name = input("Enter the PC Name : ")
                with open(config_file, 'w') as json_file:
                    json_temp_data = {"pc_name": pc_name, "entries": []}
                    json.dump(json_temp_data, json_file, indent=4)

    else:
        print("config file is not there")
        pc_name = input("Enter the PC name : ")
        # create config_file 
        with open(config_file, 'w') as json_file:
            print("file created")
            pass
        # ask for pc_name
        with open(config_file, 'w') as json_file:
            json_temp_data = {"pc_name": pc_name, "entries": []}
            json.dump(json_temp_data, json_file, indent=4)