# import datetime
import random
import time
from datetime import datetime, timezone, timedelta


current_date = datetime.now()

# print(f"This is date-time now: {current_date.now()}")
# print(f"This is date(): {current_date.date()}")
# print(f"This is time(): {current_date.time()}")
# print(f"This is month: {current_date.month}")
# print(f"This is day: {current_date.day}")
# print(f"This is hour: {current_date.hour}")
# print(f"This is minute: {current_date.minute}")
# print(f"This is second: {current_date.second}")
# print(f"This is microsecond: {current_date.microsecond}")
# print(f"This is tzinfo: {current_date.tzinfo}")
# print(f"This is tzname: {current_date.tzname()}")
# print(f"This is tzmets: {current_date.timetz()}")

# -----------------------------------
# import datetime

# part_day = datetime.date(2025, 10, 2)
# part_time = datetime.time(12, 30, 14)

# combine_datetime = datetime.datetime.combine(part_day, part_time)
# print(combine_datetime)  # Виведе "2025-10-02 12:30:14"
# ---
# second variant use datetime module
# part_day = datetime(2025, 10, 2).date()
# part_time = datetime(12, 2, 14).time()

# combine_datetie = datetime.combine(part_day, part_time)
# print(combine_datetie)
# --------------------------

# weekday()

# day_of_week = current_date.weekday()
# match day_of_week:
#     case 5:
#         print(f"Friday")
#     case 4:
#         print(f"Thirsday")

# print(f"today is {day_of_week}")
# -------------------------
# from datetime import datetime

# Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)

# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2
# --------------------------

# timedelta

# from datetime import timedelta

# delta = timedelta(
#     days=50,
#     seconds= 50,
#     microseconds=77,
#     milliseconds= 70000,
#     minutes=20,
#     hours= 5,
#     weeks=1
# )

# print(f"This is about timedelta class: {delta}")
# --------------------

# from datetime import datetime

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0
# -----------

# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(f"This is about create date different from now: {future_date}")
# -----------

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00
# -----------------------

# Створення об'єкта datetime
# date = datetime(year=2023, month=12, day=18)

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")
# # ---------------


# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# # Поточна дата
# current_date = datetime.now()

# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(f"Повних днів,з моменту, коли Наполеон спалив Москву: {days_since}")
# # ---------------

# # timestamp

# # Поточний час
# now = datetime.now()

# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# # Виведе timestamp поточного часу
# print(f"Timestamp of the current-time: {timestamp}")
# # ---------------

# # Припустимо, є timestamp
# timestamp = 174082527

# # Конвертація timestamp назад у datetime
# dt_object = datetime.fromtimestamp(timestamp)
# print(f"Timestamp in datetime: {dt_object}")  # Виведе відповідний datetime
# # -------------------

# # Парсинг дати із рядка


# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(f"formatted_date: {formatted_date}")

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(f"formatted_date_only: {formatted_date_only}")

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(f"formatted_time_only: {formatted_time_only}")

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(f"formatted_date_only: {formatted_date_only} \n")
# # ------------------------
# # на веб-сайту є рядок дата "2023.03.14" якогось посту
# # і нам треба перед тим як зберегти дату в базі даних
# # перетворити її на об'єкт datetime

# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.03.14"

# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# # Виведе об'єкт datetime, що відповідає вказаній даті та часу
# print(f"This is object datetime: {datetime_object} \n")
# ------------------------------

# ISO use isoformat()

# now = datetime.now()
# iso_format = now.isoformat()
# print(f"This is isoformat: {iso_format}")
# ------------------------------

# iso_date_format = "2025-03-01T16:31:50.139864"

# date_from_iso = datetime.fromisoformat(iso_date_format)
# print(f"This is date from format ISO: {date_from_iso}")
# ------------------------------


# day_of_week = now.isoweekday()
# print(f"Today is {day_of_week} day of week!")
# --------------------------

# Створення об'єкта datetime
# now = datetime.now()

# Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(
#     f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

# print(f"ISO Calendar: {iso_calendar}")
# --------------------------


# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(f"This is local time now: {local_now}")
# print(f"this is time zone utc: {utc_now}")  # Виведе поточний час в UTC
# # --------------------------

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # Перетворює час UTC в час Східного часового поясу
# print(f"Eastern Time Zone: {eastern_time}")
# # --------------------------

# # Припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# print(f"Local Time Zone: {local_timezone}")
# local_time = datetime(year=2023, month=3, day=14, hour=12,
#                       minute=30, second=0, tzinfo=local_timezone)

# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(f"The local time to UTC: {utc_time}")  # Виведе час в UTC
# # --------------------------
# # Час у конкретній часовій зоні
# timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
# timezone_datetime = datetime(
#     year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# # Конвертація у формат ISO 8601
# iso_format_with_timezone = timezone_datetime.isoformat()
# print(f" ISO Format With Timezone: {iso_format_with_timezone}")
# # --------------------------
# # lst = list("a,b,c,d")
# # lst.remove('b')
# # print("".join(lst))
# # --------------------------

# TIME module


# current_time = time.time()

# print(f"Next must be pause 5 seconds!")
# print(f"Current time now: {current_time}")
# # --------------------------

# time.sleep(3)
# # --------------------------

# readable_time = time.ctime(current_time)
# print(f"This use time.ctime(): {readable_time}")
# # --------------------------

# local_time = time.localtime(current_time)
# print(f"Local time now: {local_time}")

# local_time = time.gmtime(current_time)
# print(f"Local time use time.gmtime(): {local_time}")
# # --------------------------
# # useing time.perf-counter()

# start_time = time.perf_counter()

# for _ in range(1_000_000):
#     pass

# end_time = time.perf_counter()

# execution_time = end_time - start_time
# print(f"This is use module time.perf_counter: {execution_time}")
# # --------------------------
# rando, randint, shufll

number = random.randint(1, 1000)
print(f"This is random number: {number}")

random_number = random.random()
print(f"this is random.random(): {random_number}")

number_percentage = random.random() * 100
print(f"This is number_percentage: {number_percentage:.2f}%")
# # --------------------------

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

random.shuffle(cards)

print(f"Перемішана колода: {cards}")
print(f"Перемішана колода: {cards[0]}")
# --------------------------

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))
# --------------------------

items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(f"This is choices: {chosen_item}")

numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(f"This is choice with repeat: {chosen_numbers}")

colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(f"This is choices with weight of choice: {chosen_color}")


participants = ['Анна', 'Богдан', 'Віктор', 'Галина',
                'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}")


price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")
