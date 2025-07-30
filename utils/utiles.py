import random
import string


class Api:
    HOST = "https://reqres.in"
    LOCAL_HOST = "http://0.0.0.0:8000"


class TestUtils:

    @staticmethod
    def generate_email(quantity_letters_in_email=7):
        email = "".join(random.choices(string.ascii_lowercase, k=quantity_letters_in_email))
        return f"{email}@example.com"

    @staticmethod
    def generate_password(quantity_digits_in_password=7):
        return "".join(random.choices(string.digits, k=quantity_digits_in_password))

    @staticmethod
    def generate_username(quantity_letters_in_username=7):
        return "".join(random.choices(string.ascii_lowercase, k=quantity_letters_in_username))

    def get_user_data(self, user_data):
        user_data.email = self.generate_email()
        user_data.password = self.generate_password()
        user_data.username = self.generate_username()
