import random

from faker import Faker

from common.constants import PersonConstants

fake = Faker()  # ("Ru-ru")


class PersonData:
    def __init__(
        self,
        login: str = "bortolga",
        password: str = None,
        firstname: str = "Olga",
        lastname: str = "Bortnikova",
        email: str = "bortnikova.79@mail.ru",
        email_display: str = "2",
        city: str = "Innopolis",
        country: str = "RU",
        timezone: str = "Asia/Barnaul",
    ):
        self.login = login
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.email_display = email_display
        self.city = city
        self.country = country
        self.timezone = timezone

    def __repr__(self) -> str:
        return (
            "{"
            + str(self.firstname)
            + ","
            + str(self.lastname)
            + ","
            + str(self.email)
            + ","
            + str(self.city)
            + ","
            + str(self.country)
            + ","
            + str(self.timezone)
            + "}"
        )

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()
        firstname = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()
        email_display = random.choice(PersonConstants.EMAIL_DISPLAY)
        city = fake.city()
        country = fake.current_country_code()
        timezone = fake.timezone()
        return PersonData(
            login,
            password,
            firstname,
            lastname,
            email,
            email_display,
            city,
            country,
            timezone,
        )
