"""Child window / new tab tests."""

from __future__ import annotations  # future annotations enable chestundi

import pytest  # pytest marker support kosam

from pages.windows_page import WindowsPage  # WindowsPage POM import chestamu


@pytest.mark.ui  # UI category marker
@pytest.mark.regression  # regression suite marker
def test_open_child_window_and_validate_content(page) -> None:  # child window workflow test
    windows_page = WindowsPage(page)  # page object create chestamu
    windows_page.open_windows_page()  # /windows page open chestamu
    child_page = windows_page.open_child_window()  # click chesi new tab capture chestamu
    windows_page.verify_child_window(child_page)  # child tab heading validate chestamu
    child_page.close()  # child window close chestamu so test cleanup neat ga untundi
