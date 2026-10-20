import pytest

from pages.login.login import Login
from user_reader import get_users

description = '''
======================================
Owner:     Ani Movsisyan
Created:   Oktober 16, 2026
Test Case: Add Login data
======================================
Steps:
------
1. Click on the  menu
2. Enter login field
3. Enter password field 
4. Click on the 'Login' button
======================================
Expected Result:
-----------------
1. The user should login successfully
2. The Success message appears
======================================
'''

@pytest.mark.parametrize("user", get_users())
def test_login(driver_init, user):
    login = Login(driver_init)
    login.login_process(user["username"], user["password"])

    if user["expected_result"] == "success":
        # Այստեղ ստուգում ենք, որ login-ը հաջողվել է
        assert "dashboard" in driver_init.current_url.lower()

    elif user["expected_result"] == "failure":
        # Այստեղ պետք է ստուգել login-ի սխալի հաղորդագրությունը
        assert driver_init.find_element(
            "css selector", ".error-message"
        ).is_displayed()

