from datetime import datetime, timedelta
from typing import Tuple, List, Optional
from calendar import monthcalendar
from config.config import Config


class DateHelper:
    @staticmethod
    def str_to_date(date_str: str) -> Optional[datetime]:
        """Преобразование строки в формате ДД.ММ.ГГГГ в объект datetime"""
        try:
            return datetime.strptime(date_str.strip(), '%d.%m.%Y')
        except ValueError:
            return None

    @staticmethod
    def date_to_str(date: datetime) -> str:
        """Преобразование datetime в строку формата ДД.ММ.ГГГГ"""
        return date.strftime('%d.%m.%Y')

    @staticmethod
    def parse_date_range(date_range: str) -> Tuple[Optional[datetime], Optional[datetime]]:
        """Парсинг строки с диапазоном дат (ДД.ММ.ГГГГ-ДД.ММ.ГГГГ)"""
        try:
            start_str, end_str = date_range.split('-')
            start_date = DateHelper.str_to_date(start_str)
            end_date = DateHelper.str_to_date(end_str)
            return start_date, end_date
        except ValueError:
            return None, None

    @staticmethod
    def is_valid_date_range(start_date: datetime, end_date: datetime) -> bool:
        """Проверка валидности диапазона дат"""
        if not (start_date and end_date):
            return False

        now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        min_end_date = start_date + timedelta(days=Config.MIN_BOOKING_DAYS)
        max_end_date = start_date + timedelta(days=Config.MAX_BOOKING_DAYS)

        return (
                start_date >= now and
                end_date >= min_end_date and
                end_date <= max_end_date
        )

    @staticmethod
    def get_nights_count(start_date: datetime, end_date: datetime) -> int:
        """Подсчет количества ночей между датами"""
        return (end_date - start_date).days

    @staticmethod
    def get_available_dates(booked_dates: List[Tuple[datetime, datetime]]) -> List[datetime]:
        """Получение списка доступных дат на ближайшие 3 месяца"""
        available_dates = []
        now = datetime.now()
        end_date = now + timedelta(days=90)  # 3 месяца вперед

        current = now
        while current <= end_date:
            is_available = True
            for booked_start, booked_end in booked_dates:
                if booked_start <= current <= booked_end:
                    is_available = False
                    break
            if is_available:
                available_dates.append(current)
            current += timedelta(days=1)

        return available_dates

    @staticmethod
    def get_month_calendar(year: int, month: int, booked_dates: List[Tuple[datetime, datetime]]) -> List[List[dict]]:
        """Создание календаря на месяц с отметками о бронировании"""
        calendar_data = []
        month_calendar = monthcalendar(year, month)

        for week in month_calendar:
            week_data = []
            for day in week:
                if day == 0:
                    week_data.append({
                        'day': None,
                        'available': False,
                        'status': 'empty'
                    })
                    continue

                current_date = datetime(year, month, day)
                is_available = True
                status = 'available'

                # Проверка доступности даты
                for booked_start, booked_end in booked_dates:
                    if booked_start <= current_date <= booked_end:
                        is_available = False
                        status = 'booked'
                        break

                # Проверка прошедших дат
                if current_date < datetime.now():
                    is_available = False
                    status = 'past'

                week_data.append({
                    'day': day,
                    'available': is_available,
                    'status': status
                })
            calendar_data.append(week_data)

        return calendar_data

    @staticmethod
    def format_duration(start_date: datetime, end_date: datetime) -> str:
        """Форматирование продолжительности пребывания"""
        nights = DateHelper.get_nights_count(start_date, end_date)
        if nights == 1:
            return "1 ночь"
        elif 2 <= nights <= 4:
            return f"{nights} ночи"
        else:
            return f"{nights} ночей"

    @staticmethod
    def get_season(date: datetime) -> str:
        """Определение сезона для даты"""
        month = date.month
        if month in [12, 1, 2]:
            return 'winter'
        elif month in [3, 4, 5]:
            return 'spring'
        elif month in [6, 7, 8]:
            return 'summer'
        else:
            return 'autumn'

    @staticmethod
    def get_next_available_dates(booked_dates: List[Tuple[datetime, datetime]],
                                 count: int = 5) -> List[Tuple[datetime, datetime]]:
        """Получение следующих доступных периодов для бронирования"""
        available_periods = []
        now = datetime.now()
        end_check = now + timedelta(days=180)  # Проверяем на полгода вперед

        current = now
        while current <= end_check and len(available_periods) < count:
            period_start = current
            period_end = period_start + timedelta(days=Config.MIN_BOOKING_DAYS)

            is_available = True
            for booked_start, booked_end in booked_dates:
                if (period_start <= booked_end and period_end >= booked_start):
                    is_available = False
                    current = booked_end + timedelta(days=1)
                    break

            if is_available:
                available_periods.append((period_start, period_end))
                current = period_end + timedelta(days=1)
            else:
                current += timedelta(days=1)

        return available_periods

    @staticmethod
    def format_booking_period(start_date: datetime, end_date: datetime) -> str:
        """Форматирование периода бронирования для отображения"""
        if start_date.month == end_date.month:
            return f"{start_date.day}-{end_date.day} {start_date.strftime('%B %Y')}"
        elif start_date.year == end_date.year:
            return f"{start_date.strftime('%d %B')} - {end_date.strftime('%d %B %Y')}"
        else:
            return f"{start_date.strftime('%d %B %Y')} - {end_date.strftime('%d %B %Y')}"

    @staticmethod
    def is_weekend(date: datetime) -> bool:
        """Проверка, является ли дата выходным днем"""
        return date.weekday() >= 5

    @staticmethod
    def get_holiday_dates() -> List[datetime]:
        """Получение списка праздничных дат"""
        # Можно расширить список праздничных дат
        holidays = [
            (1, 1),  # Новый год
            (7, 1),  # Рождество
            (23, 2),  # День защитника Отечества
            (8, 3),  # Международный женский день
            (1, 5),  # День труда
            (9, 5),  # День Победы
            (12, 6),  # День России
            (4, 11),  # День народного единства
        ]

        holiday_dates = []
        current_year = datetime.now().year

        for month, day in holidays:
            holiday_dates.append(datetime(current_year, month, day))
            # Добавляем даты на следующий год
            holiday_dates.append(datetime(current_year + 1, month, day))

        return holiday_dates

    @staticmethod
    def is_holiday(date: datetime) -> bool:
        """Проверка, является ли дата праздничным днем"""
        holiday_dates = DateHelper.get_holiday_dates()
        return any(
            holiday.day == date.day and
            holiday.month == date.month
            for holiday in holiday_dates
        )

