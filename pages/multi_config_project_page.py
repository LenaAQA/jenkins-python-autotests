import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MultiConfigProjectPage(BasePage):
    class Locators:
        WARNING_MESSAGE = (By.ID, "enable-project")
        ENABLE_BUTTON = (By.XPATH, "//form[@id='enable-project']//button")
        PROJECT_STATUS_ICON = (By.CSS_SELECTOR, "#matrix svg.icon-md")
        CONFIGURE_MENU_ITEM = (By.XPATH, "//span[text()='Configure']/..")

    def __init__(self, driver, name, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{name}/"
        self.name = name

    @allure.step("Get text of the warning message")
    def get_text_warning_message(self):
        return self.get_visible_text_lines(self.Locators.WARNING_MESSAGE)[0]

    @allure.step("Click the button 'Enable' to enable the project")
    def enable_project(self):
        self.click_on(self.Locators.ENABLE_BUTTON)
        return self

    @allure.step("Check if the 'Enable' button is displayed")
    def is_enable_button_displayed(self) -> bool:
        return self.is_element_displayed(self.Locators.ENABLE_BUTTON)

    @allure.step("Wait for the warning message to disappear")
    def wait_warning_message_to_disappear(self) -> bool:
        return self.wait_element_to_disappear(self.Locators.WARNING_MESSAGE)

    @allure.step("Get the project status title")
    def get_project_status_title(self) -> str:
        return self.wait_and_get_attribute(self.Locators.PROJECT_STATUS_ICON, "title")

    def go_to_configure_page(self):
        with allure.step(f'Go to Configure page of project "{self.name}"'):
            from pages.multi_config_project_config_page import MultiConfigProjectConfigPage
            self.click_on(self.Locators.CONFIGURE_MENU_ITEM)
            return MultiConfigProjectConfigPage(self.driver, self.name).wait_for_url()
