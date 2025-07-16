import pandas as pd
import os

def leer_archivos_leidos():
    archivos = [f for f in os.listdir("leidos") if f.endswith(".csv") or f.endswith(".xlsx")]
    todos = []

    for archivo in archivos:
        ruta = os.path.join("leidos", archivo)
        try:
            if archivo.endswith(".csv"):
                df = pd.read_csv(ruta)
            else:
                df = pd.read_excel(ruta)
            todos.append(df)
            print(f"Cargado: {archivo}")
        except Exception as e:
            print(f"Error al leer {archivo}: {e}")
    
    if not todos:
        raise ValueError("No se encontraron archivos válidos en la carpeta 'leidos'")
    
    return pd.concat(todos, ignore_index=True)

def generar_resumen(df):
    df["Total"] = df["Cantidad"] * df["Precio Unitario"]

    resumen = {}

    resumen["Producto más vendido (cantidad)"] = df.groupby("Producto")["Cantidad"].sum().idxmax()
    resumen["Producto menos vendido (cantidad)"] = df.groupby("Producto")["Cantidad"].sum().idxmin()

    resumen["Producto que generó más ingresos"] = df.groupby("Producto")["Total"].sum().idxmax()
    resumen["Producto que generó menos ingresos"] = df.groupby("Producto")["Total"].sum().idxmin()

    resumen["Total de ingresos"] = round(df["Total"].sum(), 2)

    resumen["Cliente que más compró (cantidad)"] = df.groupby("Cliente")["Cantidad"].sum().idxmax()
    resumen["Cliente que más gastó"] = df.groupby("Cliente")["Total"].sum().idxmax()

    resumen["Método de pago más usado"] = df["Método de Pago"].value_counts().idxmax()

    return resumen

def guardar_resumen_excel(df, resumen_dict):
    if not os.path.exists("resumen"):
        os.makedirs("resumen")

    df.to_excel("resumen/datos_consolidados.xlsx", index=False)

    resumen_df = pd.DataFrame(list(resumen_dict.items()), columns=["Métrica", "Resultado"])
    resumen_df.to_excel("resumen/resumen_ventas.xlsx", index=False)

    print("Resumen generado en carpeta 'resumen/'")

# ================ EJECUCIÓN ================
df_consolidado = leer_archivos_leidos()
resumen = generar_resumen(df_consolidado)
guardar_resumen_excel(df_consolidado, resumen)
