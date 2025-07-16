import pandas as pd
import os
import shutil

cantidad = input("ingrese la cantidad de archivos excel que deseas leer ? : ")
cantidad = int(cantidad)

archivo = input("ingrese el nombre del archivo excel : ")
# Ruta del archivo Excel
contador = 1

if not os.path.exists("leidos"):
    os.makedirs("leidos")

while contador <= cantidad:
    #archivo_excel = archivo + "_" +str(contador)+".csv"  
    archivo_excel = archivo + ".csv"  

    if os.path.exists(archivo_excel):

        # Leer la hoja específica (puedes cambiar el nombre de la hoja)
        df = pd.read_excel(archivo_excel, sheet_name="Sheet1")
        
        # tratar los datos 

        # Mostrar las primeras filas del archivo
        print(df.head())
        # Mover el archivo a la carpeta "leidos"
        shutil.move(archivo_excel, os.path.join("leidos", archivo_excel))
        print(f"Archivo {archivo_excel} movido a 'leidos'")
    else :
        print(f"⚠️ El archivo {archivo_excel} no existe.")   
    contador = contador + 1 

print("================= fin de lectura =======================")
