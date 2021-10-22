# extract_csv_columns
Pequeño script en python para extraer las columnas deseadas de un csv.
Si quieres extraer solo algunas columnas de tu csv tienes dos opciones:

1. Usar el módulo de forma programática. 
2. Usar el script desde la línea de comandos.

## Uso del módulo de forma programática
Tienes que invocar a la función `extrae_columnas_csv` con el nombre y ruta del fichero csv al que quieres recortarle columnas, el nombre y ruta del fichero csv resultado, y una lista con el nombre de las columnas a extraer. Ten en cuenta que el nombre de estas columnas debe aparecer como primera línea (o línea de cabecera) en el fichero csr original.

Puedes ver un ejemplo en el módulo `csv_extractor_test`:

```python
    columnas_a_extraer=['retweet_count', 'favorited','retweeted', 'created_at', 'in_reply_to_user_id_str']
    csv_extractor.extrae_columnas_csv("../data/tweets_all.csv", 
                                      "../data/tweets_cut.csv",
                                      columnas_a_extraer)
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
* **-encoding**:  Si este argumento no aparece, se toma 'latin-1' como codificación del fichero. Si se quiere otra codificación, como utf-8, habría que especificarla.
* **-h, --help**: Muestra una ayuda breve del uso del comando.

```
The result is a new csv with only the columns specified in the argument cols

Optional arguments:
 -h, --help            show this help message and exit
 -input INPUT          original csv file
 -cols COLS [COLS ...]
                       names of the columns to extract
 -encoding [ENCODING]  encoding, by default is latin-1, you can change it to
                       utf-8
```
