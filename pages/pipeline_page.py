import allure
import logging
from urllib.parse import quote

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


logger = logging.getLogger(__name__)


class PipelinePage(BasePage):
    class Locators:
        HEADER = (By.TAG_NAME, "h1")

    def __init__(self, driver, pipeline_project_name, timeout=10):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{quote(pipeline_project_name)}/"

    @allure.step("Get the page header text")
    def get_header_pipeline_page(self) -> str:
        return self.get_visible_text(self.Locators.HEADER)
