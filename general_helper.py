from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class GeneralHelpers:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        self.driver.get(url)

    def go_page(self, url):
        self.driver.get(url)

    def find(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        return element

    def find_all(self, loc, timeout=10):
        elements = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_all_elements_located(loc)
        )
        return elements

    def get_element(self, locator, timeout=20):
        elements = self.find_all(locator, timeout)
        for element in elements:
            yield element

    def find_and_click(self, locator, timeout=10):
        element = self.find(locator, timeout)
        element.click()

    def find_and_send_keys(self, loc, inp_text, timeout=10):
        elem = self.find(loc, timeout)
        elem.send_keys(inp_text)

    def move_to_element(self, locator, element_located = "UI"):
        element = self.find(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def move_and_click(self, locator):
        element = self.find(locator, timeout=10)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()

    def wait_disapear_element(self, locator, timeout = 30):
        WebDriverWait(self.driver, timeout).until_not(expected_conditions.presence_of_element_located(locator))

    def wait_element_clickable(self, locator, timeout = 30):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_elemnt_precense(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def wait_element_visibility(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_elemnt_text(self, locator, text, timeout):
        WebDriverWait(self.driver, timeout).until(expected_conditions.text_to_be_present_in_element(locator, text))

    def wait_element_selected(self, locator, timeout = 30):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_located_to_be_selected(locator))


