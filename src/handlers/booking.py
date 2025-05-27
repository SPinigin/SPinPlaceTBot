from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from datetime import datetime
from database.db_operations import DatabaseManager
from utils.validators import validate_dates, validate_guests
from config.config import Config

CHOOSING_DATE, ENTERING_GUESTS, ENTERING_CONTACT = range(3)


async def start_booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.message.reply_text(
        "Для бронирования укажите даты заезда и выезда в формате:\n"
        "ДД.ММ.ГГГГ-ДД.ММ.ГГГГ"
    )
    return CHOOSING_DATE


async def process_dates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        dates = update.message.text.split('-')
        check_in = datetime.strptime(dates[0].strip(), '%d.%m.%Y')
        check_out = datetime.strptime(dates[1].strip(), '%d.%m.%Y')

        if not validate_dates(check_in, check_out):
            await update.message.reply_text(
                "Неверные даты. Минимальный срок бронирования - 1 день, "
                f"максимальный - {Config.MAX_BOOKING_DAYS} дней."
            )
            return CHOOSING_DATE

        if not DatabaseManager.check_availability(check_in, check_out):
            await update.message.reply_text(
                "Извините, эти даты уже забронированы. Пожалуйста, выберите другие даты."
            )
            return CHOOSING_DATE

        context.user_data['check_in'] = check_in
        context.user_data['check_out'] = check_out

        await update.message.reply_text(
            f"Укажите количество гостей (максимум {Config.MAX_GUESTS} человек):"
        )
        return ENTERING_GUESTS

    except Exception as e:
        await update.message.reply_text(
            "Неверный формат дат. Используйте формат ДД.ММ.ГГГГ-ДД.ММ.ГГГГ"
        )
        return CHOOSING_DATE


async def process_guests(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        guests = int(update.message.text)
        if not validate_guests(guests):
            raise ValueError

        context.user_data['guests'] = guests
        await update.message.reply_text(
            "Укажите ваши контактные данные в формате:\n"
            "Имя, телефон"
        )
        return ENTERING_CONTACT

    except:
        await update.message.reply_text(
            f"Пожалуйста, введите корректное число гостей (от 1 до {Config.MAX_GUESTS})"
        )
        return ENTERING_GUESTS


async def process_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact_info = update.message.text
    context.user_data['contact'] = contact_info

    # Расчет стоимости
    days = (context.user_data['check_out'] - context.user_data['check_in']).days
    total_price = days * 5000  # Примерная стоимость за сутки
    deposit = total_price * (Config.DEPOSIT_PERCENTAGE / 100)

    # Создание бронирования в БД
    booking = DatabaseManager.create_booking(
        user_id=update.effective_user.id,
        check_in=context.user_data['check_in'],
        check_out=context.user_data['check_out'],
        guests=context.user_data['guests'],
        contact_info=contact_info,
        total_price=total_price
    )

    confirmation_text = (
        "🎉 Предварительное бронирование создано!\n\n"
        f"Даты: {context.user_data['check_in'].strftime('%d.%m.%Y')} - "
        f"{context.user_data['check_out'].strftime('%d.%m.%Y')}\n"
        f"Гостей: {context.user_data['guests']}\n"
        f"Контакты: {contact_info}\n"
        f"Общая стоимость: {total_price} руб.\n"
        f"Депозит (для подтверждения): {deposit} руб.\n\n"
        "Для подтверждения бронирования необходимо внести депозит.\n"
        "Реквизиты для оплаты будут отправлены в следующем сообщении."
    )

    await update.message.reply_text(confirmation_text)
    return ConversationHandler.END
