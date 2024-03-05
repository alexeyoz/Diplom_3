import allure

from data import Url
from pages.main_function_page import MainFunctionPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


@allure.story("Тест 'Лента Заказов'")
class TestsOrderFeed:
    @allure.title('Всплывающее окно после клика на ленту заказов')
    def test_window_details(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_site(Url.BASE_URL)
        main_function_page = MainFunctionPage(driver)
        main_function_page.click_order_feed()
        order_feed_page.click_order()
        assert 'Выполнен' in order_feed_page.text_pop_up_window_details()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,')
    def test_order_in_feed_and_order_history(self, driver, user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_site(Url.LOGIN_URL)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_to_account(user)
        main_function_page = MainFunctionPage(driver)
        main_function_page.add_ingredient()
        main_function_page.click_place_order()
        num_order = order_feed_page.get_num_order()
        main_function_page.click_button_close_window()
        main_function_page.click_order_feed()
        assert order_feed_page.searching_order_number(num_order)
        personal_account_page.click_personal_account()
        personal_account_page.click_order_history()
        assert order_feed_page.searching_order_number(num_order)

    @allure.title('Значение "Выполнено за всё время" увеличивается после добавления нового заказа')
    def test_completed_all_time(self, driver, user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_site(Url.ORDER_FEED)
        all_orders = order_feed_page.get_num_all_orders()
        order_feed_page.go_to_site(Url.LOGIN_URL)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_to_account(user)
        main_function_page = MainFunctionPage(driver)
        main_function_page.add_ingredient()
        main_function_page.click_place_order()
        order_feed_page.go_to_site(Url.ORDER_FEED)
        today_orders = order_feed_page.get_num_all_orders()
        assert int(all_orders) + 1 == int(today_orders)

    @allure.title('Значение "Выполнено за сегодня" увеличивается после добавления нового заказа')
    def test_completed_all_today(self, driver, user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_site(Url.ORDER_FEED)
        all_orders_today = order_feed_page.get_num_today_orders()
        order_feed_page.go_to_site(Url.LOGIN_URL)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_to_account(user)
        main_function_page = MainFunctionPage(driver)
        main_function_page.add_ingredient()
        main_function_page.click_place_order()
        order_feed_page.go_to_site(Url.ORDER_FEED)
        today_orders = order_feed_page.get_num_today_orders()
        assert int(all_orders_today) + 1 == int(today_orders)

    @allure.title('Отображения заказа в меню "В работе"')
    def test_displaying_order_menu_orders(self, driver, user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.go_to_site(Url.LOGIN_URL)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_to_account(user)
        main_function_page = MainFunctionPage(driver)
        main_function_page.add_ingredient()
        main_function_page.click_place_order()
        num_order = order_feed_page.get_num_order()
        main_function_page.click_button_close_window()
        order_feed_page.go_to_site(Url.ORDER_FEED)
        num_order_menu_orders = order_feed_page.get_num_at_work_order()
        assert '0' + num_order == num_order_menu_orders

