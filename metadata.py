import os,stat
import time
import datetime
from pathlib import *
import pandas as pd
import csv

#for the entire directory
list_paths = []
for i in os.listdir(path):
    list_paths.append(i)

path=''#here goes the complete path of the folder
def get_info_file(path):
    file_name = []
    file_size =[]
    list_paths = []
    modification_date = []
    modification_date_2 =[]

    for i in os.scandir(path):
        file_name.append(i.name)
        file_size.append(i.stat().st_size)
        #modification time
    for i in os.listdir(path):
        list_paths.append(i)
    for x in list_paths:
        y = os.path.getmtime(x)
        modification_date.append(y)
    #Converting time to timestamp
    for i in modification_date:
        ti = time.ctime(i)
        modification_date_2.append(ti)
    #Create dataframe

    df = pd.DataFrame(
        {'Nombre Archivo':file_name,
        'Tamaño Archivo en MB':file_size,
        'Fecha de Modificación':modification_date_2,}
    )

    print(df.info()),'\n'
    print(df['Tamaño Archivo en MB'].sum(),'MB')
    return df
    
    x = str(list_paths[13])
##function to get the number of columns and rows from csv or excel

def file_info(x):#Como parametro debe recibir el nombre del archivo
    #check if is .csv
    split_tup = os.path.splitext(x)
    file_extension = split_tup[1]
    if file_extension == '.csv':
        file = open(x)
        #Leer CSV reader funcion de la libreria CSV
        entrada = csv.reader(file)
        cols = len(next(entrada))
        #Contar filas
        rows = len(list(entrada))
        #Creando el dataframe para obtener la info
        data=pd.read_csv(x)
        print(f"la cantidad de columnas son {cols} y de filas son {rows} en el archivo .csv")
        return data.info()
    elif file_extension=='.xlsx' or file_extension=='.xlx':
        excel_dataframe = pd.read_excel(x)
        #get_the number of rows in the dataframe
        rows_exe = len(excel_dataframe)
        columns = len(excel_dataframe.columns)
        print(f"la cantidad de columns son {columns} y de filas son {rows_exe} en el archivo de excel")
    else:
        print("Es otro tipo de archivo")
  
  
