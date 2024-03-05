from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class PersonalAccountLocators(BasePageLocators):
    ACCOUNT_BUTTON = (By.XPATH, './/*[@href="/account"]')
    ORDER_HISTORY = (By.XPATH, './/*[@href="/account/order-history"]')
    LOGOUT_BUTTON = (By.XPATH, ".//*[text()='Выход']")
    ENTER_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти']")

