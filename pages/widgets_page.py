"""Reusable page object for dynamic widgets and miscellaneous pages."""

from __future__ import annotations  # future type annotations kosam

from playwright.sync_api import expect  # Playwright assertion helper import chestamu

from pages.base_page import BasePage  # BasePage common actions inherit cheyyadaniki


class WidgetsPage(BasePage):
    """Checkboxes, inputs, dynamic controls, frames, tabs, hovers, filters, search-like pages."""

    def open_path(self, path: str) -> None:  # any route open cheyyadaniki generic helper
        self.open(path)  # BasePage open method call chestamu

    def check_checkbox(self, index: int = 0) -> None:  # checkbox select cheyyadaniki method
        checkbox = self.page.get_by_role("checkbox").nth(index)  # get_by_role checkbox locator; semantic locator first preference
        checkbox.check()  # Playwright check method; checkbox selected state set chestundi
        expect(checkbox).to_be_checked()  # assertion; checkbox checked ayinda validate chestundi

    def enter_number(self, value: str) -> None:  # inputs page lo number fill cheyyadaniki method
        number_input = self.page.locator("input[type='number']")  # CSS locator; number input ki label/placeholder ledu kabatti CSS second preference
        number_input.fill(value)  # fill Playwright method; input value enter chestundi
        expect(number_input).to_have_value(value)  # value correctly fill ayinda assert chestundi

    def filter_list(self, search_text: str) -> None:  # dynamic list filter/search field action
        self.page.get_by_placeholder("Search").fill(search_text)  # placeholder locator; user-visible hint kabatti first preference

    def verify_text_visible(self, text: str) -> None:  # generic visible text assertion
        expect(self.page.get_by_text(text)).to_be_visible()  # text locator; content presence check chestundi

    def switch_to_iframe_and_verify_text(self, frame_name: str, text: str) -> None:  # frame content verify helper
        frame = self.page.frame_locator(f"[name='{frame_name}']")  # CSS name selector; iframe accessible role ledu kabatti frame_locator with CSS
        expect(frame.get_by_text(text)).to_be_visible()  # frame scoped text locator; iframe content validate chestundi

    def click_tab(self, tab_text: str) -> None:  # horizontal/vertical tab click helper
        self.page.get_by_text(tab_text).click()  # visible tab text locator; examples page tab labels simple ga untayi
