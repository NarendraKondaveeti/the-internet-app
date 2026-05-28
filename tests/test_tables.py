"""Sortable table tests."""

from __future__ import annotations  # modern type hints support kosam

import pytest  # pytest marker support kosam

from pages.tables_page import TablesPage  # TablesPage POM import chestamu


@pytest.mark.ui  # UI test marker
@pytest.mark.regression  # regression suite marker
def test_table_data_visible_and_sortable(page) -> None:  # table data and sort behavior test
    tables_page = TablesPage(page)  # table page object create chestamu
    tables_page.open_tables_page()  # /tables route open chestamu
    assert tables_page.row_count() == 4  # Python assert; table lo expected 4 rows unnaya ani check chestundi
    tables_page.verify_cell_visible("Smith")  # table cell content visible ani verify chestamu
    tables_page.sort_by_column("Last Name")  # Last Name header click chesi sort trigger chestamu
    tables_page.verify_cell_visible("Doe")  # sort taruvata table still valid content show chestunda ani check chestamu
