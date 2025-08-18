import allure
from selenium.webdriver.common.by import By

from pages.ui_element import UIElementMixin


class Header(UIElementMixin):
    class Locators:
        HEADER_LOGO = (By.ID, "jenkins-home-link")
        USER_PAGE_LINK = (By.CSS_SELECTOR, "a[href*='/user/']")
        LOG_OUT = (By.XPATH, '//a[@href="/logout"]')

    @allure.step("Go to the main page by clicking logo.")
    def go_to_the_main_page(self):
        from pages.main_page import MainPage
        return self.navigate_to(MainPage, self.Locators.HEADER_LOGO)
