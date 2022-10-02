# Utilidades para trabajar con csvs 

## csv_extractor

Pequeño script en python para extraer las columnas deseadas de un csv.
Si quieres extraer solo algunas columnas de tu csv tienes dos opciones:

1. Usar el módulo de forma programática. 
2. Usar el script desde la línea de comandos.

### Uso del módulo de forma programática

Tienes que invocar a la función `extrae_columnas_csv` con el nombre y ruta del fichero csv al que quieres recortarle columnas, el nombre y ruta del fichero csv resultado,  una lista con el nombre de las columnas a extraer. Ten en cuenta que el nombre de estas columnas debe aparecer como primera línea (o línea de cabecera) en el fichero csv original.

Puedes ver un ejemplo en el módulo `csv_extractor_test`:

```python
    columnas_a_extraer=['retweet_count', 'favorited','retweeted', 'created_at', 'in_reply_to_user_id_str']
    csv_extractor.extrae_columnas_csv("../data/tweets_all.csv", 
                                      "../data/tweets_cut.csv",
                                      columnas_a_extraer)
```

Además, hay dos parámetros (`encoding` y `separator`) que toman los valores por defecto `latin-1` y `","`, respectivamente, si no se especifican, y que puedes usar si tu archivo csv tiene una codificación distinta de `latin-1` o un separador distinto de la coma, los puedes especificar usando estos parámetros. Puedes ver un ejemplo del uso de estos parámetros en el siguiente trozo de código:

```python
    columnas_a_extraer=['retweet_count', 'favorited','retweeted', 'created_at', 'in_reply_to_user_id_str']
    csv_extractor.extrae_columnas_csv("../data/tweets_all.csv", 
                                      "../data/tweets_cut.csv",
                                      columnas_a_extraer,
                                      encoding='utf-8',
                                      separator=";")
```

### Uso desde la línea de comandos
También puedes usar el script desde la línea de comandos. Ten en cuenta que para ejecutarlo debes situarte en la ruta donde tengas almacenado el módulo `csv_extractor`, o tener bien configurado tu path. Un ejemplo de uso del script desde la línea de comandos lo tienes aquí:

```
python.exe csv_extractor.py -input "../data/tweets_all.csv" -cols "retweet_count" "favorited" "retweeted"
```
El archivo csv resultado de la ejecución del comando tendrá el mismo nombre que el original, sin la extensión .csv y acabado en _cut.csv. Para el ejemplo anterior el archivo resultante se llamará `tweets_all_cut.csv"

Los argumentos que puedes usar son los siguientes:

* **-input**: Nombre y ruta del csv original
* **-cols**: Nombres de las columnas a extraer. Deven estar separados por espacios en blanco.
* **-encoding**:  Si este argumento no aparece, se toma 'latin-1' como codificación del fichero. Si se quiere otra codificación, como utf-8, hay que especificarlo mediante este argumento.
* **-separator**: Si este argumento no aparece, se toma la coma como separador por defecto. Si se quiere usar otro separador, hay que especificarlo mediante este argumento.
* **-h, --help**: Muestra una ayuda breve del uso del comando. El aspecto de la ayuda mostrada es el que ves a continuación.

```
usage: csv_extractor [-h] [-input INPUT] [-encoding [ENCODING]]
                     [-separator [SEPARATOR]] [-cols COLS [COLS ...]]

The result is a new csv with only the columns specified in the argument cols

optional arguments:
  -h, --help            show this help message and exit
  -input INPUT          Original csv file
  -encoding [ENCODING]  If omitted, the default value is latin-1, you can
                        change it to utf-8
  -separator [SEPARATOR]
                        If omitted, the default value is comma ","
  -cols COLS [COLS ...]
                        Names of the columns to extract. They should be
                        present as a header in the original csv file.

```
## csv_joiner

Pequeño script en python para unir dos csvs en uno. El csv resultado tendrá las
columnas del primero junto con las del segundo. Si ambos csvs tienen distinto número
de filas, el csv resultado tendrá el tantas filas como el menor número de filas de los dos archivos.

Si quieres unir dos archivos csv tienes dos opciones:

1. Usar el módulo de forma programática. 
2. Usar el script desde la línea de comandos.

### Uso del módulo de forma programática

Tienes que invocar a la función `une_columnas_csvs` con el nombre y ruta de los ficheros que quieres unir, el nombre y ruta del fichero resultado de la unión. La función tiene los parámetros `encoding_1` y `encoding_2` para indicar la codificación de los dos archivos que se van a unir. El valor por defecto para estos parámetros es 
`latin-1`. Finalmente, esta función también tiene los parámetros separator_1 y separator_2 para indicar el caracter que se usa como separador en el csv. El separador por defecto en ambos casos es la coma.

El fichero de salida tendrá la misma codificación y el mismo separador del `fichero_1`.
Puedes ver un ejemplo en el módulo `csv_joiner_test`:

```python
    csv_joiner.une_columnas_csvs("../data/hoteles.csv", "../data/hotels.csv", "../data/hoteles_joined.csv",
                                      encoding_1="utf-8", 
                                      encoding_2="utf-8")
```

### Uso desde la línea de comandos

También puedes usar el script desde la línea de comandos. Ten en cuenta que para ejecutarlo debes situarte en la ruta donde tengas almacenado el módulo `csv_joiner`, o tener bien configurado tu path. Un ejemplo de uso del script desde la línea de comandos lo tienes aquí:

```
python.exe csv_joiner.py -input1 "../data/hoteles.csv" -input2 "../data/hotels.csv" -encoding1 "utf-8" -encoding2 "utf-8"
```
El archivo csv resultado de la ejecución del comando tendrá el mismo nombre que el fichero que se pasa como parámetro `input1`, sin la extensión `.csv` y acabado en `_joined.csv`. Para el ejemplo anterior el archivo resultante se llamará `hoteles_joined.csv`

Los argumentos que puedes usar son los siguientes:

* **-input1**: Nombre y ruta del primer csv
* **-input2**: Nombre y ruta del segundo csv
* **-encoding1**:  Si este argumento no aparece, se toma 'latin-1' como codificación del primer fichero. Si se quiere otra codificación, como utf-8, hay que especificarlo mediante este argumento.
* **-encoding2**:  Si este argumento no aparece, se toma 'latin-1' como codificación del segundo fichero. Si se quiere otra codificación, como utf-8, hay que especificarlo mediante este argumento.
* **-separator1**: Si este argumento no aparece, se toma la coma como separador por defecto para el primer fichero. Si se quiere usar otro separador, hay que especificarlo mediante este argumento.
* **-separator2**: Si este argumento no aparece, se toma la coma como separador por defecto para el segundo fichero. Si se quiere usar otro separador, hay que especificarlo mediante este argumento.
* **-h, --help**: Muestra una ayuda breve del uso del comando. El aspecto de la ayuda mostrada es el que ves a continuación:

```
usage: csv_joiner [-h] [-input1 INPUT1] [-encoding1 [ENCODING1]]
                  [-separator1 [SEPARATOR1]] [-input2 INPUT2]
                  [-encoding2 [ENCODING2]] [-separator2 [SEPARATOR2]]
```

## csv_generator

Pequeño script en python para añadir a un csv columnas generadas de forma aleatoria.
Si quieres generar de forma aleatoria columnas a tu csv tienes dos opciones:

1. Usar el módulo de forma programática. 
2. Usar el script desde la línea de comandos.

### Uso del módulo de forma programática

Tienes que invocar a la función `genera_columnas_csv` con el nombre y ruta del fichero al que quieres agregarle columnas, un diccionario con la configuración de las columnas a generar, el delimitador que usa el csv (por defecto la coma) y la codificación del archivo (por defecto, `latin-1`). 

El fichero de salida tendrá la misma codificación y el mismo separador del `fichero de entrada`.
Puedes ver un ejemplo en el módulo `csv_generator_test`:

```python
   new_columns_param = {'TIENE_MATERNAL': {'type': 'boolean'},
                         'NUM_CAMAS_MATERNAL': {'type': 'int', 'range': [0, 25]},
                         'MEDIA_OCUPACION_MATERNAL': {'type': 'float', 'range': [1.0, 45.5], 'step': 0.5},
                         'RESPONSABLE_REPETICION': {'type': 'str', 'values': ['R1', 'R2', 'R3'], 'randomize': True},
                         'RESPONSABLE_SIN_REPETICION': {'type': 'str', 'values': ['R'] * 83, 'randomize': False},
                         'FECHA_ULTIMA_REFORMA': {'type': 'date', \
                                                  'range': ['01/01/2020', '31/12/2021'],
                                                  'format': "%d/%m/%Y"},
                         'HORA_CONSULTA':{'type': 'time',
                                          'range': ['08:30','15:00'],
                                          'format': "%H:%M"},
                         'FECHA_HORA':{'type': 'datetime',
                                       'range': ['01/01/2020 08:30','31/12/2021 15:00'],
                                        'format': "%d/%m/%Y %H:%M"}
                         }

    csv_generator.genera_columnas_csv('../data/centrosSanitarios.csv', new_columns_param, delimiter=";")
```

También puedes usar de forma programática la versión de la función que toma un archivo en formato json como parámetro de entrada en el que se define la configuración de las columnas que se quiere generar. También puedes ver un ejemplo en el módulo `csv_generator_test`:

```python
 csv_generator.genera_columnas_csv_de_json('../data/centrosSanitarios.csv', '../data/columnas.json', delimiter=";")
```

### Uso desde la línea de comandos

También puedes usar el script desde la línea de comandos. Ten en cuenta que para ejecutarlo debes situarte en la ruta donde tengas almacenado el módulo `csv_generator`, o tener bien configurado tu path. Un ejemplo de uso del script desde la línea de comandos lo tienes aquí:

```
python.exe csv_generator.py -input "../data/centrosSanitarios.csv" -encoding "utf-8" -config  "../data/columnas.json"
```
El archivo csv resultado de la ejecución del comando tendrá el mismo nombre que el fichero que se pasa como parámetro `input`, sin la extensión `.csv` y acabado en `_generated.csv`. Para el ejemplo anterior el archivo resultante se llamará `centrosSanitarios_joined.csv`

Los argumentos que puedes usar son los siguientes:

* **-input**: Nombre y ruta del archivo csb
* **-config**: Nombre y ruta de un archivo json con la configuración de las columnas a generar.
* **-encoding**:  Si este argumento no aparece, se toma 'latin-1' como codificación fichero. Si se quiere otra codificación, como utf-8, hay que especificarlo mediante este argumento.
* **-separator**: Si este argumento no aparece, se toma la coma como separador por defecto. Si se quiere usar otro separador, hay que especificarlo mediante este argumento.
* **-h, --help**: Muestra una ayuda breve del uso del comando. El aspecto de la ayuda mostrada es el que ves a continuación:

```
usage: csv_generator [-h] [-input INPUT] [-config CONFIG]
                     [-encoding [ENCODING]] [-separator [SEPARATOR]]

The result is a new csv with the new columns specified in the argument config by means of a json config file

optional arguments:
  -h, --help            show this help message and exit
  -input INPUT          Original csv file
  -config CONFIG        JSON file with the configuration of columns.
  -encoding [ENCODING]  If omitted, the default value is latin-1, you can
                        change it to utf-8
  -separator [SEPARATOR]
                        If omitted, the default value is comma, you can change
                        it to any other
```