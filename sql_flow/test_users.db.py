
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from db import create_users, get_user


@pytest.fixture
def driver_init():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_login_with_db_user(driver_init):
    create_users()

    user = get_user()

    user_id = user[0]
    username = user[1]
    password = user[2]

    driver = driver_init
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    username_field = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )
    username_field.send_keys(username)

    password_field = driver.find_element(
        By.ID, "password"
    )
    password_field.send_keys(password)

    driver.find_element(
        By.ID, "login-button"
    ).click()

    inventory = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    assert inventory.is_displayed()

    print("User ID:", user_id)
    print("Username:", username)
    print("Login successful!")
