from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDERS = (By.XPATH, ".//*[@class='OrderFeed_list__OLh59']")
    POP_UP_DETAILS = By.XPATH, '//*[contains(@class, "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10")]'
    NUM_ORDER = (By.XPATH, ".//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text "
                           "text_type_digits-large mb-8']")
    NUM_ORDER_SEARCH = (By.XPATH, ".//*[text()='#0{num_order}']")
    ALL_ORDERS = (By.XPATH, ".//p[text() = 'Выполнено за все время:']/following-sibling::p[@class = "
                            "'OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDERS_FOR_TODAY = (By.XPATH, "//div[last()]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    IN_WORK = (By.XPATH, "//ul[contains(@class, 'ListReady')]/li")

