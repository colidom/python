from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()
TOKEN = os.getenv("TOKEN")


# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"¡Hola {update.effective_user.first_name}! Bienvenido, me llamo Bender y soy un bot 🤖"
    )


import requests


# Función para manejar mensajes de texto
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text.lower()
    user_name = update.effective_user.first_name

    if "hola" in user_text:
        await update.message.reply_text(f"Hola {user_name}, ¡bienvenido! 😊")
    elif "adiós" in user_text or "chao" in user_text:
        await update.message.reply_text(f"¡Hasta luego, {user_name}! 👋")
    elif "gracias" in user_text:
        await update.message.reply_text(f"¡De nada, {user_name}! 😊")
    elif "cómo estás" in user_text:
        await update.message.reply_text(f"¡Estoy muy bien, {user_name}! ¿Y tú? 😄")
    elif "buenos días" in user_text:
        await update.message.reply_text(
            f"¡Buenos días, {user_name}! ☀️ Espero que tengas un gran día."
        )
    elif "buenas noches" in user_text:
        await update.message.reply_text(
            f"¡Buenas noches, {user_name}! 🌙 Que descanses."
        )
    elif "cuéntame un chiste" in user_text:
        await update.message.reply_text(
            "¿Por qué el libro de matemáticas estaba triste? ¡Porque tenía demasiados problemas! 😂"
        )
    elif "cuál es tu nombre" in user_text:
        await update.message.reply_text(
            "Soy Bender, un bot amigable, siempre aquí para ayudarte. 🤖"
        )
    elif "eres muy gracioso" in user_text:
        await update.message.reply_text(f"¡Me alegra que pienses eso, {user_name}! 😄")
    elif "previsión del tiempo" in user_text:
        await update.message.reply_text(
            "Por favor, comparte tu ubicación para decirte el clima actual. 🌍",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Compartir ubicación 📍", request_location=True)]],
                one_time_keyboard=True,
                resize_keyboard=True,
            ),
        )


# Función para manejar la ubicación del usuario
async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lat = update.message.location.latitude
    lon = update.message.location.longitude

    # Llama a la API de OpenWeatherMap (debes reemplazar 'TU_API_KEY' con tu clave de API)
    api_key = "42bdcbdb5e34cde430eab4f8ad50a92f"
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=es"

    response = requests.get(url).json()

    # Procesar la respuesta de la API
    if response.get("weather"):
        weather_description = response["weather"][0]["description"]
        temperature = response["main"]["temp"]
        city = response["name"]
        await update.message.reply_text(
            f"El tiempo en {city} es: {weather_description} con una temperatura de {temperature}°C 🌡️"
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
    application = ApplicationBuilder().token(TOKEN).build()

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
