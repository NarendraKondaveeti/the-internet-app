"""General form/input tests."""

from __future__ import annotations  # type hints future behavior kosam

import pytest  # pytest marker support kosam

from pages.widgets_page import WidgetsPage  # shared widgets page object


@pytest.mark.ui  # UI test marker
@pytest.mark.regression  # regression suite marker
def test_number_input_accepts_value(page) -> None:  # number input form test
    widgets_page = WidgetsPage(page)  # page object create chestamu
    widgets_page.open_path("/inputs")  # inputs page open chestamu
    widgets_page.enter_number("12345")  # number input lo value fill chesi assertion chestamu
