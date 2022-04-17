#!/usr/bin/env python3

import os
import json
from colorama import *
import pycurl
from io import BytesIO
from packaging import version
import commands
import pandas

def github_remote_version(github_url):
    bytesObj = BytesIO()
    handle_cURL = pycurl.Curl()
    handle_cURL.setopt(handle_cURL.URL, github_url)
    handle_cURL.setopt(handle_cURL.WRITEDATA, bytesObj)
    handle_cURL.perform()
    handle_cURL.close()
    bytesObj_body = bytesObj.getvalue()
    str_cURL = bytesObj_body.decode('utf8')
    json_cURL_data = json.loads(str_cURL)
    remote_version = version.parse(json_cURL_data["tag_name"])
    return str(remote_version)

def update_package_list():
    config_dir =  commands.config.f_config_dir()
    config_file = os.path.join(config_dir, 'PacMan.json')
    upgradable = 0

    with open(config_file, 'r') as json_file:
        json_data = json.loads(json_file.read())

    for index in range (len(json_data['entries'])):
        if version.parse(json_data['entries'][index]['current_version']) < version.parse(json_data['entries'][index]['remote_version']):
            print(Fore.CYAN + json_data['entries'][index]['display_name'] + Style.RESET_ALL + " | " + json_data['entries'][index]['current_version'] + " -> " + Fore.GREEN + json_data['entries'][index]['remote_version'] + Style.RESET_ALL)
            upgradable = upgradable + 1
    print(str(upgradable) + " package(s) can be upgraded")

def update_c():
    config_dir =  commands.config.f_config_dir()
    config_file = os.path.join(config_dir, 'PacMan.json')

    json_data = {}
    try:
        with open(config_file, 'r') as json_file:
            json_data = json.loads(json_file.read())
    except FileNotFoundError:
        print("config missing - before addition create should happen")
        print("Try help")
    except json.decoder.JSONDecodeError:
        print("before addition create should happen")
        print("Try help")
    else:  
        length_entries = len(json_data['entries'])
        for index in range(0, length_entries):
            json_data['entries'][index]['remote_version'] = github_remote_version(json_data['entries'][index]['api_url'])

        with open(config_file, 'w') as json_file:
            json.dump(json_data, json_file, indent = 4)
    
    update_package_list()