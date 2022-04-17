#!/usr/bin/env python3

import os
import json
from commands.color import color as c
import commands
# from simple_term_menu import TerminalMenu
from packaging import version
from colorama import Fore, Back, Style

def upgradable_count():
    config_dir =  commands.config.f_config_dir()
    config_file = os.path.join(config_dir, 'PacMan.json')
    
    u_pac_count = 0

    with open(config_file, 'r') as json_file:
        json_data = json.loads(json_file.read())

    for index in range(len(json_data['entries'])):
        if version.parse(json_data['entries'][index]['current_version']) < version.parse(json_data['entries'][index]['remote_version']):
            u_pac_count = u_pac_count + 1

    return u_pac_count 


def upgrade_c():
    config_dir =  commands.config.f_config_dir()
    config_file = os.path.join(config_dir, 'PacMan.json')
    
    with open(config_file, 'r') as json_file:
        json_data = json.loads(json_file.read())

    u_pac_count = 0
    up_pack_count = upgradable_count()
    print(Fore.GREEN + str(up_pack_count) + Style.RESET_ALL + " upgradable" + "\npackage list")

    for index in range(len(json_data['entries'])):
        if version.parse(json_data['entries'][index]['current_version']) < version.parse(json_data['entries'][index]['remote_version']):
            upgrade_status = input(Fore.CYAN + "\033[1m" + json_data['entries'][index]['display_name'] + Style.RESET_ALL + "\npackage upgraded [" + Fore.GREEN + "Y" + Style.RESET_ALL + "/" + Fore.RED + "n" + Style.RESET_ALL + "]: ")
            if upgrade_status == 'y' or upgrade_status == 'Y':
                print(Fore.LIGHTGREEN_EX + json_data['entries'][index]['display_name'] + " upgraded")
                u_pac_count = u_pac_count + 1
                json_data['entries'][index]['current_version'] = json_data['entries'][index]['remote_version']
            elif upgrade_status == 'n' or upgrade_status == 'N':
                continue
    
    print("[" + Fore.GREEN + str(u_pac_count) + Style.RESET_ALL + "/" + str(up_pack_count) + "] upgraded")
    with open(config_file, 'w') as json_file:    
        json.dump(json_data, json_file, indent=4)