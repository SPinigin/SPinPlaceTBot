import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    DATABASE_URL = os.getenv('DATABASE_URL')

    MAX_GUESTS = 10
    MIN_BOOKING_DAYS = 1
    MAX_BOOKING_DAYS = 14
    DEPOSIT_PERCENTAGE = 20

    IMAGES_PATH = 'resources/images/'
    COTTAGE_DESCRIPTION = 'resources/texts/description.txt'
    RULES_TEXT = 'resources/texts/rules.txt'

    ADMIN_CONTACT = "+7 (932) 477-96-22"
    EMAIL = "pinigin09@yandex.ru"
