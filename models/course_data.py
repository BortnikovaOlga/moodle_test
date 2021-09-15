from faker import Faker

fake = Faker("Ru-ru")


class CourseData:
    def __init__(
        self,
        full_name=None,
        short_name=None,
    ):
        self.full_name = full_name
        self.short_name = short_name

    @staticmethod
    def random():
        full_name = fake.job()
        short_name = fake.word()

        return CourseData(full_name, short_name)
