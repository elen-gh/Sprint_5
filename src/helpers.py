import faker
from faker import Faker

def get_sign_up_data():
    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    return email, password

def get_ad_data():
    fake = Faker('ru_RU')
    description = fake.text(max_nb_chars=150)
    price = fake.random_int(min=1000, max=50000)
    return description, price