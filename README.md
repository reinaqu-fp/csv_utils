# extract_csv_columns
Pequeño script en python para extraer las columnas deseadas de un csv.
Si quieres extraer solo algunas columnas de tu csv tienes dos opciones:

1. Usar el módulo de forma programática. 
2. Usar el script desde la línea de comandos.

## Uso del módulo de forma programática
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

## Uso desde la línea de comandos
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
