from BDD.conexion import obtener_datos
from Model.graficos import generar_grafico
from View.html import obtener_html

def procesar_datos_csv():
    df = obtener_datos()
    return df.to_dict(orient="records")

def procesar_estadisticas():
    df = obtener_datos()
    mejor_mes_idx = df["ventas"].idxmax()
    return {
        "total_ventas": float(df["ventas"].sum()),
        "promedio_ventas": float(df["ventas"].mean()),
        "total_clientes": int(df["clientes"].sum()),
        "mejor_mes": str(df.loc[mejor_mes_idx, "mes"])
    }

def procesar_imagen_grafico(tipo: str):
    return generar_grafico(tipo)

def procesar_dashboard_html():
    df = obtener_datos()
    total = float(df["ventas"].sum())
    promedio = float(df["ventas"].mean())
    clientes_total = int(df["clientes"].sum())
    return obtener_html(total, promedio, clientes_total)