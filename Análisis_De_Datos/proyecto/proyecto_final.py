import pandas as pd
import random
import datetime
import os
import shutil

def generar_datos(nombre_archivo, extension="csv"):
    productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora"]
    categorias = ["Electrónica", "Periféricos", "Accesorios"]
    clientes = ["Juan", "Lucía", "Pedro", "Ana", "Carlos"]
    metodos_pago = ["Efectivo", "Tarjeta", "Yape", "Plin"]
    sucursales = ["Sucursal Norte", "Sucursal Sur"]

    datos = []
    for i in range(100):
        fecha = datetime.date(2024, random.randint(1, 6), random.randint(1, 28))
        datos.append((
            i + 1,
            fecha,
            random.choice(productos),
            random.choice(categorias),
            random.choice(clientes),
            random.randint(1, 5),
            round(random.uniform(100, 1000), 2),
            random.choice(metodos_pago),
            random.choice(sucursales)
        ))

    columnas = [
        "ID", "Fecha", "Producto", "Categoría", "Cliente",
        "Cantidad", "Precio Unitario", "Método de Pago", "Sucursal"
    ]
    df = pd.DataFrame(datos, columns=columnas)

    if extension == "csv":
        df.to_csv(nombre_archivo, index=False)
    else:
        df.to_excel(nombre_archivo, index=False)

    print(f"Archivo generado: {nombre_archivo}")

def leer_archivo(nombre_archivo):
    if nombre_archivo.endswith(".csv"):
        return pd.read_csv(nombre_archivo)
    elif nombre_archivo.endswith(".xlsx"):
        return pd.read_excel(nombre_archivo)
    else:
        raise ValueError("Formato de archivo no compatible: debe ser .csv o .xlsx")

def generar_modelo_estrella(df, nombre_salida):
    dimensiones = {
        "Producto": df["Producto"].unique().tolist(),
        "Categoría": df["Categoría"].unique().tolist(),
        "Cliente": df["Cliente"].unique().tolist(),
        "Método de Pago": df["Método de Pago"].unique().tolist(),
        "Sucursal": df["Sucursal"].unique().tolist()
    }

    tablas_dim = {}
    for nombre_dim, valores in dimensiones.items():
        tablas_dim[nombre_dim] = pd.DataFrame(
            [(i + 1, v) for i, v in enumerate(valores)],
            columns=[f"ID_{nombre_dim.replace(' ', '_')}", nombre_dim]
        )

    df_hechos = df.copy()
    for nombre_dim in dimensiones:
        mapa = {valor: idx + 1 for idx, valor in enumerate(dimensiones[nombre_dim])}
        df_hechos[f"ID_{nombre_dim.replace(' ', '_')}"] = df_hechos[nombre_dim].map(mapa)

    df_hechos["Fecha"] = pd.to_datetime(df_hechos["Fecha"])
    df_hechos["Año"] = df_hechos["Fecha"].dt.year
    df_hechos["Mes"] = df_hechos["Fecha"].dt.month
    df_hechos["Día"] = df_hechos["Fecha"].dt.day

    if not os.path.exists("modelosdatos"):
        os.makedirs("modelosdatos")

    output_path = f"modelosdatos/{nombre_salida}.xlsx"
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df_hechos.to_excel(writer, sheet_name="Tabla_Hechos", index=False)
        for nombre, df_dim in tablas_dim.items():
            df_dim.to_excel(writer, sheet_name=f"Dim_{nombre}", index=False)

    print(f"Modelo de datos generado: {output_path}")

def mover_a_leidos(nombre_archivo):
    if not os.path.exists("leidos"):
        os.makedirs("leidos")
    shutil.move(nombre_archivo, f"leidos/{nombre_archivo}")
    print(f"Archivo {nombre_archivo} movido a carpeta 'leidos'")

# ====================== FLUJO PRINCIPAL ======================

extensiones = ["csv", "xlsx"]  # puedes alternar entre formatos
for i in range(1, 6):
    ext = extensiones[i % 2]  # alterna entre .csv y .xlsx
    nombre_archivo = f"ventas_{i}.{ext}"

    # Paso 1: generar archivo
    generar_datos(nombre_archivo, extension=ext)

    # Paso 2: leer datos con pandas
    df = leer_archivo(nombre_archivo)

    # Paso 3: generar modelo estrella
    generar_modelo_estrella(df, nombre_salida=f"modelo_datos_ventas_{i}")

    # Paso 4: mover archivo original
    mover_a_leidos(nombre_archivo)

print("\nProceso completado: 5 modelos de datos generados.")

