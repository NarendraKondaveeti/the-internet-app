"""Sortable data tables page object."""

from __future__ import annotations  # forward type annotations kosam

from playwright.sync_api import expect  # Playwright assertions import chestamu

from locators.table_locators import TABLE_ONE_ID  # stable table id constant import chestamu
from pages.base_page import BasePage  # common methods inherit cheyyadaniki


class TablesPage(BasePage):
    """Table validations and sorting actions."""

    def open_tables_page(self) -> None:  # tables page open cheyyadaniki method
        self.open("/tables")  # relative navigation use chestamu

    def sort_by_column(self, column_name: str) -> None:  # table header click chesi sort cheyyadaniki method
        self.page.locator(TABLE_ONE_ID).get_by_role("link", name=column_name).click()  # table scope + role link; header links accessible kabatti first preference

    def verify_cell_visible(self, text: str) -> None:  # table cell content visible check
        expect(self.page.locator(TABLE_ONE_ID).get_by_text(text)).to_be_visible()  # table scoped get_by_text; duplicate text risk reduce chestundi

    def row_count(self) -> int:  # table rows count return cheyyadaniki method
        return self.page.locator(f"{TABLE_ONE_ID} tbody tr").count()  # CSS tbody row selector; row count ki direct and stable
