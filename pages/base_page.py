from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.recovery_password_locators import RecoveryPasswordLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element_located_click(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def current_url(self):
        return self.driver.current_url

    def go_to_personal_account(self):
        self.find_element_located_click(RecoveryPasswordLocators.PASSWORD_RECOVERY_BUTTON)

    def find_element_located_input(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).send_keys(text)

    def get_element_text(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator)).text

    def drag_and_drop(self, drag_element, drop_element):
        ActionChains(self.driver).drag_and_drop(drag_element, drop_element).perform()

    def expectation_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_to_be(url))

    def get_attribute(self, locator, attribute, time=30):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).get_attribute(attribute)

    def waiting_for_the_order_number(self, locator, template, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.text_to_be_present_in_element(locator, template))

    def wait_visibility(self, timeout, locator):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
