import allure
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


@allure.story('Личный кабинет')
class PersonalAccountPage(BasePage):
    @allure.step('переход по клику на «Личный кабинет»')
    def click_personal_account(self):
        self.find_element_located_click(PersonalAccountLocators.ACCOUNT_BUTTON)

    @allure.step("Переход в историю заказов")
    def click_order_history(self):
        self.find_element_located_click(PersonalAccountLocators.ORDER_HISTORY)

    @allure.step("Вход в аккаунт")
    def login_to_account(self, data):
        self.find_element_located_input(PersonalAccountLocators.LOGIN_EMAIL_INPUT_FIELD, data["email"])
        self.find_element_located_input(PersonalAccountLocators.LOGIN_PASSWORD_INPUT_FIELD, data["password"])
        self.find_element_located_click(PersonalAccountLocators.ENTER_TO_ACCOUNT)

    @allure.step('выход из аккаунта')
    def logout_account(self):
        self.find_element_located_click(PersonalAccountLocators.LOGOUT_BUTTON)
