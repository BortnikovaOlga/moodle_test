import datetime

from faker import Faker

fake = Faker("Ru-ru")


class CourseData:
    def __init__(
        self,
        full_name=None,
        short_name=None,
        summary=None,
        date_start=datetime.date.today(),
        date_end=datetime.date.today(),
    ):
        self.full_name = full_name
        self.short_name = short_name
        self.summary = summary
        self.date_start = date_start
        self.date_end = date_end

    @staticmethod
    def random():
        full_name = fake.job() + datetime.date.today().isoformat()
        short_name = fake.word()
        summary = fake.text(max_nb_chars=140)
        date_end = fake.date_between(start_date="today", end_date="+2y")
        return CourseData(full_name, short_name, summary, date_end=date_end)
