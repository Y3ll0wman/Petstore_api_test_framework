from random import randint
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender


def user_id() -> int:
    return randint(0, 9999)


def username() -> str:
    person = Person(Locale.RU)
    return person.username()


def first_name() -> str:
    person = Person(Locale.EN)
    return person.first_name(gender=Gender.MALE)


def last_name() -> str:
    person = Person(Locale.EN)
    return person.last_name(gender=Gender.MALE)


def email() -> str:
    person = Person(Locale.RU)
    return person.email(domains=['gmail.com'])


def password() -> str:
    person = Person(Locale.RU)
    return person.password(length=8)


def phone() -> str:
    person = Person(Locale.RU)
    return person.phone_number(mask="+7##########")
