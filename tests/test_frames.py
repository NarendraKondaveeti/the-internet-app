"""Frame and iframe tests."""

from __future__ import annotations  # type hint future mode kosam

import pytest  # pytest marker support kosam

from pages.widgets_page import WidgetsPage  # generic widgets POM import chestamu


@pytest.mark.ui  # browser based test marker
@pytest.mark.regression  # regression suite marker
def test_nested_frames_available(page) -> None:  # frames page navigation test
    widgets_page = WidgetsPage(page)  # shared widgets page object create chestamu
    widgets_page.open_path("/frames")  # frames landing page open chestamu
    widgets_page.verify_text_visible("Nested Frames")  # nested frames link/text visible ani verify chestamu
    widgets_page.verify_text_visible("iFrame")  # iframe link/text visible ani verify chestamu


@pytest.mark.ui  # UI marker
@pytest.mark.regression  # regression marker
def test_iframe_text_editor_visible(page) -> None:  # iframe editor content test
    widgets_page = WidgetsPage(page)  # widgets page object create chestamu
    widgets_page.open_path("/iframe")  # iframe route open chestamu
    widgets_page.switch_to_iframe_and_verify_text("mce_0_ifr", "Your content goes here.")  # frame_locator tho iframe text validate chestamu
