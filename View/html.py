def obtener_html(total: float, promedio: float, clientes_total: int) -> str:
    """Retorna la plantilla HTML completa con los datos inyectados."""
    return f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Dashboard de Ventas</title>
    <style>
        body {{
            font-family: Arial;
            background: #f0f4f8;
            padding: 30px;
        }}
        h1 {{
            color: #1e3a5f;
        }}
        .indicadores {{
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
        }}
        .tarjeta {{
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 8px #ddd;
            flex: 1;
            min-width: 160px;
        }}
        .graficos {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 25px;
        }}
        .graficos img {{
            width: 100%;
            max-width: 580px;
            border-radius: 10px;
            background: white;
        }}
    </style>
</head>
<body>
    <h1>Dashboard de Ventas</h1>
    <p>Análisis de datos con Python y FastAPI</p>
    
    <div class="indicadores">
        <div class="tarjeta">
            <h3>Ventas totales</h3>
            <h2>${total:,.2f}</h2>
        </div>
        <div class="tarjeta">
            <h3>Promedio mensual</h3>
            <h2>${promedio:,.2f}</h2>
        </div>
        <div class="tarjeta">
            <h3>Clientes registrados</h3>
            <h2>{clientes_total}</h2>
        </div>
    </div>
    
    <div class="graficos">
        <img src="/grafico/barras">
        <img src="/grafico/lineas">
    </div>
    
    <p>
        <a href="/datos">Ver Dataset</a> | 
        <a href="/estadisticas">Ver estadísticas</a> | 
        <a href="/docs">Documentación API</a>
    </p>
</body>
</html>
"""