import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38])
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100])

# Añadimos una capa para este ejemplo
# capa = tf.keras.layers.Dense(units=1, input_shape=[1])
# modelo = tf.keras.Sequential([capa])

# Añadimos varias capas intermedias con tres neuronas
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 =tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error')

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado!")

# Resultado de la función de pérdida
import matplotlib.pyplot as plt
plt.xlabel("# Etapa")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])


# Hacemos una predicción
resultado = modelo.predict([100.0])
print(f"El resultado es {resultado} fahrenheit!")

# Variables internas del módulo
# print(capa.get_weights())
# print(oculta1.get_weights())
# print(oculta2.get_weights())
# print(salida.get_weights())
