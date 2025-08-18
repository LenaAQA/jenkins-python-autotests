import pytest
import allure

from pages.multi_config_project_config_page import MultiConfigProjectConfigPage
from tests.multi_configuration_project_configuration.data import ProjectToggle


@pytest.fixture(scope="function")
@allure.title("Create Multi-configuration project")
def multi_config_project_enabled(new_item_page) -> MultiConfigProjectConfigPage:
    return new_item_page.create_new_multi_config_project(ProjectToggle.PROJECT_NAME)


@pytest.fixture(scope="function")
@allure.title("Prepare project page of disabled Multi-configuration project")
def page_disabled_multi_config_project(multi_config_project_enabled: MultiConfigProjectConfigPage):
    multi_config_project_enabled.click_switch_button()
    return multi_config_project_enabled.submit_and_open_project_page()
