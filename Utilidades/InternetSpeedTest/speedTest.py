import speedtest

st = speedtest.Speedtest()

# Verificamos la velocidad de descarga
print(st.download())

# Verificamos la velocidad de carga
print(st.upload())

# Verificamos el ping
print(st.results.ping)
