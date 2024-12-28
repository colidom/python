import os
from dotenv import load_dotenv
from utils.filesystem import get_csv_file, read_data, create_directories
from utils.map import (
    initialize_map,
    add_aggressor_markers,
    add_safe_zone,
    add_victim_zone,
    save_map,
)
from utils.distance import calculate_distance


def main():
    load_dotenv()
    # Establecer el directorio de trabajo al directorio del script actual
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Imprimir el directorio de trabajo actual para depuración
    print("Directorio actual:", os.getcwd())

    # Configuración de carpetas
    data_folder = os.path.join(script_dir, "data")
    result_folder = os.path.join(script_dir, "result")
    output_map = "map_points.html"

    create_directories([data_folder, result_folder])

    # Configuración de la zona segura y proximidad
    secured_area = (
        float(os.getenv("SECURED_AREA_LAT")),
        float(os.getenv("SECURED_AREA_LNG")),
    )
    proximity_distance = int(os.getenv("PROXIMITY_DISTANCE"))

    # Flujo principal
    Aggressor_file = get_csv_file(os.path.join(data_folder, "A"))  # Carpeta del agresor
    Victim_file = get_csv_file(os.path.join(data_folder, "V"))  # Carpeta de la víctima
    aggressor_data = read_data(Aggressor_file)
    victim_data = read_data(Victim_file)

    m = initialize_map(secured_area)

    # Añadir marcadores e iconos del agresor
    add_aggressor_markers(m, aggressor_data, is_victim=False)

    # Añadir la zona segura
    add_safe_zone(m, secured_area, proximity_distance)

    # Verificar la proximidad de la víctima con el agresor
    for _, victim_row in victim_data.iterrows():
        location = victim_row["location"]

        # Asegurarnos de que location sea una cadena
        if isinstance(location, float):
            print(
                f"Valor inesperado en 'location' de la víctima: {location}. Ignorando fila."
            )
            continue  # Ignorar fila si location es un flotante

        victim_lat, victim_lng = map(float, location.split(","))

        for _, aggressor_row in aggressor_data.iterrows():
            aggressor_location = aggressor_row["location"]

            # Asegurarnos de que location del agresor sea una cadena
            if isinstance(aggressor_location, float):
                print(
                    f"Valor inesperado en 'location' del agresor: {aggressor_location}. Ignorando fila."
                )
                continue  # Ignorar fila si location es un flotante

            aggressor_lat, aggressor_lng = map(float, aggressor_location.split(","))

            # Calcular la distancia entre la víctima y el agresor
            distance = calculate_distance(
                (victim_lat, victim_lng), (aggressor_lat, aggressor_lng)
            )
            # Si la víctima está a 200 metros o menos del agresor, se añade la zona de la víctima
            if distance <= proximity_distance:
                add_victim_zone(m, (victim_lat, victim_lng), proximity_distance)

    save_map(m, result_folder, output_map)


if __name__ == "__main__":
    main()
