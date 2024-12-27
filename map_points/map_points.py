import os
import pandas as pd
import folium

# Configuración de carpetas
data_folder = "data"
result_folder = "result"

# Detectar automáticamente el único archivo CSV en la carpeta "data"
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]
if len(csv_files) != 1:
    raise ValueError(f"Se esperaba un único archivo CSV en '{data_folder}', pero se encontraron {len(csv_files)} archivos.")

csv_file = os.path.join(data_folder, csv_files[0])
output_map = os.path.join(result_folder, "map_points.html")

# Leer el archivo CSV
data = pd.read_csv(csv_file)

# Configurar la zona segura y proximidad
secured_area = (37.5531099, -3.63737)
proximity_distance = 200  # Distancia en metros

# Crear el mapa centrado en la zona segura
m = folium.Map(location=secured_area, zoom_start=15)

# Procesar las filas del CSV y agregar puntos al mapa
for _, row in data.iterrows():
    try:
        # Extraer coordenadas y otra información relevante
        lat, lng = map(float, row["location"].split(","))  # Suponiendo que "location" tiene el formato "lat,lng"
        precision = row.get("precision", "N/A")
        time = row.get("time", "N/A")
        
        # Ignorar coordenadas inválidas como (0.0, 0.0)
        if lat != 0.0 and lng != 0.0:
            popup_text = f"<b>Time:</b> {time}<br><b>Precision:</b> {precision}"
            folium.Marker(
                location=(lat, lng),
                popup=popup_text,
                icon=folium.Icon(color="red", icon="male", prefix="fa")
            ).add_to(m)
    except Exception as e:
        print(f"Error procesando fila: {row} - {e}")

# Agregar marcador para la zona segura
folium.Marker(
    location=secured_area,
    popup="Secured Area",
    icon=folium.Icon(color="green", icon="home", prefix="fa")
).add_to(m)

# Agregar un círculo de proximidad alrededor de la zona segura
folium.Circle(
    location=secured_area,
    radius=proximity_distance,
    color="green",
    fill=True,
    fill_opacity=0.2,
    popup=f"Proximity Zone: {proximity_distance}m"
).add_to(m)

# Guardar el mapa en formato HTML
os.makedirs(result_folder, exist_ok=True)
m.save(output_map)
print(f"Mapa generado exitosamente: {output_map}")
