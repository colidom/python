import os
import re
import requests
from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# Importar el diccionario desde el archivo numeros_significados.py
from numeros_significados import numeros_significados

# Cargar variables de entorno desde el archivo .env
load_dotenv()
TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")


# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"¡Hola {update.effective_user.first_name}! Bienvenido, me llamo Bender y soy un bot 🤖"
    )


# Función para manejar mensajes de texto
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text.lower()
    user_name = update.effective_user.first_name

    # Patrón regex para detectar preguntas sobre el significado de un número
    numero_pregunta_patron = re.compile(
        r"cu[aá]l es el significado del n[uú]mero (\d{2})"
    )

    # Verificar si el texto contiene una pregunta sobre un número
    match = numero_pregunta_patron.search(user_text)
    if match:
        numero = match.group(1)  # Extraer el número de la pregunta
        palabras = numeros_significados.get(numero, [])
        if palabras:
            respuesta = f"El número {numero} está asociado con: {', '.join(palabras)}"
        else:
            respuesta = f"No hay palabras asociadas al número {numero}"

        await update.message.reply_text(respuesta)
    else:
        # Aquí va el resto de los casos que el bot maneja
        match user_text:
            case text if "hola" in text:
                await update.message.reply_text(f"Hola {user_name}, ¡bienvenido! 😊")
            case text if "adiós" in text or "chao" in text:
                await update.message.reply_text(f"¡Hasta luego, {user_name}! 👋")
            case text if "gracias" in text:
                await update.message.reply_text(f"¡De nada, {user_name}! 😊")
            case text if "cómo estás" in text:
                await update.message.reply_text(
                    f"¡Estoy muy bien, {user_name}! ¿Y tú? 😄"
                )
            case text if "buenos días" in text:
                await update.message.reply_text(
                    f"¡Buenos días, {user_name}! ☀️ Espero que tengas un gran día."
                )
            case text if "buenas noches" in text:
                await update.message.reply_text(
                    f"¡Buenas noches, {user_name}! 🌙 Que descanses."
                )
            case text if "cuéntame un chiste" in text:
                await update.message.reply_text(
                    "¿Por qué el libro de matemáticas estaba triste? ¡Porque tenía demasiados problemas! 😂"
                )
            case text if "cuál es tu nombre" in text:
                await update.message.reply_text(
                    "Soy Bender, un bot amigable, siempre aquí para ayudarte. 🤖"
                )
            case text if "eres muy gracioso" in text:
                await update.message.reply_text(
                    f"¡Me alegra que pienses eso, {user_name}! 😄"
                )
            case text if "previsión del tiempo" in text:
                if update.message.chat.type == "private":
                    await update.message.reply_text(
                        "Por favor, comparte tu ubicación para decirte el clima actual. 🌍",
                        reply_markup=ReplyKeyboardMarkup(
                            [
                                [
                                    KeyboardButton(
                                        "Compartir ubicación 📍", request_location=True
                                    )
                                ]
                            ],
                            one_time_keyboard=True,
                            resize_keyboard=True,
                        ),
                    )
                else:
                    await update.message.reply_text(
                        "Para saber el clima actual, compárteme tu ubicación en un mensaje privado haciendo clic aquí: t.me/bender0_bot 🌍"
                    )


# Función para manejar la ubicación del usuario
async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lat = update.message.location.latitude
    lon = update.message.location.longitude

    # API de OpenWeatherMap
    TOKEN_OPENWEATHER = os.getenv("TOKEN_OPENWEATHER")
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={TOKEN_OPENWEATHER}&units=metric&lang=es"

    response = requests.get(url).json()

    # Verificar si hay datos en la respuesta
    if "list" in response:
        # Usar el primer pronóstico para otras informaciones
        first_forecast = response["list"][0]
        weather_description = first_forecast["weather"][0]["description"]
        temperature = first_forecast["main"]["temp"]
        city = response["city"]["name"]

        # Acceder a la sensación térmica, humedad, presión y velocidad del viento
        feels_like = first_forecast["main"]["feels_like"]  # Sensación térmica
        humidity = first_forecast["main"]["humidity"]  # Humedad
        pressure = first_forecast["main"]["pressure"]  # Presión
        wind_speed = first_forecast["wind"]["speed"]  # Velocidad del viento

        # Determinar el icono basado en la temperatura
        if temperature < 20:
            temp_icon = "🥶"  # Frío
        elif 20 <= temperature <= 26:
            temp_icon = "😊"  # Bienestar
        else:
            temp_icon = "🥵"  # Calor

        await update.message.reply_text(
            f"El tiempo en {city} es: {weather_description} con una temperatura de {temperature}°C 🌡️\n"
            f"Pero se siente como {feels_like}°C {temp_icon}\n"
            f"Humedad: {humidity}% 💧\n"
            f"Presión: {pressure} hPa ☁️\n"
            f"Velocidad del viento: {wind_speed} m/s 💨\n"
        )
    else:
        await update.message.reply_text(
            "No pude obtener el clima en este momento, intenta de nuevo más tarde. ❌"
        )


# Función para manejar errores
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"Update {update} caused error {context.error}")


# Configuración del bot
if __name__ == "__main__":
    # Crear la aplicación del bot
    application = ApplicationBuilder().token(TOKEN_TELEGRAM).build()

    # Registrar los manejadores de comandos y mensajes
    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    application.add_handler(MessageHandler(filters.LOCATION, handle_location))

    # Manejo de errores
    application.add_error_handler(error_handler)

    # Iniciar el bot
    print("Bot corriendo...")
    application.run_polling()
