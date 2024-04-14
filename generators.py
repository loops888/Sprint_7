from random import randrange

from faker import Faker
from phone_gen import PhoneNumber
import datetime

class Data:
    faker_ru = Faker('ru_RU')
    # name = переменная для генерации имени.
    first_name = faker_ru.first_name()
    # surname = переменная для генерации фамилии.
    last_name = faker_ru.last_name()
    # address = переменная для генерации адреса.
    address = faker_ru.street_name()
    # number = переменная для генерации номера телефона.
    metro_station = randrange(1, 10)
    phone = PhoneNumber('RU')
    phone_number = phone.get_number()
    rent_time = randrange(1, 6)
    # date = переменная для генерации текущей даты.
    delivery_date = datetime.date.today().day
    comment = 'Quote Generated'
