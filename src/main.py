import logging

from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from config.config import Config
from database.db_operations import DatabaseManager
from handlers.about import handle_about
from handlers.booking import (
    start_booking, process_dates, process_guests,
    process_contact, CHOOSING_DATE, ENTERING_GUESTS, ENTERING_CONTACT
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update, context):
    from keyboards.keyboards import Keyboards
    await update.message.reply_text(
        "Добро пожаловать! Выберите действие:",
        reply_markup=Keyboards.main_menu()
    )


def main():
    DatabaseManager.init_db()

    register_info_handlers(application)

    application = Application.builder().token(Config.BOT_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(handle_about, pattern='^(about|description|photos|amenities)$'))

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(start_booking, pattern='^book$')],
        states={
            CHOOSING_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_dates)],
            ENTERING_GUESTS: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_guests)],
            ENTERING_CONTACT: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_contact)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    application.add_handler(conv_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
