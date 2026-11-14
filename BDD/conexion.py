from pathlib import Path
import pandas as pd

# Ubicación del dataset dentro de la carpeta BDD o raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
ARCHIVO = BASE_DIR / "ventas.csv"

def crear_dataset():
    """Crea el archivo CSV con datos por defecto si no existe."""
    if not ARCHIVO.exists():
        datos = {
            "mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
            "ventas": [1200, 1800, 1500, 2300, 2800, 3500],
            "clientes": [25, 32, 29, 40, 46, 58]
        }
        df = pd.DataFrame(datos)
        df.to_csv(ARCHIVO, index=False)

def obtener_datos():
    """Lee y retorna el DataFrame desde el archivo CSV."""
    crear_dataset()
    return pd.read_csv(ARCHIVO)