# -*- coding: utf-8 -*-
'''
Created on 1 oct 2022

@author: Toñi Reina
'''
import random
import numpy as np
from datetime import datetime, timedelta

def generar_booleanos(num_booleanos):
    '''
    Genera una lista aleatoria de booleanos
    @param num_booleanos: n�mero de booleanos a generar
    @type num: int
    @return: Una lista de booleanos generados de forma aleatoria. La lista tendr� tantos booleanos
    como indique el par�metro num_booleanos  
    @rtype: [boolean]
    '''
    boolean_muestra = [True, False]
    return np.random.choice(boolean_muestra, size=num_booleanos)
    
def generar_enteros(limite_inferior, limite_superior, num_enteros):
    '''
    Genera una lista aleatoria de enteros
    @param limite_inferior: L�mite inferior del rango de enteros a generar
    @type limite_inferior: int
    @param limite_superior: L�mite superior del rango de enteros a generar
    @type limite_superior: int
    @param num_enteros: N�mero de enteros a generar.
    @type num_enteros: int  
    @return:  Una lista de enteros en el rango [limite_inferior, limite_superior] generados
    de forma aleatoria.
    @rtype: [int] 
    '''
    return  np.random.randint(limite_inferior, limite_superior, num_enteros)

def generar_reales(limite_inferior, limite_superior, paso, num_reales):
    '''
    Genera una lista de reales
    @param limite_inferior: L�mite inferior del rango de reales a generar
    @type limite_inferior: float
    @param limite_superior: L�mite superior del rango de reales a generar
    @type limite_superior: float
    @param paso: Paso de generaci�n
    @type paso: float 
    @param num_reales: N�mero de reales a generar.
    @type num_reales: int  
    @return:  Una lista de reales en el rango [limite_inferior, limite_superior] generados
    de forma aleatoria  y con el paso dado como par�metro.
    @rtype: [float]     
    '''
    random_float = np.arange(limite_inferior, limite_superior, round(paso, 2))
    return np.random.choice(random_float, size=num_reales)

def generar_cadenas( lista_valores, num_cadenas):
    '''
    @param lista_valores: Lista de cadenas a partir de la cual se generar� la lista 
    resultado aleatoria
    @type lista_valores: [str]
    @param num_cadenas: N�mero de cadenas a generar en la lista resultado
    @type num_cadenas: int
    @return: Lista de cadenas generada aleatoriamente a partir de la lista de valores de entrada. La
    lista resultante tendr� num_cadenas elementos.
    @rtype: [str]    
    '''
    return np.random.choice(lista_valores, size=num_cadenas)

def generar_fechas(limite_inferior, limite_superior, formato, num_fechas):
    '''
    @param limite_inferior: Fecha que marca el l�mite inferior del rango
    @type limite_inferior: str  
    @param limite_superior: Fecha que marca el l�mite superior del rango
    @type limite_superior: str
    @param formato: Formato de la fecha (en estilo Python)
    @type formato: str
     
    '''
    fecha1 = datetime.strptime(limite_inferior, formato)
    fecha2 = datetime.strptime(limite_superior, formato)
    fechas_lista = []
    for _ in range(num_fechas):
        fecha_aux = generar_fecha(fecha1, fecha2)        
        fechas_lista.append(fecha_aux.strftime(formato)) #a�adir la fecha en formato str
    return fechas_lista

def generar_fecha (limite_inferior, limite_superior):
    '''
    @param limite_inferior: Fecha que marca el l�mite inferior del rango
    @type limite_inferior: datetime.date  
    @param limite_superior: Fecha que marca el l�mite superior del rango
    @type limite_superior: datetime.date
    @return: Fecha generada aleatoriamente entre el limite inferior y el limite superior (ambos inclusive)
    @rtype: datetime.date
    '''
    # dias entre las dos fechas
    dias_totales = (limite_superior - limite_inferior).days
    randay = random.randrange(dias_totales)
    return limite_inferior + timedelta(days=randay)

