from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FolderConfigPage(BasePage):
    class Locators:
        GENERAL_BUTTON = (By.ID, "general")
        SAVE_BUTTON = (By.CSS_SELECTOR, "[name='Submit']")
        DESCRIPTION = (By.XPATH, "//*[@id='view-message']")
        DESCRIPTION_FIELD = (By.CSS_SELECTOR, "div.setting-main> textarea")
        PREVIEW = (By.CLASS_NAME, "textarea-show-preview")
        TEXT_PREVIEW = (By.CLASS_NAME, "textarea-preview")
        HIDE_PREVIEW = (By.CLASS_NAME, "textarea-hide-preview")
        HEALTH_METRICS = (By.ID, "health-metrics")
        FOLDER_NAME = (By.CSS_SELECTOR, "#main-panel> h1")

    def __init__(self, driver, folder_name,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{folder_name}/configure"
        self.name = folder_name
