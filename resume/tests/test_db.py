import pytest

from django.contrib.auth.models import User

# # During tests, tables are created
# # Tables do not persist over tests
# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('test', 'test@test.com', 'test')
#     assert User.objects.count() == 1


# # @pytest.mark.django_db
# def test_check_password(user_1):
#     user_1.set_password('new-password')
#     assert user_1.check_password('new-password') is True

# def test_new_user(new_user):
#     print(new_user.first_name)
#     assert new_user.first_name == "MyName"

# def test_new_user_staff(new_user_2):
#     new_user = new_user_2
#     print(new_user.is_staff)
#     assert new_user.is_staff == True

@pytest.mark.django_db
def test_new_user(new_user1):
    print(new_user1.username)
    assert True

