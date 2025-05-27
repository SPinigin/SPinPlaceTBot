from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🏡 О коттедже", callback_data='about')],
        [InlineKeyboardButton("📅 Забронировать", callback_data='book')],
        [InlineKeyboardButton("ℹ️ Важная информация", callback_data='info')],
        [InlineKeyboardButton("☎️ Контакты", callback_data='contacts')]
    ]
    return InlineKeyboardMarkup(keyboard)
