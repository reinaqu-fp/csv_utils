# -*- coding: utf-8 -*-
'''
Created on 1 oct 2022

@author: Toñi Reina
'''
import random
import numpy as np
from datetime import datetime, timedelta, time, date

def generar_booleanos(num_booleanos):
    '''
    Genera una lista aleatoria de booleanos
    @param num_booleanos: nímero de booleanos a generar
    @type num: int
    @return: Una lista de booleanos generados de forma aleatoria. La lista tendrí tantos booleanos
    como indique el parímetro num_booleanos  
    @rtype: [boolean]
    '''
    boolean_muestra = [True, False]
    return np.random.choice(boolean_muestra, size=num_booleanos)
    
def generar_enteros(limite_inferior, limite_superior, num_enteros):
    '''
    Genera una lista aleatoria de enteros
    @param limite_inferior: Límite inferior del rango de enteros a generar
    @type limite_inferior: int
    @param limite_superior: Límite superior del rango de enteros a generar
    @type limite_superior: int
    @param num_enteros: Nímero de enteros a generar.
    @type num_enteros: int  
    @return:  Una lista de enteros en el rango [limite_inferior, limite_superior] generados
    de forma aleatoria.
    @rtype: [int] 
    '''
    return  np.random.randint(limite_inferior, limite_superior, num_enteros)

def generar_reales(limite_inferior, limite_superior, paso, num_reales):
    '''
    Genera una lista de reales
    @param limite_inferior: Límite inferior del rango de reales a generar
    @type limite_inferior: float
    @param limite_superior: Límite superior del rango de reales a generar
    @type limite_superior: float
    @param paso: Paso de generaciín
    @type paso: float 
    @param num_reales: Nímero de reales a generar.
    @type num_reales: int  
    @return:  Una lista de reales en el rango [limite_inferior, limite_superior] generados
    de forma aleatoria  y con el paso dado como parímetro.
    @rtype: [float]     
    '''
    random_float = np.arange(limite_inferior, limite_superior, round(paso, 2))
    return np.random.choice(random_float, size=num_reales)

def generar_cadenas( lista_valores, num_cadenas):
    '''
    @param lista_valores: Lista de cadenas a partir de la cual se generarí la lista 
    resultado aleatoria
    @type lista_valores: [str]
    @param num_cadenas: Nímero de cadenas a generar en la lista resultado
    @type num_cadenas: int
    @return: Lista de cadenas generada aleatoriamente a partir de la lista de valores de entrada. La
    lista resultante tendrí num_cadenas elementos.
    @rtype: [str]    
    '''
    return np.random.choice(lista_valores, size=num_cadenas)

def generar_fechas(limite_inferior, limite_superior, formato, num_fechas):
    '''
    @param limite_inferior: Fecha que marca el límite inferior del rango
    @type limite_inferior: str  
    @param limite_superior: Fecha que marca el límite superior del rango
    @type limite_superior: str
    @param formato: Formato de la fecha (en estilo Python)
    @type formato: str
     
    '''
    fecha1 = datetime.strptime(limite_inferior, formato)
    fecha2 = datetime.strptime(limite_superior, formato)
    fechas_lista = []
    for _ in range(num_fechas):
        fecha_aux = generar_fecha(fecha1, fecha2)        
        fechas_lista.append(fecha_aux.strftime(formato)) #añadir la fecha en formato str
    return fechas_lista

def generar_fecha (limite_inferior, limite_superior):
    '''
    @param limite_inferior: Fecha que marca el límite inferior del rango
    @type limite_inferior: datetime.date  
    @param limite_superior: Fecha que marca el límite superior del rango
    @type limite_superior: datetime.date
    @return: Fecha generada aleatoriamente entre el limite inferior y el limite superior (ambos inclusive)
    @rtype: datetime.date
    '''
    # dias entre las dos fechas
    dias_totales = (limite_superior - limite_inferior).days
    randay = random.randrange(dias_totales)
    return limite_inferior + timedelta(days=randay)

def generar_hora (limite_inferior=None, limite_superior=None):
    '''
    @param limite_inferior: Hora que marca el límite inferior del rango. Si es None se consideran
      las 00:00
    @type limite_inferior: datetime.time  
    @param limite_superior: Hora que marca el límite superior del rango. Si es None se considera
      las 23:59
    @type limite_superior: datetime.time
    @return: Hora generada aleatoriamente entre el limite inferior y el limite superior (ambos inclusive)
    @rtype: datetime.time
    '''
    # dias entre las dos fechas
    if limite_inferior == None:
        limite_inferior = time(0,0)
    if limite_superior == None:
        limite_superior = time(23,59)
    hoy = date.today()    
    minutos_totales = datetime.combine(hoy, limite_superior) - datetime.combine(hoy, limite_inferior)
    randminutes = random.randrange(minutos_totales.total_seconds())//60
    res = datetime.combine(hoy, limite_inferior) + timedelta(minutes=randminutes)
    return res.time()

def generar_fecha_hora (limite_inferior, limite_superior):
    '''
    @param limite_inferior: Fecha y hora que marca el límite inferior del rango
    @type limite_inferior: datetime.datetime  
    @param limite_superior: Fecha y hora que marca el límite superior del rango
    @type limite_superior: datetime.datetime
    @return: Fecha generada aleatoriamente entre el limite inferior y el limite superior (ambos inclusive)
    @rtype: datetime.datetime
    '''
    delta_seconds = (limite_superior - limite_inferior).total_seconds()
    randseconds = random.randrange(delta_seconds)
    return limite_inferior + timedelta(seconds=randseconds)


    