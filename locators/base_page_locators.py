from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_EMAIL_INPUT_FIELD = (By.XPATH, ".//*[@name='name']")
    LOGIN_PASSWORD_INPUT_FIELD = (By.XPATH, ".//*[@name='Пароль']")
