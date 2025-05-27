from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters

CHOOSING_DATE, ENTERING_GUESTS, ENTERING_CONTACT = range(3)


async def start_booking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass


async def process_dates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass


def register_booking_handlers(application):
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('book', start_booking)],
        states={
            CHOOSING_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_dates)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    application.add_handler(conv_handler)
