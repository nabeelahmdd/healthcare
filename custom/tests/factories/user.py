import factory
from custom.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = "Password@123"
    phone_number = factory.Faker('phone_number')
    category = factory.Faker(
        'random_element', elements=['d', 'p', 'r']
    )
    is_active = True
