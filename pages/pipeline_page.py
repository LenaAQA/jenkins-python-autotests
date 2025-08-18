import allure
import logging
from urllib.parse import quote

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


logger = logging.getLogger(__name__)


class PipelinePage(BasePage):
    class Locators:
        DESCRIPTION_ELEMENT = (By.ID, "description")
        MOVE_LINK = (By.XPATH, '//a[contains(@href, "/move")]')
        MOVE_BTN = (By.XPATH, "//button[@name='Submit']")
        SETTING_INPUT = (By.XPATH, "//select[@name='destination']")
        HEADER = (By.TAG_NAME, "h1")
        BUILDS_LINKS = (By.CSS_SELECTOR, "#jenkins-build-history a.app-builds-container__item__inner__link")
        BUILDS_NEXT_PAGE_BUTTON = (By.ID, "down")
        BUILDS_PREV_PAGE_BUTTON = (By.ID, "up")
        SINGLE_BUILD_NUMBER = (By.CLASS_NAME, "app-builds-container__item__inner__link")

    def __init__(self, driver, pipeline_project_name, timeout=10):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(pipeline_project_name)}/"

    @allure.step("Get the page header text")
    def get_header_pipeline_page(self) -> str:
        return self.get_visible_text(self.Locators.HEADER)
