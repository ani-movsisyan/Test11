import time
from selenium.webdriver.common.by import By
import environment
from general_helper import GeneralHelpers


class Login(GeneralHelpers):

    inp_pass = ((By.ID, "login_pass"), "Password Field")
    inp_email = ((By.ID, "login_email"), "Email field")
    login_btn = ((By.XPATH, "//a[text()='Login']"), "Login button")

    def login_process(self, email, password):
        self.go_to_page(environment.env_data["test_url"])
        time.sleep(8)
        self.find_and_send_keys(self.inp_email, email)
        self.find_and_send_keys(self.inp_pass, password)
        self.find_and_click(self.login_btn)
