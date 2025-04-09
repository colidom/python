import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from utils import load_config

config = load_config()

def create_xml(imei, latitude, longitude, precision, event_type, hour_offset=0):
    """Genera el XML con la hora local actual ajustada según hour_offset."""
    now_adjusted = (datetime.now() - timedelta(hours=abs(hour_offset))).strftime("%Y-%m-%d %H:%M:%S")
    
    message = ET.Element("Message")
    sender = ET.SubElement(message, "Sender")
    sender.text = config["SENDER"]
    
    device = ET.SubElement(message, "Device")
    imei_elem = ET.SubElement(device, "Imei")
    imei_elem.text = imei
    battery = ET.SubElement(device, "Battery")
    battery.text = config["BATTERY"]
    
    bracelet = ET.SubElement(message, "Bracelet")
    battery_b = ET.SubElement(bracelet, "BatteryB")
    battery_b.text = config["BATTERY_B"]
    temp_b = ET.SubElement(bracelet, "TempB")
    temp_b.text = config["TEMP_B"]
    
    event_type_elem = ET.SubElement(message, "EventType")
    event_type_elem.text = event_type
    
    time_elem = ET.SubElement(message, "Time")
    time_elem.text = now_adjusted  # Se usa la hora ajustada a enviar en el XML
    
    position = ET.SubElement(message, "Position")
    lon = ET.SubElement(position, "Longitude")
    lon.text = longitude
    lat = ET.SubElement(position, "Latitude")
    lat.text = latitude
    alt = ET.SubElement(position, "Altitude")
    alt.text = config["ALTITUDE"]
    prec = ET.SubElement(position, "Precision")
    prec.text = precision
    
    # data = ET.SubElement(message, "Data")
    
    return ET.tostring(message, encoding="utf-8", method="xml").decode("utf-8"), now_adjusted 
