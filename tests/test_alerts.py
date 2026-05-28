"""JavaScript alert, confirm, and prompt tests."""

from __future__ import annotations  # type hints future behavior kosam

import pytest  # pytest framework import chestamu

from pages.alerts_page import AlertsPage  # AlertsPage POM import chestamu


@pytest.mark.ui  # browser UI test marker
@pytest.mark.regression  # complete regression marker
def test_javascript_alert_accept(page) -> None:  # JS alert accept test
    alerts_page = AlertsPage(page)  # AlertsPage object create chestamu
    alerts_page.open_alerts_page()  # alerts page open chestamu
    alerts_page.accept_alert()  # alert popup OK click chestamu
    alerts_page.verify_result("You successfully clicked an alert")  # result text assert chestamu


@pytest.mark.ui  # UI test marker
@pytest.mark.regression  # regression marker
def test_javascript_confirm_dismiss(page) -> None:  # JS confirm cancel test
    alerts_page = AlertsPage(page)  # page object create chestamu
    alerts_page.open_alerts_page()  # page open chestamu
    alerts_page.dismiss_confirm()  # confirm popup Cancel click chestamu
    alerts_page.verify_result("You clicked: Cancel")  # cancel result validate chestamu


@pytest.mark.ui  # UI marker
@pytest.mark.regression  # regression marker
def test_javascript_prompt_submit_text(page) -> None:  # JS prompt input test
    alerts_page = AlertsPage(page)  # page object initialize chestamu
    alerts_page.open_alerts_page()  # prompt page route open chestamu
    alerts_page.submit_prompt("Telugu Playwright Learning")  # prompt lo sample text submit chestamu
    alerts_page.verify_result("You entered: Telugu Playwright Learning")  # prompt result text verify chestamu
