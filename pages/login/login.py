import time
from selenium.webdriver.common.by import By
import environment
from general_helper import GeneralHelpers


class Login(GeneralHelpers):

    login_btn = ((By.XPATH, "//a[text()='Login']"), "Login button")
    inp_email = ((By.ID, "login_email"), "Email field")


    def login_process(self):
        self.go_to_page(environment.env_data["test_url"])
        time.sleep(8)
        self.find_and_send_keys(self.inp_email_field, "email")

