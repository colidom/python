import pywhatkit as kit
 
# Usamos Un try-except
try: 
 
  # Enviamos el mensaje
 
  kit.sendwhatmsg("+34xxxxxxxxxx2",  
                        "Mensaje De Prueba",
                        15,5) 
 
  print("Mensaje Enviado") 
 
  
 
except: 
 
  print("Ocurrio Un Error")
