"""Explicit wait helpers for rare cases where auto-wait is not enough."""

from __future__ import annotations  # type annotations runtime cost reduce cheyyadaniki

from playwright.sync_api import Locator, Page  # Playwright classes; type hints and methods kosam


class WaitUtils:
    """Playwright auto-wait primary; ee helpers special cases ki matrame."""

    @staticmethod
    def wait_for_visible(locator: Locator, timeout: int = 10000) -> None:  # locator visible ayye varaku wait chestundi
        locator.wait_for(state="visible", timeout=timeout)  # wait_for Playwright method; explicit visibility sync kosam

    @staticmethod
    def wait_for_network_idle(page: Page) -> None:  # network complete ayye varaku wait cheyyadaniki helper
        page.wait_for_load_state("networkidle")  # networkidle state API calls settle ayyaka continue chestundi
