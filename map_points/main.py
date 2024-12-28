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
from utils.distance import calculate_distance, process_location


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

    map_view = initialize_map(secured_area)

    # Añadir marcadores e iconos del agresor
    add_aggressor_markers(map_view, aggressor_data, is_victim=False)

    # Añadir la zona segura
    add_safe_zone(map_view, secured_area, proximity_distance)

    # Verificar la proximidad de la víctima con el agresor
    for _, victim_row in victim_data.iterrows():
        victim_coordinates = process_location(victim_row, location_column="location")

        if victim_coordinates:
            victim_lat, victim_lng = victim_coordinates

        for _, aggressor_row in aggressor_data.iterrows():
            aggressor_coordinates = process_location(aggressor_row, location_column="location")

            if aggressor_coordinates:
                aggressor_lat, aggressor_lng = aggressor_coordinates

            # Calcular la distancia entre la víctima y el agresor
            distance = calculate_distance(
                (victim_lat, victim_lng), (aggressor_lat, aggressor_lng)
            )
            # Si la víctima está a 200 metros o menos del agresor, se añade la zona de la víctima
            if distance <= proximity_distance:
                time = victim_row.get("time", "N/A")
                precision = victim_row.get("precision", "N/A")
                add_victim_zone(
                    map_view,
                    (victim_lat, victim_lng),
                    proximity_distance,
                    time=time,
                    precision=precision,
                )

    save_map(map_view, result_folder, output_map)


if __name__ == "__main__":
    main()
