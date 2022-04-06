# -*- coding: utf-8 -*-
'''
Created on 22 oct 2021

@author: reinaqu_2
'''
import argparse
import csv
import logging

def une_columnas_csvs(fichero_1, fichero_2, fichero_salida, 
                      encoding_1='latin-1', separator_1=",",
                     encoding_2='latin-1', separator_2 = ","):
    '''
    Esta función genera un fichero csv a partir dos ficheros csvs dado como parámetro. El nuevo fichero
    tendrá las columnas del primer csv seguidas de las columnas del segundo csv
    @param fichero_entrada1: Nombre y ruta del primer fichero csv 
    @type fichero_entrada1: str
    @param fichero_entrada2: Nombre y ruta del segundo fichero csv 
    @type fichero_entrada2: str
    @param fichero_salida: Nombre y ruta del fichero csv resultado.
    @type fichero_salida: str 
    @type columnas_a_extraer: [str] 
    @param encoding_1: Cadena que indica la codificación en la que está el primer fichero. Si no se 
    especifica, por defecto se supone que el archivo está codificado en latin-1 (codificación de Windows).
    @type encoding_1: str 
    @param separator_1: Cadena que indica el separador del primer fichero. Si no se pone nada, 
    toma la coma comp separador por defecto. Este separador es también el que se usará 
    en el fichero de salida
    @type separator_1: str
    @param encoding_2: Cadena que indica la codificación en la que está el segundo fichero. Si no se 
    especifica, por defecto se supone que el archivo está codificado en latin-1 (codificación de Windows).
    @type encoding_2: str 
    @param separator_2: Cadena que indica el separador del segundo fichero. Si no se pone nada, 
    toma la coma comp separador por defecto.
    @type separator_2: str

    '''    
    with open(fichero_1, encoding=encoding_1) as rf:
        lector_1 = csv.DictReader(rf, delimiter=separator_1)
        with open(fichero_2, encoding=encoding_2) as rf:
            lector_2 = csv.DictReader(rf, delimiter=separator_2)
        
            with open(fichero_salida, 'w', encoding=encoding_1,  newline='') as wf:
                cabecera = lector_1.fieldnames + lector_2.fieldnames
                dw = csv.DictWriter(wf, fieldnames=cabecera, quoting=csv.QUOTE_ALL, quotechar='"', delimiter=separator_1)
                dw.writeheader()
                #Vamos leyendo los diccionarios del lector
                for dict_lector_1, dict_lector_2 in zip(lector_1, lector_2):
                    dict_fila=dict(dict_lector_1) 
                    dict_fila.update(dict_lector_2)
                    dw.writerow (dict_fila)
            wf.close()
        rf.close        


def nombre_fichero_salida(fichero_entrada):  
    '''
    @param fichero_entrada: Nombre y ruta del fichero csv de entrada.
    @type fichero_entrada: str
    @return: El nombre del fichero de salida que se genera como el nombre del fichero de entrada,
        sin la cadena ".csv" y terminado en "_cut.csv"
    '''
    return fichero_entrada.replace(".csv","")+"_joined.csv"

def main():
    '''
    Función principal para gestionar la línea de argumentos
    '''
    args = parse_arg()
    print(type(args))
    logging.basicConfig(level=logging.INFO)
    
    fichero_entrada1 = args.input1[0]
    fichero_entrada2 = args.input2[0]
    fichero_salida = nombre_fichero_salida (fichero_entrada1)
    enc1 = args.encoding1[0] if args.encoding1 else 'latin-1'
    enc2 = args.encoding2[0] if args.encoding2 else 'latin-1' 
    sep1 = args.separator1[0] if args.separator1 else ','
    sep2 = args.separator2[0] if args.separator2 else ',' 
    logging.info("Escribiendo en ..."+ fichero_salida)
    une_columnas_csvs(fichero_entrada1, fichero_entrada2, fichero_salida,
                                      encoding1=enc1,
                                      enconding2=enc2,
                                      separator1= sep1,
                                      separator2=sep2)


def parse_arg():
    '''
    @return: Un objeto que define los argumentos que se esperan si se usa este módulo
    desde la linea de comandos
    @rtype: argparse.Namespace
    '''
    descr = 'The result is a new csv with the columns of the file specified in input1 followed by the columns of the file specified in input2'
    parser = argparse.ArgumentParser(prog='csv_joiner', description=descr)
    parser.add_argument('-input1', nargs=1, type=str, help='Original csv file')
    parser.add_argument('-encoding1', nargs='?', help='If omitted, the default value is latin-1, you can change it to utf-8')
    parser.add_argument('-separator1', nargs='?', help='If omitted, the default value is comma ","')
    parser.add_argument('-input2', nargs=1, type=str, help='Original csv file')
    parser.add_argument('-encoding2', nargs='?', help='If omitted, the default value is latin-1, you can change it to utf-8')
    parser.add_argument('-separator2', nargs='?', help='If omitted, the default value is comma ","')
    
    return parser.parse_args()


if __name__ == "__main__":
    main()