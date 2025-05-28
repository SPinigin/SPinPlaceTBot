from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config.config import Config
from keyboards.keyboards import Keyboards

class InfoHandler:
    @staticmethod
    async def handle_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()

        if query.data == 'rules':
            await InfoHandler.show_rules(query)
        elif query.data == 'directions':
            await InfoHandler.show_directions(query)
        elif query.data == 'check_in_out':
            await InfoHandler.show_check_in_out(query)
        elif query.data == 'faq':
            await InfoHandler.show_faq(query)

    @staticmethod
    async def show_rules(query):
        rules_text = """
📜 Правила проживания в коттедже:

1. Общие правила:
   • Время заезда: 14:00
   • Время выезда: 12:00
   • Курение разрешено только на улице
   • Проживание с домашними животными по согласованию

2. Бронирование и оплата:
   • Предоплата 20% для гарантии бронирования
   • Полная оплата при заселении
   • Возврат предоплаты при отмене за 7 дней

3. Правила поведения:
   • Соблюдение тишины с 23:00 до 8:00
   • Бережное отношение к имуществу
   • Запрет на проведение шумных мероприятий

4. Ответственность:
   • Гости несут ответственность за порчу имущества
   • При заселении вносится возвратный депозит 5000 руб.

5. Уборка и обслуживание:
   • Ежедневная уборка не входит в стоимость
   • Смена белья раз в 5 дней
   • Дополнительная уборка по запросу

6. Безопасность:
   • Закрывайте двери и окна при выходе
   • Не оставляйте ценные вещи без присмотра
   • В случае ЧП звоните администратору
"""
        keyboard = [[InlineKeyboardButton("« Назад", callback_data='info')]]
        await query.edit_message_text(
            text=rules_text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    @staticmethod
    async def show_directions(query):
        directions_text = """
🚗 Как добраться до коттеджа:

📍 Наш адрес:
[Ваш адрес]

🚘 На автомобиле:
1. Описание маршрута по основной дороге
2. Ключевые повороты и ориентиры
3. Где припарковаться

🚇 На общественном транспорте:
1. От ближайшей станции метро/вокзала
2. Номера автобусов/маршруток
3. Время в пути

🚕 На такси:
• Рекомендуемые службы такси
• Примерная стоимость
• Ориентиры для водителя

📱 Координаты для навигатора:
[Широта, Долгота]

❗️ Важные замечания:
• Особенности дороги
• Где лучше свернуть
• Характерные ориентиры

📞 При возникновении трудностей:
Звоните администратору: {Config.ADMIN_CONTACT}
"""
        keyboard = [[InlineKeyboardButton("« Назад", callback_data='info')]]
        await query.edit_message_text(
            text=directions_text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    @staticmethod
    async def show_check_in_out(query):
        check_info_text = """
🕒 Заселение и выселение:

📥 Заселение (Check-in):
• Время: с 14:00
• Необходимые документы: паспорт
• Процедура заселения:
  1. Встреча с администратором
  2. Осмотр коттеджа
  3. Подписание акта приема-передачи
  4. Внесение депозита
  5. Получение ключей

📤 Выселение (Check-out):
• Время: до 12:00
• Процедура выселения:
  1. Осмотр коттеджа администратором
  2. Подписание акта возврата
  3. Возврат депозита
  4. Сдача ключей

⚠️ Важно:
• Ранний заезд и поздний выезд по предварительной договоренности
• Доплата за ранний заезд: 500 руб/час
• Доплата за поздний выезд: 500 руб/час
• Предварительное бронирование обязательно

📞 Контакты администратора:
{Config.ADMIN_CONTACT}
"""
        keyboard = [[InlineKeyboardButton("« Назад", callback_data='info')]]
        await query.edit_message_text(
            text=check_info_text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    @staticmethod
    async def show_faq(query):
        faq_text = """
❓ Часто задаваемые вопросы (FAQ):

🏠 О коттедже:
Q: Какая площадь коттеджа?
A: [Площадь] м²

Q: Сколько спален в коттедже?
A: [Количество] спален

Q: Есть ли парковка?
A: Да, на 2 автомобиля

💰 Оплата и бронирование:
Q: Как забронировать коттедж?
A: Через бот или сайт с внесением предоплаты

Q: Какие способы оплаты принимаются?
A: Наличные, перевод на карту, безналичный расчет

Q: Возвращается ли предоплата при отмене?
A: Да, при отмене за 7 дней до заезда

🏡 Проживание:
Q: Есть ли Wi-Fi?
A: Да, бесплатный высокоскоростной

Q: Можно ли с детьми?
A: Да, есть детская площадка

Q: Можно ли с животными?
A: По предварительному согласованию

🛎 Сервис:
Q: Есть ли уборка?
A: При заезде и выезде, дополнительно по запросу

Q: Предоставляется ли постельное белье?
A: Да, включено в стоимость

Q: Есть ли мангальная зона?
A: Да, с предоставлением дров

⚠️ Особые случаи:
Q: Что делать при поломке?
A: Немедленно сообщить администратору

Q: Можно ли продлить проживание?
A: При отсутствии следующего бронирования

📞 Дополнительные вопросы:
Звоните: {Config.ADMIN_CONTACT}
Email: {Config.EMAIL}
"""
        keyboard = [[InlineKeyboardButton("« Назад", callback_data='info')]]
        await query.edit_message_text(
            text=faq_text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

def register_info_handlers(application):
    """Регистрация обработчиков информационного раздела"""
    application.add_handler(
        CallbackQueryHandler(
            InfoHandler.handle_info,
            pattern='^(info|rules|directions|check_in_out|faq)$'
        )
    )
