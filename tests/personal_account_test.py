import allure
from pages.personal_account_page import PersonalAccountPage
from pages.recovery_password_page import RecoveryPasswordPage
from data import Url
from locators.personal_account_locators import PersonalAccountLocators


@allure.story('Тест "Личный кабинет"')
class TestPersonalAccount:

    @allure.step('тест клик "Личный кабинет"')
    def test_personal_account_page(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.go_to_site(Url.BASE_URL)
        personal_account_page.click_personal_account()
        assert personal_account_page.current_url() == Url.LOGIN_URL

    @allure.step("тест клик 'История заказов'")
    def test_history(self, driver, user):
        personal_account_page = PersonalAccountPage(driver)
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.go_to_site(Url.LOGIN_URL)
        personal_account_page.login_to_account(user)
        personal_account_page.click_personal_account()
        personal_account_page.click_order_history()
        assert personal_account_page.current_url() == Url.ORDER_HISTORY

    @allure.step('тест клик "Выход из аккаунта"')
    def test_logout(self, driver, user):
        personal_account_page = PersonalAccountPage(driver)
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.go_to_site(Url.LOGIN_URL)
        personal_account_page.login_to_account(user)
        personal_account_page.click_personal_account()
        personal_account_page.logout_account()
        personal_account_page.wait_visibility(10, PersonalAccountLocators.ENTER_TO_ACCOUNT)
        assert personal_account_page.current_url() == Url.LOGIN_URL


