# -*- coding: utf-8 -*-
'''
Created on 22 oct 2021

@author: reinaqu_2
'''
import argparse
import csv
import logging

def extrae_columnas_csv(fichero_entrada, fichero_salida, columnas_a_extraer=[], encoding='latin-1', separator=","):
    '''
    Esta función genera un fichero csv a partir del fichero csv dado en el parámetro fichero_entrada
    pero que solo tiene las columnas especificadas en el parámetro columnas_a_extraer.
    @param fichero_entrada: Nombre y ruta del fichero csv original
    @type fichero_entrada: str
    @param fichero_salida: Nombre y ruta del fichero csv resultado.
    @type fichero_salida: str 
    @param columnas_a_extraer: Lista con los nombres de las columnas que queremos extraer del csv
    original. La primera linea del fichero csv original debe contener los nombres de las columnas.
    @type columnas_a_extraer: [str] 
    @param encoding: Cadena que indica la codificación en la que está el fichero original. Si no se 
    especifica, por defecto se supone que el archivo está codificado en latin-1 (codificación de Windows).
    @type encoding: str 
    @param separator: Cadena que indica el separador usado para generar el csv
    @type separator: str
    '''    
    with open(fichero_entrada, encoding=encoding) as rf:
        lector = csv.DictReader(rf, delimiter=separator)
        with open(fichero_salida, 'w', encoding=encoding,  newline='') as wf:
            dict_cabecera = crea_dict_cabecera (columnas_a_extraer)
            dw = csv.DictWriter(wf, fieldnames=dict_cabecera, quoting=csv.QUOTE_ALL, quotechar='"', delimiter=separator)
            dw.writeheader()
            #Vamos leyendo los diccionarios del lector
            for dict_lector in lector:
                dict_fila = crea_dict_fila (dict_lector, columnas_a_extraer)
                dw.writerow (dict_fila)
        wf.close()
    rf.close        

def crea_dict_cabecera(nombres_columnas):
    '''
    @param nombres_columnas: Lista con los nombres de las columnas a extraer.
    @type nombres_columnas: [str]
    @return: Devuelve un diccionario que tiene como y como valores los nombres de las columnas.
    @rtype: {str:str} 
    '''
    return {nombre_col:nombre_col for nombre_col in nombres_columnas}

def crea_dict_fila(dict_origen, columnas_a_extraer):
    '''
    @param dict_origen: Diccionario que representa una fila del csv original. Las claves del diccionario
    son los nombres de las columnas y los valores, el valor concreto de esa columna en la fila del
    csv original.
    @type dict_origen: {str:str}
    @param columnas_a_extraer: Lista con los nombres de las columnas que queremos extraer del csv
    original. La primera linea del fichero csv original debe contener los nombres de las columnas.
    @type columnas_a_extraer: [str]     
    @return Un diccionario cuyas parejas de elementos son un subconjunto de las parejas del diccionario
    original. Solamente tiene las parejas cuyas claves son las columnas a extraer.
    @rtype: {str:str}
    '''
    return {nombre_col: dict_origen[nombre_col] for nombre_col in columnas_a_extraer}

def nombre_fichero_salida(fichero_entrada):  
    '''
    @param fichero_entrada: Nombre y ruta del fichero csv de entrada.
    @type fichero_entrada: str
    @return: El nombre del fichero de salida que se genera como el nombre del fichero de entrada,
        sin la cadena ".csv" y terminado en "_cut.csv"
    '''
    return fichero_entrada.replace(".csv","")+"_cut.csv"

def encoding(args):
    '''
    @return: Un objeto que define los argumentos que se esperan si se usa este módulo
    desde la linea de comandos.
    @type args: argparse.Namespace
    @return: La codificación extraída de los argumentos de la línea de comandos. Si
    el parámetro no se especifica, la codificación por defecto es utf-8.
    @rtype: str
    '''
    enc=","
    if args.encoding:
        enc = args.encoding[0]
    return enc

def separador(args):
    '''
    @return: Un objeto que define los argumentos que se esperan si se usa este módulo
    desde la linea de comandos.
    @type args: argparse.Namespace
    @return: El carácter separador usado para separar una columna de otra en el csv extraido
    de los argumentos de la línea de comandos. Si el parámetro no se especifica, el separador 
    por defecto es la coma.
    @rtype: str
    '''
    sep = 'latin-1'
    if args.separator:
        sep = args.separator[0]
    return sep

def main():
    '''
    Función principal para gestionar la línea de argumentos
    '''
    args = parse_arg()
    print(type(args))
    logging.basicConfig(level=logging.INFO)
    
    fichero_entrada = args.input[0]
    fichero_salida = nombre_fichero_salida (fichero_entrada)
    enc = encoding(args)
    sep = separador (args) 
    logging.info("Escribiendo en ..."+ fichero_salida)
    extrae_columnas_csv(fichero_entrada, fichero_salida,
                                      args.cols, 
                                      encoding=enc,
                                      separator= sep)



def parse_arg():
    '''
    @return: Un objeto que define los argumentos que se esperan si se usa este módulo
    desde la linea de comandos
    @rtype: argparse.Namespace
    '''
    descr = 'The result is a new csv with only the columns specified in the argument cols'
    parser = argparse.ArgumentParser(prog='csv_extractor', description=descr)
    parser.add_argument('-input', nargs=1, type=str, help='Original csv file')
    parser.add_argument('-encoding', nargs='?', help='If omitted, the default value is latin-1, you can change it to utf-8')
    parser.add_argument('-separator', nargs='?', help='If omitted, the default value is comma ","')
    parser.add_argument('-cols', nargs='+', type=str, help='Names of the columns to extract. They should be present as a header in the original csv file.')
    return parser.parse_args()


if __name__ == "__main__":
    main()