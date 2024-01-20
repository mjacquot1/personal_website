import pytest

# This file is automatically found by pytest
# This will house all fixtures that are automatically grabbed by test files
# Fixtures in this file are only created once then re-used per test

from pytest_factoryboy import register
from resume.tests.factories import UserFactory


# Create/register a fixture of UserFactory as user_factory
register(UserFactory)

@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user



# from django.contrib.auth.models import User


# # With a fixture, 'db' imports the database VS @pytest.mark.django_db being used to bring in a database
# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user('test_user')
#     return user

# @pytest.fixture
# def new_user_factory(db):
#     def create_app_user(
#             username: str,
#             password: str = None,
#             first_name: str = "firstname",
#             last_name: str = "lastname",
#             email: str = "test@test.com",
#             is_staff: str = False,
#             is_superuser: str = False,
#             is_active: str = True,
#     ):
#         user = User.objects.create_user(
#             username    =username,
#             password    =password,
#             first_name  =first_name,
#             last_name   =last_name,
#             email       =email,
#             is_staff    =is_staff,
#             is_superuser=is_superuser,
#             is_active   =is_active,
#         )
#         return user
#     return create_app_user

# @pytest.fixture
# def new_user(db, new_user_factory):
#     return new_user_factory("test_user","password","MyName")

# @pytest.fixture
# def new_user_2(db, new_user_factory):
#     return new_user_factory("test_user","password","MyName", is_staff = True)