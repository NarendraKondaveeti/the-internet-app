"""Form Authentication page object."""

from __future__ import annotations  # annotations future mode enable chestundi

from playwright.sync_api import expect  # assertion helper import chestamu

from locators.form_locators import FLASH_ID, LOGIN_BUTTON_NAME, PASSWORD_LABEL, USERNAME_LABEL  # form locator names import chestamu
from pages.base_page import BasePage  # BasePage common actions kosam


class LoginPage(BasePage):
    """Login page specific actions."""

    def open_login_page(self) -> None:  # login page open method
        self.open("/login")  # relative URL use chestamu because base_url conftest lo configured undi

    def login(self, username: str, password: str) -> None:  # username/password submit cheyyadaniki method
        self.page.get_by_label(USERNAME_LABEL).fill(username)  # get_by_label Playwright built-in locator; label association stable kabatti first preference
        self.page.get_by_label(PASSWORD_LABEL).fill(password)  # password field label based locator; CSS avoid chestamu because semantic locator available undi
        self.button(LOGIN_BUTTON_NAME).click()  # role button locator; user click chese Login button ni represent chestundi

    def verify_flash_message(self, expected_message: str) -> None:  # login result message verify cheyyadaniki method
        flash = self.page.locator(FLASH_ID)  # CSS id locator; flash message ki accessible role ledu kabatti CSS second preference
        expect(flash).to_contain_text(expected_message)  # expected text partial match assertion auto-wait tho run avtundi

    def logout(self) -> None:  # secure area nundi logout cheyyadaniki method
        self.link("Logout").click()  # role=link locator; visible Logout link stable ga locate avtundi
