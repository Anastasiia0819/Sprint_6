import faker


def get_random_data_for_order():
    fake = faker.Faker('ru_RU')
    name = fake.first_name()
    surname = fake.last_name()
    when_order_data = fake.date_between(start_date='today', end_date='+30d').strftime('%d.%m.%Y')
    return name, surname, when_order_data
