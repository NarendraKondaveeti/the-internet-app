"""Child window page object."""

from __future__ import annotations  # future annotations enable chestundi

from playwright.sync_api import Page, expect  # Page type and expect assertion import chestamu

from pages.base_page import BasePage  # BasePage inherit cheyyadaniki


class WindowsPage(BasePage):
    """New tab / child window workflows."""

    def open_windows_page(self) -> None:  # windows page navigate method
        self.open("/windows")  # child window example route open chestundi

    def open_child_window(self) -> Page:  # new tab open chesi child page return chestundi
        with self.page.context.expect_page() as new_page_info:  # expect_page new tab/window event kosam wait chestundi
            self.link("Click Here").click()  # role link locator; new window trigger click chestundi
        child_page = new_page_info.value  # captured child Page object store chestamu
        child_page.wait_for_load_state()  # child page load complete ayye varaku wait chestamu
        return child_page  # test lo assertions cheyyadaniki child page return chestamu

    @staticmethod
    def verify_child_window(child_page: Page) -> None:  # child page content verify method
        expect(child_page.get_by_role("heading", name="New Window")).to_be_visible()  # role heading locator; accessible and stable first preference
