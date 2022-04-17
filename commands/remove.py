#!/usr/bin/env python3

import os
import json
import commands

def remove_c():
    config_dir =  commands.config.f_config_dir()
    config_file = os.path.join(config_dir, 'PacMan.json')

    with open(config_file, 'r') as json_file:
        try:
            json_data = json.load(json_file)
        except json.decoder.JSONDecodeError:
            print("Still entries doesn't get created")
            print("Try help for more details")
        else:
            try:
                if not json_data["entries"][0]:
                    print("No Entries found")
                    return
            except IndexError:
                print("No Entries found")
                return
            commands.display.display()
            remove_entry = int(input("Enter a number to remove the entry : "))
            remove_entry = remove_entry - 1
            json_data["entries"].pop(remove_entry)

    with open(config_file, 'w') as json_file:
        json.dump(json_data, json_file)
    print("Entry removed")