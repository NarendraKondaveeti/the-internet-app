"""Filter and status code style validation tests."""

from __future__ import annotations  # type hints future mode kosam

import pytest  # pytest framework import chestamu

from pages.widgets_page import WidgetsPage  # generic page object import chestamu


@pytest.mark.ui  # UI test marker
@pytest.mark.regression  # regression marker
def test_status_codes_filter_like_navigation(page) -> None:  # status code link filtering/navigation validation
    widgets_page = WidgetsPage(page)  # widgets page object create chestamu
    widgets_page.open_path("/status_codes")  # status codes page open chestamu
    widgets_page.link("200").click()  # role link locator; status filter/navigation 200 click chestamu
    widgets_page.verify_text_visible("This page returned a 200 status code.")  # resulting content verify chestamu
