from random import randrange

from faker import Faker
from phone_gen import PhoneNumber
import datetime

class Data:
    faker_ru = Faker('ru_RU')
    # first_name = переменная для генерации имени.
    first_name = faker_ru.first_name()
    # last_name = переменная для генерации фамилии.
    last_name = faker_ru.last_name()
    # address = переменная для генерации адреса.
    address = faker_ru.street_name()
    # metro_station = переменная для генерации станции метро.
    metro_station = randrange(1, 10)
    phone = PhoneNumber('RU')
    # phone_number - переменная для генерации номера телефона.
    phone_number = phone.get_number()
    # rent_time переменная для генерации времени аренды.
    rent_time = randrange(1, 6)
    # delivery_date = переменная для генерации текущей даты.
    delivery_date = datetime.date.today().day
    # comment - переменная для комментария.
    comment = 'Quote Generated'
