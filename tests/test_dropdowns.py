"""Dropdown tests."""

from __future__ import annotations  # type annotations future mode kosam

import pytest  # pytest markers and runner kosam

from pages.dropdowns_page import DropdownsPage  # DropdownsPage POM import chestamu


@pytest.mark.ui  # browser based test marker
@pytest.mark.smoke  # quick validation suite marker
def test_select_each_dropdown_option(page) -> None:  # dropdown option selection test
    dropdown_page = DropdownsPage(page)  # page object create chestamu
    dropdown_page.open_dropdown_page()  # dropdown page open chestamu
    dropdown_page.select_option("Option 1")  # visible label tho Option 1 select chestamu
    dropdown_page.verify_selected_option("Option 1")  # selected option Option 1 ani validate chestamu
    dropdown_page.select_option("Option 2")  # visible label tho Option 2 select chestamu
    dropdown_page.verify_selected_option("Option 2")  # selected option Option 2 ani validate chestamu
