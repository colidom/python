import folium
import os


def initialize_map(center, zoom_start=15):
    """Inicializa un mapa centrado en una ubicación específica."""
    return folium.Map(location=center, zoom_start=zoom_start)


def add_markers(map_object, data):
    """Agrega marcadores al mapa a partir de los datos proporcionados."""
    for _, row in data.iterrows():
        try:
            lat, lng = map(float, row["location"].split(","))
            precision = row.get("precision", "N/A")
            time = row.get("time", "N/A")

            if lat != 0.0 and lng != 0.0:
                popup_text = f"<b>Time:</b> {time}<br><b>Precision:</b> {precision}"
                folium.Marker(
                    location=(lat, lng),
                    popup=popup_text,
                    icon=folium.Icon(color="red", icon="male", prefix="fa"),
                ).add_to(map_object)
        except Exception as e:
            print(f"Error procesando fila: {row} - {e}")


def add_safe_zone(map_object, secured_area, proximity_distance):
    """Agrega un marcador y un círculo de proximidad para la zona segura."""
    folium.Marker(
        location=secured_area,
        popup="Secured Area",
        icon=folium.Icon(color="green", icon="home", prefix="fa"),
    ).add_to(map_object)

    folium.Circle(
        location=secured_area,
        radius=proximity_distance,
        color="green",
        fill=True,
        fill_opacity=0.2,
        popup=f"Proximity Zone: {proximity_distance}m",
    ).add_to(map_object)


def save_map(map_object, result_folder, output_file):
    """Guarda el mapa en un archivo HTML."""
    os.makedirs(result_folder, exist_ok=True)
    map_object.save(os.path.join(result_folder, output_file))
    print(f"Mapa generado exitosamente: {os.path.join(result_folder, output_file)}")
