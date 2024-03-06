from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class RecoveryPasswordLocators(BasePageLocators):
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//*[@href='/forgot-password']")
    BUTTON_RECOVERY = (By.XPATH, ".//*[text()='Восстановить']")
    EMAIL = (By.XPATH, ".//*[@class='text input__textfield text_type_main-default']")
    PASS_AVAILABLE = (By.XPATH, ".//*[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    BUTTON_SHOW_HIDE = (By.XPATH, ".//*[@class='input__icon input__icon-action']")
