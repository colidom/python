import folium
from geopy.distance import geodesic
import os


def initialize_map(center, zoom_start=15):
    """Inicializa un mapa centrado en una ubicación específica."""
    return folium.Map(location=center, zoom_start=zoom_start)


def add_aggressor_markers(map_object, data, is_victim=True):
    """Agrega marcadores al mapa a partir de los datos proporcionados."""
    position = 1  # Empezamos en la posición 1
    for _, row in data.iterrows():
        try:
            location = row["location"]

            # Verificar si location es un número flotante o una cadena
            if isinstance(location, str):
                # Si es una cadena, intentamos dividirla
                lat, lng = map(float, location.split(","))
            elif isinstance(location, float):
                # Si es un flotante, lo ignoramos o realizamos algún tipo de procesamiento (si corresponde)
                print(f"Valor inesperado en 'location': {location}")
                continue  # Si es un flotante, ignoramos esta fila por ahora.
            else:
                print(f"Tipo no esperado en 'location': {type(location)}")
                continue  # Si el tipo no es ni str ni float, ignoramos la fila.

            precision = row.get("precision", "N/A")
            time = row.get("time", "N/A")

            if lat != 0.0 and lng != 0.0:
                tooltip_text = f"<b>Position:</b> {position}<br><b>Lon:</b> {lng}<br><b>Lat:</b> {lat}</br><b>Time:</b> {time}<br><b>Precision:</b> {precision}"
                icon_color = (
                    "green" if is_victim else "red"
                )  # Cambiar color según si es víctima o agresor
                folium.Marker(
                    location=(lat, lng),
                    tooltip=tooltip_text,
                    icon=folium.Icon(
                        color=icon_color,
                        icon="home" if is_victim else "male",
                        prefix="fa",
                    ),
                ).add_to(map_object)
                position += 1
        except Exception as e:
            print(f"Error procesando fila: {row} - {e}")


def add_safe_zone(map_object, secured_area, proximity_distance):
    """Agrega un marcador y un círculo de proximidad para la zona segura con información detallada."""
    lat, lng = secured_area
    tooltip_text = f"<b>Lon:</b> {lng}<br>" f"<b>Lat:</b> {lat}<br>"

    # Agregar marcador para la zona segura
    folium.Marker(
        location=secured_area,
        tooltip=tooltip_text,
        icon=folium.Icon(color="blue", icon="home", prefix="fa"),
    ).add_to(map_object)

    # Agregar círculo para la zona de proximidad de la zona segura
    folium.Circle(
        location=secured_area,
        radius=proximity_distance,
        color="blue",
        fill=True,
        fill_opacity=0.2,
        tooltip=f"Secured Area: {proximity_distance}m",
    ).add_to(map_object)


def add_victim_zone(
    map_object,
    victim_location,
    proximity_distance,
    time="N/A",
    precision="N/A",
):
    """Agrega un círculo de proximidad y un marcador para la víctima con información detallada."""
    lat, lng = victim_location
    tooltip_text = (
        f"<b>Lon:</b> {lng}<br>"
        f"<b>Lat:</b> {lat}<br>"
        f"<b>Time:</b> {time}<br>"
        f"<b>Precision:</b> {precision}"
    )

    # Agregar marcador para la ubicación de la víctima
    folium.Marker(
        location=victim_location,
        tooltip=tooltip_text,
        icon=folium.Icon(color="green", icon="female", prefix="fa"),
    ).add_to(map_object)

    folium.Circle(
        location=victim_location,
        radius=proximity_distance,
        color="green",
        fill=False,
        fill_opacity=0.2,
        tooltip=f"Victim's Zone: {proximity_distance}m",
    ).add_to(map_object)


def save_map(map_object, result_folder, output_file):
    """Guarda el mapa en un archivo HTML."""
    os.makedirs(result_folder, exist_ok=True)
    map_object.save(os.path.join(result_folder, output_file))
    print(f"Mapa generado exitosamente: {os.path.join(result_folder, output_file)}")
