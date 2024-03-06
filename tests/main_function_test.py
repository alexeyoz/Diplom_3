import allure

from pages.main_function_page import MainFunctionPage
from pages.personal_account_page import PersonalAccountPage
from pages.recovery_password_page import RecoveryPasswordPage
from data import Url


class TestMainFunction:
    @allure.title("Переход к Конструктору")
    def test_go_to_constructor(self, driver):
        main_function_page = MainFunctionPage(driver)
        main_function_page.go_to_site(Url.ORDER_FEED)
        main_function_page.click_constructor()
        assert main_function_page.current_url() == Url.BASE_URL + '/'

    @allure.title('Переключение на ленту заказов')
    def test_go_to_order_feed(self, driver):
        main_function_page = MainFunctionPage(driver)
        main_function_page.go_to_site(Url.BASE_URL)
        main_function_page.click_order_feed()
        assert main_function_page.current_url() == Url.ORDER_FEED

    @allure.title('Кликнуть на ингредиент, появится всплывающее окно')
    def test_pop_up_window(self, driver):
        main_function_page = MainFunctionPage(driver)
        main_function_page.go_to_site(Url.BASE_URL)
        main_function_page.click_ingredient()
        assert 'Детали ингредиента' in main_function_page.text_pop_up_window()

    @allure.title('Закрываем всплывающее окно')
    def test_pop_up_window_close(self, driver):
        main_function_page = MainFunctionPage(driver)
        main_function_page.go_to_site(Url.BASE_URL)
        main_function_page.click_ingredient()
        main_function_page.click_button_close_window()
        assert 'Лента Заказов' in main_function_page.text_home_page()

    @allure.title('Увеличение счетчика ингредиента')
    def test_ingredient_counter(self, driver):
        main_function_page = MainFunctionPage(driver)
        main_function_page.go_to_site(Url.BASE_URL)
        main_function_page.add_ingredient()
        assert main_function_page.get_counter() == '2'

    @allure.title('Оформления заказа пользователем')
    def test_checkout(self, driver, user):
        main_function_page = MainFunctionPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        recovery_password_page = RecoveryPasswordPage(driver)
        recovery_password_page.go_to_site(Url.LOGIN_URL)
        personal_account_page.login_to_account(user)
        main_function_page.add_ingredient()
        main_function_page.click_place_order()
        assert 'Ваш заказ начали готовить' in main_function_page.text_home_page()
