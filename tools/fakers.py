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
        """
        Генерирует случайный текст
        :return: Случайный текст
        """
        return self.faker.text()

    def uid (self) -> str:
        """
        Генерирует случайный UID
        :return: случайный UID
        """
        return self.faker.uuid4()

    def email(self)-> str:
        """
        Генерирует случайный email
        :return: случайный emai
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Генериеует случайное предложение
        :return:случайное предложение
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль
        :return:случайный пароль
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует случайную фамилию.
        :return:Случайная фамилия.
        """
        return self.faker.last_name()

    def first_name (self) -> str:
        """
        Генерирует случайное имя.
        :return:Случайное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайное отчество/среднее имя.
        :return:Случайное отчество.
        """
        return self.faker.first_name()

    def estimated_time(self):
        """
        Генерирует строку с предполагаемым временем (например, "2 weeks")
        :return:f"{self.integer(1, 10)} weeks"
        """
        return f"{self.integer(1,5)} weeks"

    def integer(self, start: int =1, end: int = 100):
        """
        Генерирует случайное целое число в заданном диапазоне.
        :param start: Начало диапазона (включительно)
        :param end: Конец диапазона (включительно)
        :return: Случайное целое число
        """
        return self.faker.random_int( start, end)

    def max_score(self) -> int:
        """
        Генерирует случайный максимальный балл в диапазоне от 1 до 100.
        :return:Случайный балл
        """
        return self.integer(1,100)

    def min_score(self) -> int:
        """
        Генерирует случайный минимальный балл в диапазоне от 1 до 10
        :return: минимальный балл
        """
        return self.integer(0,10)

# Создаем экземпляр класса Fake с использованием Faker
fake = Fake(faker=Faker())

