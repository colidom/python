# coordinates-mock-sender

Este script envía periódicamente solicitudes POST con datos XML a un servicio web, utilizando coordenadas y precisión obtenidas de dos archivos Excel. Los datos enviados incluyen información sobre dos dispositivos (por ejemplo, un dispositivo de la víctima y otro del inculpado). El script lee las coordenadas de cada archivo Excel y las envía cada 15 segundos, alternando entre los dispositivos.

## Requisitos

- Python 3.6 o superior
- Librerías:
  - `requests`
  - `pandas`
  - `python-dotenv`
  - `openpyxl` (para leer archivos `.xlsx`)

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    ```
3. Activa el entorno virtual:
    - En Windows:
      ```bash
      venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Configuración

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno:

```bash
URL=tu_url_del_servicio
APP_KEY=tu_app_key
IMEI_V=imei_del_dispositivo_victima
IMEI_A=imei_del_dispositivo_inculpado
DATA_PATH_V=./data/coordinates_V.xlsx
DATA_PATH_A=./data/coordinates_A.xlsx
SENDER=Oysta
BATTERY=84.0
BATTERY_B=80.0
TEMP_B=0.0
EVENT_TYPE=CYC
ALTITUDE=179
```

- **URL**: La URL del servicio al que se enviarán las peticiones.
- **APP_KEY**: La clave de la aplicación que se usa en los encabezados de la petición.
- **IMEI_V**: El IMEI del dispositivo de la víctima.
- **IMEI_A**: El IMEI del dispositivo del inculpado.
- **DATA_PATH_V**: La ruta del archivo `.xlsx` que contiene las coordenadas del dispositivo de la víctima.
- **DATA_PATH_A**: La ruta del archivo `.xlsx` que contiene las coordenadas del dispositivo del inculpado.
- **SENDER**: El nombre del remitente (en este caso, "Intellicare").
- **BATTERY**: El porcentaje de batería del dispositivo.
- **BATTERY_B**: El porcentaje de batería de la pulsera.
- **TEMP_B**: La temperatura de la pulsera.
- **EVENT_TYPE**: El tipo de evento (en este caso, "CYC").
- **ALTITUDE**: La altitud en metros.

## Uso

1. Asegúrate de que el archivo `.env` está configurado correctamente.
2. Coloca los archivos de coordenadas `coordinates_V.xlsx` y `coordinates_A.xlsx` en el directorio `./data/`.
3. Ejecuta el script principal:
    ```bash
    python main.py
    ```
4. El script comenzará a enviar las solicitudes POST cada 15 segundos alternando entre las coordenadas de la víctima y el inculpado. Cada iteración de la solicitud será trazada en la consola con los datos del dispositivo, las coordenadas, la hora de la petición (local) y la hora ajustada enviada al servidor.

## Ejemplo de salida

```bash
Petición: 1
Dispositivo: 352701641669459
Longitud: -1.8317908
Latitud: 41.0714056
Hora de la petición (local): 16:09:31
Hora enviada en XML (ajustada -2h): 14:09:31
Código de respuesta: 200
```

## Notas

- El script usa la librería `requests` para enviar las solicitudes y `xml.etree.ElementTree` para generar los datos XML.
- Las coordenadas se extraen de los archivos Excel y se envían en el XML, alternando entre el dispositivo de la víctima y el del inculpado.
- El campo `<Time>` dentro del XML se ajusta con el parámetro `hour_offset`.
- Si no se desea verificar el certificado SSL (por ejemplo en entornos de pruebas), se puede usar `verify=False` en la petición, aunque esto mostrará advertencias de seguridad.
- Para suprimir estas advertencias, se utiliza el siguiente snippet:

```python
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
