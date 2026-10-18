import pytest
from user_reader import get_users


@pytest.mark.parametrize("user", get_users())
def test_user_data(user):
    print(user["username"])
    print(user["status"])
    print(user["id"])

    assert user["username"] in ["test_user_01", "test_user_02", "test_user_03"]
    assert user["status"] in ["active", "blocked"]
    assert user["id"].isdigit()