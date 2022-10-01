# -*- coding: utf-8 -*-
'''
Created on 22 oct 2021

@author: reinaqu_2
'''
import csv_generator


def main():
    new_columns_param = {'TIENE_MATERNAL': {'type': 'boolean'},
                         'NUM_CAMAS_MATERNAL': {'type': 'int', 'range': [0, 25]},
                         'MEDIA_OCUPACION_MATERNAL': {'type': 'float', 'range': [1.0, 45.5], 'step': 0.5},
                         'RESPONSABLE_REPETICION': {'type': 'str', 'values': ['R1', 'R2', 'R3'], 'randomize': True},
                         'RESPONSABLE_SIN_REPETICION': {'type': 'str', 'values': ['R'] * 83, 'randomize': False},
                         'FECHA_ULTIMA_REFORMA': {'type': 'datetime', 'range': ['01/01/2020', '31/12/2021'],
                                                  'format': "%d/%m/%Y"}}

    csv_generator.genera_columnas_csv('../data/centrosSanitarios.csv', new_columns_param, delimiter=";")


if __name__ == "__main__":
    main()
