from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from Controller.funciones import (
    procesar_datos_csv,
    procesar_estadisticas,
    procesar_imagen_grafico,
    procesar_dashboard_html
)

app = FastAPI(title="Dashboard de Ventas")

@app.get("/datos")
def datos():
    return procesar_datos_csv()

@app.get("/estadisticas")
def estadisticas():
    return procesar_estadisticas()

@app.get("/grafico/barras")
def grafico_barras():
    imagen = procesar_imagen_grafico("barras")
    return Response(content=imagen, media_type="image/png")

@app.get("/grafico/lineas")
def grafico_lineas():
    imagen = procesar_imagen_grafico("lineas")
    return Response(content=imagen, media_type="image/png")

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return procesar_dashboard_html()