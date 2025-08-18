import allure
import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.ui_element import UIElementMixin


logger = logging.getLogger(__name__)


class MainPage(BasePage, UIElementMixin):
    class Locators:
        PAGE_NAME = (By.XPATH, "//a[text()='Dashboard']")
        NEW_ITEM_BUTTON = (By.LINK_TEXT, "New Item")
        BUILD_HISTORY_BUTTON = (By.LINK_TEXT, "Build History")
        MANAGE_JENKINS_BUTTON = (By.LINK_TEXT, "Manage Jenkins")
        TABLE_ITEM = (By.CSS_SELECTOR, "a.inside")
        BUILD_QUEUE_BLOCK = (By.ID, 'buildQueue')
        BUILD_QUEUE_HEADER = (By.CLASS_NAME, "pane-header-title")
        BUILD_QUEUE_STATUS_MESSAGE = (By.CLASS_NAME, "pane")
        BUILD_QUEUE_TOGGLE = (By.CSS_SELECTOR, "a[href = '/toggleCollapse?paneId=buildQueue']")
        FOLDER_LINK_LOCATOR = "//*[@id='job_{}']/td[3]/a"
        TABLE_HEADERS = (By.XPATH, "//table[@id='projectstatus']//thead//th")
        CELLS_IN_JOB_ROW = (By.XPATH, "//td[../td//a[contains(@href, 'job')]]")
        PROJECT_BUTTON = (By.XPATH, "//table[@id='projectstatus']//tbody//td[3]/a")
        TABLE_SVG = (By.CSS_SELECTOR, "td svg")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/"

    @allure.step("Go to the New Item Page by clicking New Item button.")
    def go_to_new_item_page(self):
        from pages.new_item_page import NewItemPage
        return self.navigate_to(NewItemPage, self.Locators.NEW_ITEM_BUTTON)

    def go_to_manage_jenkins_page(self):
        from pages.manage_jenkins.manage_jenkins_page import ManageJenkinsPage
        self.click_on(self.Locators.MANAGE_JENKINS_BUTTON)
        return ManageJenkinsPage(self.driver).wait_for_url()
