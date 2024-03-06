import allure
from locators.main_function_locators import MainFunctionLocators
from pages.base_page import BasePage


class MainFunctionPage(BasePage):
    @allure.step('Кликнуть на кнопку "Конструктор"')
    def click_constructor(self):
        self.find_element_located_click(MainFunctionLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на ленту заказов")
    def click_order_feed(self):
        self.find_element_located_click(MainFunctionLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик на ингредиент")
    def click_ingredient(self):
        self.find_element_located_click(MainFunctionLocators.INGREDIENT_BREAD)

    @allure.step('Получить текст названия всплывающего окна')
    def text_pop_up_window(self):
        return self.find_element_located(MainFunctionLocators.POP_UP_WINDOW).text

    @allure.step("Клик 'Закрыть всплывающее окно'")
    def click_button_close_window(self):
        self.find_element_located_click(MainFunctionLocators.CLOSE_WINDOW)

    @allure.step('Получить текст стартовой страницы')
    def text_home_page(self):
        return self.find_element_located(MainFunctionLocators.HOME_PAGE).text

    @allure.step("Добавление ингредиента")
    def add_ingredient(self):
        ingredient = self.find_element_located(MainFunctionLocators.INGREDIENT_BREAD)
        add_to_order = self.find_element_located(MainFunctionLocators.SELECT_TO_ORDER)
        self.drag_and_drop(ingredient, add_to_order)

    @allure.step("Получение счетчика ингредиента")
    def get_counter(self):
        return self.get_element_text(MainFunctionLocators.INGREDIENT_COUNTER)

    @allure.step("Клик 'Оформить заказ'")
    def click_place_order(self):
        self.find_element_located_click(MainFunctionLocators.CREATE_ORDER)
