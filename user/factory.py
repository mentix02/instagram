from django.contrib.auth import get_user_model

from faker import Faker

fake = Faker()
User = get_user_model()


def create_user() -> User:
    return User.objects.create_user(
        fake.user_name(),
        fake.email(),
        'abcd',
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )
