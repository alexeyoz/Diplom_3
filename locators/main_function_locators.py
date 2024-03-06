from selenium.webdriver.common.by import By


class MainFunctionLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[contains(text(),"Конструктор")]')
    ORDER_FEED_BUTTON = (By.XPATH, './/*[@href="/feed"]')
    INGREDIENT_BREAD = (By.XPATH, ".//*[@alt='Флюоресцентная булка R2-D3']")
    POP_UP_WINDOW = By.XPATH, '//*[contains(@class, "Modal_modal__contentBox__sCy8X pt-10 pb-15")]'
    CLOSE_WINDOW = (By.XPATH, ".//*[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    HOME_PAGE = By.XPATH, '//*'
    SELECT_TO_ORDER = (By.XPATH, './/div[contains(@class,"constructor-element constructor-element_pos_top")]')
    INGREDIENT_COUNTER = (By.XPATH, '(.//p[contains(@class,"counter_counter__num")])[1]')
    CREATE_ORDER = (By.XPATH, './/button[text()="Оформить заказ"]')







