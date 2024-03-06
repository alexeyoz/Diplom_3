import allure

from pages.base_page import BasePage
from locators.recovery_password_locators import RecoveryPasswordLocators


@allure.story('Восстановление пароля')
class RecoveryPasswordPage(BasePage):
    @allure.step('Кнопка "Восстановление пароля"')
    def click_button_recovery(self):
        self.find_element_located_click(RecoveryPasswordLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Вводим email для восстановления пароля')
    def input_email(self, email):
        self.find_element_located_input(RecoveryPasswordLocators.EMAIL, email)

    @allure.step('Кнопка "Восстановить"')
    def click_button_recovery_password(self):
        self.find_element_located_click(RecoveryPasswordLocators.BUTTON_RECOVERY)

    @allure.step('Кнопка "Скрыть/Показать пароль"')
    def click_show_hide(self):
        self.find_element_located_click(RecoveryPasswordLocators.BUTTON_SHOW_HIDE)

    @allure.step("Получить класс подсвечиваемого поля")
    def get_class_highlighted_field(self):
        return self.get_attribute(RecoveryPasswordLocators.PASS_AVAILABLE, "class")

    def go_to_personal_account(self):
        self.find_element_located_click(RecoveryPasswordLocators.PASSWORD_RECOVERY_BUTTON)
