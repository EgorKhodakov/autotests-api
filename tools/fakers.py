from faker import Faker


class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def uid (self) -> str:
        return self.faker.uuid4()

    def email(self)-> str:
        return self.faker.email()

    def sentance(self) -> str:
        return self.faker.sentence()

    def password(self) -> str:
        return self.faker.password()

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name (self) -> str:
        return self.faker.first_name()

    def middle_name(self) -> str:
        return self.faker.first_name()

    def estimated_time(self):
        return f"{self.integer(1,5)} weeks"

    def integer(self, start: int =1, end: int = 100):
        return self.faker.random_int( start, end)

    def max_score(self) -> int:
        return self.integer(1,100)

    def min_score(self) -> int:
        return self.integer(0,10)

# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker())

