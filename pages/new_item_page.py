import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NewItemPage(BasePage):
    class Locators:
        PAGE_NAME = (By.XPATH, "//h1[text()='New Item']")
        ITEM_NAME = (By.CSS_SELECTOR, '#name')
        ITEM_FOLDER = (By.CSS_SELECTOR, '[class*="cloudbees_hudson_plugins_folder"]')
        OK_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, '#ok-button')
        ITEM_ORGANIZATION_FOLDER = (By.CLASS_NAME, "jenkins_branch_OrganizationFolder")
        ITEM_PIPELINE_PROJECT = (By.CLASS_NAME, "org_jenkinsci_plugins_workflow_job_WorkflowJob")
        ITEM_FREESTYLE_PROJECT = (By.CLASS_NAME, "hudson_model_FreeStyleProject")
        ITEM_MULTIBRANCH_PIPELINE_PROJECT = (
            By.CLASS_NAME, "org_jenkinsci_plugins_workflow_multibranch_WorkflowMultiBranchProject"
        )

        SELECTED_ITEM = (By.XPATH, "//li[@aria-checked='true']")
        ACTIVE_ITEM = (By.CLASS_NAME, "active")

        ERROR_MESSAGE = (By.ID, "itemname-required")
        ANY_ENABLED_ERROR = (By.CSS_SELECTOR, ".input-validation-message:not(.input-message-disabled)")

        ITEM_MULTI_CONFIG_PROJECT = (By.CLASS_NAME, "hudson_matrix_MatrixProject")
        ITEM_TYPES = (By.CSS_SELECTOR, ".label")
        ITEM_DESCRIPTIONS = (By.XPATH, "//div[@class='desc']")
        COPY_FROM = (By.ID, "from")
        DROPDOWN_COPY = (By.CSS_SELECTOR, "div.jenkins-dropdown")

    def __init__(self, driver, timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + "/view/all/newJob"

    @allure.step("Create new folder: \"{name}\"")
    def create_new_folder(self, name):
        from pages.folder_config_page import FolderConfigPage
        self.wait_for_element(self.Locators.ITEM_NAME).send_keys(name)
        self.wait_to_be_clickable(self.Locators.ITEM_FOLDER).click()
        self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        return FolderConfigPage(self.driver, name).wait_for_url()

    @allure.step("Create new Pipeline project: \"{name}\"")
    def create_new_pipeline_project(self, name):
        from pages.pipeline_config_page import PipelineConfigPage
        self.enter_item_name(name).click_pipeline_project().click_ok_button()
        return PipelineConfigPage(self.driver, name).wait_for_url()

    @allure.step("Click \"OK\" button")
    def click_ok_button(self):
        return self.click_on(self.Locators.OK_BUTTON)

    @allure.step("Click \"Pipeline\" project")
    def click_pipeline_project(self):
        self.click_on(self.Locators.ITEM_PIPELINE_PROJECT)
        return self

    @allure.step("Create new Multi-configuration project: \"{name}\"")
    def create_new_multi_config_project(self, name):
        from pages.multi_config_project_config_page import MultiConfigProjectConfigPage
        self.wait_for_element(self.Locators.ITEM_NAME).send_keys(name)
        item_multi_config_project = self.wait_to_be_clickable(self.Locators.ITEM_MULTI_CONFIG_PROJECT)
        self.scroll_into_view(item_multi_config_project)
        item_multi_config_project.click()
        self.wait_to_be_clickable(self.Locators.OK_BUTTON).click()
        return MultiConfigProjectConfigPage(self.driver, name).wait_for_url()

    def get_dropdown_text(self):
        try:
            return self.get_visible_text_lines(self.Locators.DROPDOWN_COPY)
        except TimeoutException:
            self.logger.error("Dropdown did not appear: element is not visible on the page.")
            return []

    @allure.step("Enter \"{name}\" in the \"Item Name\" field")
    def enter_item_name(self, name):
        self.enter_text(self.Locators.ITEM_NAME, name)
        return self

    def enter_copy_from(self, name):
        self.enter_text(self.Locators.COPY_FROM, name)
        return self

    @allure.step("Enter the first character of the item name into the 'Copy from' input field")
    def enter_first_character_in_copy_from(self, name):
        self.enter_copy_from(name[0])
        return self

    @allure.step("Try to copy from non-existent item: \"{copy_name}\", redirect to error page")
    def go_to_error_page_copy(self, name, copy_name):
        from pages.error_page_copy_from import ErrorPageCopyFrom
        self.enter_item_name(name).enter_copy_from(copy_name).click_ok_button()
        return ErrorPageCopyFrom(self.driver).wait_for_url()

    @allure.step("Click an item from dropdown")
    def select_item_from_dropdown(self):
        return self.click_on(self.Locators.DROPDOWN_COPY)

    def get_copy_from_field_value(self):
        return self.wait_and_get_attribute(self.Locators.COPY_FROM, "value")
