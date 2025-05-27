import asyncio
import logging
from telegram.ext import Application

from config.config import Config
from handlers.about import register_about_handlers
from handlers.booking import register_booking_handlers
from handlers.info import register_info_handlers
from handlers.contacts import register_contacts_handlers


async def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    application = Application.builder().token(Config.BOT_TOKEN).build()

    register_about_handlers(application)
    register_booking_handlers(application)
    register_info_handlers(application)
    register_contacts_handlers(application)

    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
