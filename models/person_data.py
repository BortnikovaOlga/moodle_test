from faker import Faker

fake = Faker("Ru-ru")


class PersonData:
    def __init__(
        self,
        login="bortolga",
        password=None,
        firstname="Olga",
        lastname="Bortnikova",
        email="bortnikova.79@mail.ru",
        email_display="2",
        city="Innopolis",
        country="RU",
        timezone="Asia/Barnaul",
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

    @staticmethod
    def random():
        login = fake.email()
        password = fake.password()
        firstname = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()
        city = fake.city
        country = fake.country()
        timezone = None
        comments = "fake.lorem()"
        foto = None
        return PersonData(
            login,
            password,
            firstname,
            lastname,
            email,
            city,
            country,
            timezone,
            comments,
            foto,
        )
