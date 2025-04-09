import time
from utils import load_config, load_coordinates, get_next_coordinate
from xml_util import create_xml
from request_handler import send_request


config = load_config()

if __name__ == "__main__":
    coordinates_v_df = load_coordinates(config["DATA_PATH_V"])
    coordinates_a_df = load_coordinates(config["DATA_PATH_A"])

    index = 0
    while True:
        # Enviar datos del dispositivo de la víctima
        lat_v, lon_v, prec_v = get_next_coordinate(coordinates_v_df, index)
        xml_data_v, time_sent_v = create_xml(config["IMEI_V"], lat_v, lon_v, prec_v, config['EVENT_TYPE'], -2)
        send_request(index + 1, config["IMEI_V"], lat_v, lon_v, xml_data_v, "victimMessage", time_sent_v)

        # Enviar datos del dispositivo del inculpado
        lat_a, lon_a, prec_a = get_next_coordinate(coordinates_a_df, index)
        xml_data_a, time_sent_a = create_xml(config["IMEI_A"], lat_a, lon_a, prec_a, config['EVENT_TYPE'], -2)
        send_request(index + 1, config["IMEI_A"], lat_a, lon_a, xml_data_a, "aggressorMessage", time_sent_a)

        index += 1
        time.sleep(15)
