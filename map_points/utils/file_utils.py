import os
import pandas as pd


def get_csv_file(data_folder):
    """Detecta automáticamente el único archivo CSV en una carpeta dada."""
    csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]
    if len(csv_files) != 1:
        raise ValueError(
            f"Se esperaba un único archivo CSV en '{data_folder}', pero se encontraron {len(csv_files)} archivos."
        )
    return os.path.join(data_folder, csv_files[0])


def read_data(csv_file):
    """Lee un archivo CSV y lo devuelve como un DataFrame."""
    return pd.read_csv(csv_file)


def create_directories(directories):
    """Crea múltiples directorios si no existen."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
