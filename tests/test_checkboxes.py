"""Checkbox workflow tests."""

from __future__ import annotations  # type hints future mode kosam

import pytest  # pytest framework import chestamu

from pages.widgets_page import WidgetsPage  # widgets page object import chestamu


@pytest.mark.ui  # UI category marker
@pytest.mark.smoke  # smoke suite marker
def test_checkbox_can_be_checked(page) -> None:  # checkbox interaction test
    widgets_page = WidgetsPage(page)  # widgets POM create chestamu
    widgets_page.open_path("/checkboxes")  # checkboxes route open chestamu
    widgets_page.check_checkbox(0)  # first checkbox check chesi checked state assert chestamu
