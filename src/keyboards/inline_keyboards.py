from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboards:
    @staticmethod
    def main_menu():
        keyboard = [
            [InlineKeyboardButton("🏡 О коттедже", callback_data='about')],
            [InlineKeyboardButton("📅 Забронировать", callback_data='book')],
            [InlineKeyboardButton("ℹ️ Важная информация", callback_data='info')],
            [InlineKeyboardButton("☎️ Контакты", callback_data='contacts')],
            [InlineKeyboardButton("🗓 Мои бронирования", callback_data='my_bookings')]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def about_menu():
        keyboard = [
            [InlineKeyboardButton("📝 Описание", callback_data='description')],
            [InlineKeyboardButton("📸 Фотографии", callback_data='photos')],
            [InlineKeyboardButton("🛋 Удобства", callback_data='amenities')],
            [InlineKeyboardButton("💰 Стоимость", callback_data='price')],
            [InlineKeyboardButton("« Назад", callback_data='main_menu')]
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def info_menu():
        keyboard = [
            [InlineKeyboardButton("📜 Правила проживания", callback_data='rules')],
            [InlineKeyboardButton("🚗 Как добраться", callback_data='directions')],
            [InlineKeyboardButton("🕒 Заселение/выселение", callback_data='check_in_out')],
            [InlineKeyboardButton("❓ FAQ", callback_data='faq')],
            [InlineKeyboardButton("« Назад", callback_data='main_menu')]
        ]
        return InlineKeyboardMarkup(keyboard)
