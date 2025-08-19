import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NewItemPage(BasePage):
    class Locators:
        PAGE_NAME = (By.XPATH, "//h1[text()='New Item']")
        ITEM_NAME = (By.CSS_SELECTOR, '#name')
        OK_BUTTON = (By.CSS_SELECTOR, '#ok-button')
        ITEM_FOLDER = (By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]')
        ITEM_PIPELINE_PROJECT = (By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob")
        ITEM_MULTI_CONFIG_PROJECT = (By.CLASS_NAME, "hudson_matrix_MatrixProject")
        COPY_FROM = (By.ID, "from")
        DROPDOWN_COPY = (By.CSS_SELECTOR, "div.jenkins-dropdown")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/view/all/newJob"

    @allure.step("Create a new item: '{name}'")
    def create_new_item(self, name, locator, page_class):
        self.enter_item_name(name)
        self.click_on(locator)
        self.click_ok_button()
        return page_class(self.driver, name).wait_for_url()

    @allure.step("Create new Folder: '{name}'")
    def create_new_folder(self, name):
        from pages.folder_config_page import FolderConfigPage
        return self.create_new_item(name, self.Locators.ITEM_FOLDER, FolderConfigPage)

    @allure.step("Create new Pipeline project: '{name}'")
    def create_new_pipeline_project(self, name):
        from pages.pipeline_config_page import PipelineConfigPage
        return self.create_new_item(name, self.Locators.ITEM_PIPELINE_PROJECT, PipelineConfigPage)

    @allure.step("Create new Multi-configuration project: '{name}'")
    def create_new_multi_config_project(self, name):
        from pages.multi_config_project_config_page import MultiConfigProjectConfigPage
        return self.create_new_item(name, self.Locators.ITEM_MULTI_CONFIG_PROJECT, MultiConfigProjectConfigPage)

    @allure.step("Click 'OK' button")
    def click_ok_button(self):
        return self.click_on(self.Locators.OK_BUTTON)

    @allure.step("Enter item name: '{name}'")
    def enter_item_name(self, name):
        self.enter_text(self.Locators.ITEM_NAME, name)
        return self

    @allure.step("Enter value '{name}' in the 'Copy from' field")
    def enter_copy_from(self, name):
        self.enter_text(self.Locators.COPY_FROM, name)
        return self

    @allure.step("Enter the first character of '{name}' into the 'Copy from' field")
    def enter_first_character_in_copy_from(self, name):
        self.enter_copy_from(name[0])
        return self

    @allure.step("Go to error page when trying to copy from non-existent item: '{copy_name}'")
    def go_to_error_page_copy(self, name, copy_name):
        from pages.error_page_copy_from import ErrorPageCopyFrom
        self.enter_item_name(name).enter_copy_from(copy_name).click_ok_button()
        return ErrorPageCopyFrom(self.driver).wait_for_url()

    @allure.step("Click an item from dropdown")
    def select_item_from_dropdown(self):
        return self.click_on(self.Locators.DROPDOWN_COPY)

    @allure.step("Get 'Copy from' field value")
    def get_copy_from_field_value(self):
        return self.wait_and_get_attribute(self.Locators.COPY_FROM, "value")

    @allure.step("Get dropdown text")
    def get_dropdown_text(self):
        try:
            return self.get_visible_text_lines(self.Locators.DROPDOWN_COPY)
        except TimeoutException:
            self.logger.error("Dropdown did not appear: element is not visible on the page.")
            return []
