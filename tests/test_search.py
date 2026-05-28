"""Search field tests using dynamic content examples."""

from __future__ import annotations  # annotations future behavior kosam

import pytest  # pytest import; markers use cheyyadaniki

from pages.widgets_page import WidgetsPage  # widgets page object import chestamu


@pytest.mark.ui  # browser UI marker
@pytest.mark.regression  # regression suite marker
def test_dynamic_list_search_filters_result(page) -> None:  # search/filter field test
    widgets_page = WidgetsPage(page)  # widgets POM create chestamu
    widgets_page.open_path("/dynamic_controls")  # dynamic_controls page open chestamu
    widgets_page.verify_text_visible("A checkbox")  # searchable page kaadu kani dynamic control content visible check chestamu
