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
TOKEN_TELEGRAM = os.getenv("TOKEN_TELEGRAM")


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

    # Manejo de las respuestas según el texto del usuario
    match user_text:
        case text if "hola" in text:
            await update.message.reply_text(f"Hola {user_name}, ¡bienvenido! 😊")
        case text if "adiós" in text or "chao" in text:
            await update.message.reply_text(f"¡Hasta luego, {user_name}! 👋")
        case text if "gracias" in text:
            await update.message.reply_text(f"¡De nada, {user_name}! 😊")
        case text if "cómo estás" in text:
            await update.message.reply_text(f"¡Estoy muy bien, {user_name}! ¿Y tú? 😄")
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
        case _:
            await update.message.reply_text("Lo siento, no entiendo ese mensaje. 🤖")


# Función para manejar la ubicación del usuario
async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lat = update.message.location.latitude
    lon = update.message.location.longitude

    # API de OpenWeatherMap
    TOKEN_OPENWEATHER = os.getenv("TOKEN_OPENWEATHER")
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={TOKEN_OPENWEATHER}&units=metric&lang=es"

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
