import allure

from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Кликнуть на ленту заказов')
    def click_order(self):
        self.find_element_located_click(OrderFeedLocators.ORDERS)

    @allure.step('Получить детали всплывающего окна')
    def text_pop_up_window_details(self):
        return self.find_element_located(OrderFeedLocators.POP_UP_DETAILS).text

    @allure.step("Получить номер заказа")
    def get_num_order(self):
        self.find_element_located(OrderFeedLocators.NUM_ORDER)
        self.waiting_for_the_order_number(OrderFeedLocators.NUM_ORDER, '9999')
        return self.get_element_text(OrderFeedLocators.NUM_ORDER)

    @allure.step("Найти заказ по номеру")
    def searching_order_number(self, num_order):
        str_num_order = OrderFeedLocators.NUM_ORDER_SEARCH
        str_num_order = (str_num_order[0], str_num_order[1].format(num_order=num_order))
        return self.find_element_located(str_num_order)

    @allure.step("Заказы за все время")
    def get_num_all_orders(self):
        return self.get_element_text(OrderFeedLocators.ALL_ORDERS)

    @allure.step("Заказы за сегодня")
    def get_num_today_orders(self):
        return self.get_element_text(OrderFeedLocators.ORDERS_FOR_TODAY)

    @allure.step("Заказ в работе")
    def get_num_at_work_order(self):
        self.find_element_located(OrderFeedLocators.IN_WORK)
        self.waiting_for_the_order_number(OrderFeedLocators.IN_WORK, 'Все текущие заказы готовы!')
        return self.get_element_text(OrderFeedLocators.IN_WORK)
