"""Common assertion wrappers for readable test intent."""

from __future__ import annotations  # future annotations; clean type hints kosam

from playwright.sync_api import Locator, Page, expect  # Playwright expect assertions import chestamu


class CommonAssertions:
    """Reusable assertions so tests readable and beginner friendly ga untayi."""

    @staticmethod
    def should_have_title(page: Page, expected_title: str) -> None:  # page title verify cheyyadaniki method
        expect(page).to_have_title(expected_title)  # Playwright assertion; browser title expected value tho compare chestundi

    @staticmethod
    def should_be_visible(locator: Locator) -> None:  # element visible unda ani verify cheyyadaniki method
        expect(locator).to_be_visible()  # auto-wait assertion; element visible ayye varaku wait chestundi

    @staticmethod
    def should_contain_text(locator: Locator, expected_text: str) -> None:  # element text verify helper
        expect(locator).to_contain_text(expected_text)  # partial text match kosam Playwright assertion
