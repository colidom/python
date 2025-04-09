import requests
from utils import load_config
from datetime import datetime
import urllib3
from requests.exceptions import ConnectionError, Timeout, RequestException

config = load_config()
URL = config["URL"]
HEADERS = config["HEADERS"]

def send_request(iteration, imei, latitude, longitude, xml_data, request_type, time_sent):
    """Envía la solicitud POST con el XML y traza los datos enviados."""
    endpoint = f"/services/{request_type}?postParameter=payload"
    full_url = f"{URL}{endpoint}"
    now_local = datetime.now().strftime("%H:%M:%S")

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        response = requests.post(full_url, headers=HEADERS, data=xml_data, verify=False)

        print(f"\nPetición: {iteration}")
        print(f"Dispositivo: {imei}")
        print(f"Longitud: {longitude}")
        print(f"Latitud: {latitude}")
        print(f"Hora de la petición (local): {now_local}")
        print(f"Hora enviada en XML (ajustada): {time_sent}")
        print(f"Código de respuesta: {response.status_code}\n")

    except ConnectionError:
        print(f"\n❌ Error de conexión en la petición {iteration}. Posiblemente se ha caído la red o la VPN.")
    except Timeout:
        print(f"\n⏳ Tiempo de espera agotado en la petición {iteration}.")
    except RequestException as e:
        print(f"\n⚠️ Error inesperado en la petición {iteration}: {e}")
