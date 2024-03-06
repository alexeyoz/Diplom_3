import allure
import helpers
from pages.recovery_password_page import RecoveryPasswordPage
from data import Url


class TestRecoveryPassword:

    @allure.step('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_recovery_password_page(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.go_to_site(Url.LOGIN_URL)
        recovery_password_page.go_to_personal_account()
        assert recovery_password_page.current_url() == Url.FROGOT_PASSWORD_URL

    @allure.step('ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_clicking(self, driver, user):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.go_to_site(Url.FROGOT_PASSWORD_URL)
        recovery_password_page.input_email(user["email"])
        recovery_password_page.click_button_recovery_password()
        recovery_password_page.expectation_url(Url.RESET_PASSWORD)
        assert recovery_password_page.current_url() == Url.RESET_PASSWORD

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_clicking_show_hide(self, driver, user):
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.go_to_site(Url.FROGOT_PASSWORD_URL)
        recovery_password_page.input_email(user["email"])
        recovery_password_page.click_button_recovery_password()
        recovery_password_page.click_show_hide()
        result = recovery_password_page.get_class_highlighted_field()
        assert "status_active" in result
