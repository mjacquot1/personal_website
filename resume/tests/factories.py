import factory
from faker import Faker

from django.contrib.auth.models import User

fake = Faker()

# Inherity from factory-boys DjangoModel Class
# Set modeul to Django's User model
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'

