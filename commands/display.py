#!/usr/bin/env python3

import os
import json
import pprint
import pandas
import commands
from tabulate import tabulate
from colorama import *

def display_c():
    config_dir =  commands.config.f_config_dir()
    config_file = os.path.join(config_dir, 'PacMan.json')

    try:
        with open(config_file, 'r') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        print("before addition create should happen")
        print("Try help")
    else:
        print(Fore.BLUE + "PC Name : ", json_data['pc_name'] + Style.RESET_ALL)
        json_data_array = json_data['entries']
        data_print = pandas.DataFrame(json_data_array, columns=["display_name", "current_version"])
        data_print.index = data_print.index + 1
        print(tabulate(data_print, headers='keys', tablefmt='grid', numalign='center', stralign='center'))