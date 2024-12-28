from geopy.distance import geodesic


def calculate_distance(coord1, coord2):
    """
    Calcula la distancia en metros entre dos coordenadas geográficas usando la librería geopy.

    :param coord1: Tupla (latitud, longitud) del primer punto.
    :param coord2: Tupla (latitud, longitud) del segundo punto.
    :return: Distancia en metros entre los dos puntos.
    """
    return geodesic(coord1, coord2).meters


def process_location(data_row, location_column="location"):
    """Procesa la ubicación de un dato, extrayendo las coordenadas de latitud y longitud."""
    location = data_row[location_column]

    # Asegurarnos de que location sea una cadena
    if isinstance(location, float):
        print(f"Valor inesperado en '{location_column}': {location}. Ignorando fila.")
        return None  # Retorna None si location es un flotante

    # Si es una cadena, intentamos dividirla
    try:
        lat, lng = map(float, location.split(","))
        return lat, lng
    except ValueError:
        print(
            f"Ubicación no válida en '{location_column}': {location}. Ignorando fila."
        )
        return None
