"""Home page object for The Internet application."""

from __future__ import annotations  # type hints future behavior enable chestundi

from playwright.sync_api import expect  # Playwright expect assertions import chestamu

from locators.home_locators import AVAILABLE_EXAMPLES_TEXT, HOME_HEADING_TEXT  # locator constants import chestamu
from pages.base_page import BasePage  # common actions inherit cheyyadaniki base page import


class HomePage(BasePage):
    """Home page actions and validations."""

    def open_home_page(self) -> None:  # home page open cheyyadaniki readable method
        self.open("/")  # BasePage open method; root URL ki navigate chestundi

    def verify_home_loaded(self) -> None:  # home page load ayinda ani validate chestundi
        expect(self.heading(HOME_HEADING_TEXT)).to_be_visible()  # heading role locator accessibility based kabatti first preference
        expect(self.page.get_by_text(AVAILABLE_EXAMPLES_TEXT)).to_be_visible()  # visible text locator section presence validate chestundi

    def open_example(self, link_name: str) -> None:  # any example link open cheyyadaniki generic action
        self.link(link_name).click()  # get_by_role link locator click chestundi; Playwright auto-wait handles readiness
