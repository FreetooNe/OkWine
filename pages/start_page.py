import random
from time import sleep

from selenium.webdriver.common.keys import Keys
from constants.header import HeaderConsts
from constants.start_page import StartPageConst
# from constants.user_profile import ProfileConsts
from pages.base_page import BasePage
from pages.utils import log_wrapper, wait_until_ok


class StartPage(BasePage):
    """Stores methods describes start page actions"""

    @log_wrapper
    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.consts_header = HeaderConsts
        # self.const_profile = ProfileConsts

    @wait_until_ok()
    @log_wrapper
    def add_item_to_cart(self):
        self.click(xpath=self.const.VERIFY_AGE_XPATH)
        self.click(xpath=self.const.VERIFY_CITY)
        self.click(xpath=self.const.OPEN_ITEM_XPATH)
        self.click(xpath=self.const.ADD_ITEM_TO_CART_XPATH)
        assert self.is_element_exists(xpath=self.const.VERIFY_CHANGE_BUTTON_XPATH)
        self.click(xpath=self.const.OPEN_POPUP_XPATH)
        self.click(xpath=self.const.CONTINUE_SHOPPING_XPATH)
        self.click(xpath=self.consts_header.BASKET_BUTTON_XPATH)
        assert self.is_element_visible(xpath=self.const.VERIFY_ITEM)
