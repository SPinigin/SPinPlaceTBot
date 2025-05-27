from telegram import Update
from telegram.ext import ContextTypes
from keyboards.keyboards import Keyboards
import os
from config.config import Config


async def handle_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'description':
        with open(Config.COTTAGE_DESCRIPTION, 'r', encoding='utf-8') as file:
            description = file.read()
        await query.edit_message_text(
            text=description,
            reply_markup=Keyboards.about_menu()
        )

    elif query.data == 'photos':
        photos_dir = Config.IMAGES_PATH
        for photo in os.listdir(photos_dir):
            with open(os.path.join(photos_dir, photo), 'rb') as photo_file:
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=photo_file
                )

    elif query.data == 'amenities':
        amenities_text = """
        🏠 Удобства в коттедже:

        ✓ 3 спальни
        ✓ 2 санузла
        ✓ Полностью оборудованная кухня
        ✓ Бесплатный Wi-Fi
        ✓ Кондиционеры
        ✓ Телевизор Smart TV
        ✓ Парковка на 2 машины
        ✓ Мангальная зона
        ✓ Придомовая территория
        """
        await query.edit_message_text(
            text=amenities_text,
            reply_markup=Keyboards.about_menu()
        )
