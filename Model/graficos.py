import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
from BDD.conexion import obtener_datos

def generar_grafico(tipo: str) -> bytes:
    """Genera gráficos de barras o líneas y retorna la imagen en bytes."""
    df = obtener_datos()
    fig, ax = plt.subplots(figsize=(9, 4))
    
    if tipo == "barras":
        ax.bar(df["mes"], df["ventas"], color="royalblue")
        ax.set_title("Ventas por mes")
        ax.set_ylabel("Ventas ($)")
    else:
        ax.plot(df["mes"], df["clientes"], marker="o", color="green", linewidth=3)
        ax.set_title("Crecimiento de clientes")
        ax.set_ylabel("Clientes")
        
    ax.grid(axis="y", alpha=0.2)
    plt.xticks(rotation=25)
    plt.tight_layout()
    
    imagen = BytesIO()
    fig.savefig(imagen, format="png", dpi=120)
    plt.close(fig)
    
    return imagen.getvalue()