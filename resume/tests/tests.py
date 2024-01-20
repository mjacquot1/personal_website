import pytest

# 'scope=session' is so that the object is created only once per test session, not per each test
@pytest.fixture(scope="session")
def fixture_1():
    print('running fixture')
    return 1


@pytest.fixture(scope="session")
def yield_fixture():
    print('start test phase')
    yield 6
    print("end test phase")

def test_example1(fixture_1):
    num = fixture_1
    assert num == 1


def test_example2(fixture_1):
    num = fixture_1
    assert num == 1