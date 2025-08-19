import allure
import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.ui_element import UIElementMixin


logger = logging.getLogger(__name__)


class MainPage(BasePage, UIElementMixin):
    class Locators:
        NEW_ITEM_BUTTON = (By.LINK_TEXT, "New Item")
        MANAGE_JENKINS_BUTTON = (By.LINK_TEXT, "Manage Jenkins")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/"

    @allure.step("Go to the New Item Page by clicking New Item button.")
    def go_to_new_item_page(self):
        from pages.new_item_page import NewItemPage
        return self.navigate_to(NewItemPage, self.Locators.NEW_ITEM_BUTTON)

    @allure.step("Go to 'Manage Jenkins' page")
    def go_to_manage_jenkins_page(self):
        from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage
        self.click_on(self.Locators.MANAGE_JENKINS_BUTTON)
        return ManageJenkinsPage(self.driver).wait_for_url()
