from pages.base_page import BasePage


class FolderConfigPage(BasePage):
    def __init__(self, driver, folder_name,  timeout=5):
        super().__init__(driver, timeout=timeout)
        self.url = self.base_url + f"/job/{folder_name}/configure"
        self.name = folder_name
