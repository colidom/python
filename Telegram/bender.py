from telegram import Update
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

    # Manejo de errores
    application.add_error_handler(error_handler)

    # Iniciar el bot
    print("Bot corriendo...")
    application.run_polling()
