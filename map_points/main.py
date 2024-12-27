import os
from map_points.utils.filesystem import get_csv_file, read_data, create_directories
from map_points.utils.map import initialize_map, add_markers, add_safe_zone, save_map


def main():
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
    secured_area = (37.5531099, -3.63737)
    proximity_distance = 200  # Distancia en metros

    # Flujo principal
    csv_file = get_csv_file(data_folder)
    data = read_data(csv_file)

    m = initialize_map(secured_area)
    add_markers(m, data)
    add_safe_zone(m, secured_area, proximity_distance)
    save_map(m, result_folder, output_map)


if __name__ == "__main__":
    main()
