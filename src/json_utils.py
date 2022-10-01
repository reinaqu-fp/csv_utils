# -*- coding: utf-8 -*-
'''
Created on 1 oct 2022

@author: reinaqu_2
'''
import json

def crea_config_de_json (filename):
    '''
    @param filename: Nombre y ruta del archivo json con la configuración de las columnas
    @type filename: str
    @return: Un diccionario con los datos de configuración de las columnas
    @rtype: {str: Any}
    '''
    with open(filename) as json_file:
        data = json.load(json_file)
    return data
            