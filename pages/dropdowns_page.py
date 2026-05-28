"""Dropdown page object."""

from __future__ import annotations  # modern type hints support kosam

from playwright.sync_api import expect  # Playwright assertion library import chestamu

from pages.base_page import BasePage  # common navigation and assertions inherit cheyyadaniki


class DropdownsPage(BasePage):
    """Dropdown interactions."""

    def open_dropdown_page(self) -> None:  # dropdown page ki navigate cheyyadaniki method
        self.open("/dropdown")  # relative URL; config base_url tho combine avtundi

    def select_option(self, label: str) -> None:  # dropdown option select cheyyadaniki method
        dropdown = self.page.locator("#dropdown")  # CSS id locator; native select ki label ledu kabatti second preference CSS use chestamu
        dropdown.select_option(label=label)  # Playwright select_option method; visible label based option select chestundi

    def verify_selected_option(self, label: str) -> None:  # selected option verify cheyyadaniki method
        selected = self.page.locator("#dropdown option:checked")  # CSS pseudo selector; selected option check cheyyadaniki best direct strategy
        expect(selected).to_have_text(label)  # selected option text expected label tho compare chestundi
