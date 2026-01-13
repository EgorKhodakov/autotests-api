import pytest

@pytest.fixture(autouse=True)
def send_analytic_data():
    print("Отправка аналитических данных")

@pytest.fixture(scope='function')
def settings():
    print("Создание настроек для тестов")

@pytest.fixture(scope='class')
def user():
    print("Создаем пользователя один раз на тестовый класс")

@pytest.fixture(scope='function')
def users_client():
    print("Создаем API клиента для каждого атвотеста")


class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        pass

    def test_user_can_create_course(self, settings, user, users_client):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        pass
