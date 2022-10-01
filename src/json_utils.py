# -*- coding: utf-8 -*-
'''
Created on 1 oct 2022

@author: reinaqu_2
'''
import json

def crea_config_de_json (filename):
    print(filename)
    with open(filename) as json_file:
        data = json.load(json_file)
    return data
            
   