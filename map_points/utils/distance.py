from geopy.distance import geodesic


def calculate_distance(coord1, coord2):
    """
    Calcula la distancia en metros entre dos coordenadas geográficas usando la librería geopy.

    :param coord1: Tupla (latitud, longitud) del primer punto.
    :param coord2: Tupla (latitud, longitud) del segundo punto.
    :return: Distancia en metros entre los dos puntos.
    """
    return geodesic(coord1, coord2).meters
