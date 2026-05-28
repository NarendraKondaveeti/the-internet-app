"""Base page object with common browser actions."""

from __future__ import annotations  # future annotations; type hints runtime lo evaluate kakunda help chestundi

from pathlib import Path  # file paths clean ga handle cheyyadaniki standard library

import re  # Python regex module; URL partial match pattern create cheyyadaniki

from playwright.sync_api import Download, Locator, Page, expect  # Playwright classes and expect assertion import chestamu


class BasePage:
    """Common methods anni page objects reuse cheyyadaniki base class."""

    def __init__(self, page: Page) -> None:  # constructor; page fixture object receive chestundi
        self.page = page  # Playwright Page object ni instance variable lo store chestamu

    def open(self, path: str = "/") -> None:  # page open cheyyadaniki reusable method
        self.page.goto(path)  # goto Playwright method; base_url configured kabatti relative path use cheyyachu

    def heading(self, name: str) -> Locator:  # heading locator create cheyyadaniki helper
        return self.page.get_by_role("heading", name=name)  # get_by_role Playwright built-in locator; accessibility based stable strategy

    def link(self, name: str) -> Locator:  # link locator helper
        return self.page.get_by_role("link", name=name)  # role=link user visible link ni identify chestundi

    def button(self, name: str) -> Locator:  # button locator helper
        return self.page.get_by_role("button", name=name)  # role=button accessible name tho stable ga locate chestundi

    def assert_text_visible(self, text: str) -> None:  # visible text assertion common method
        expect(self.page.get_by_text(text)).to_be_visible()  # get_by_text user visible text kabatti beginner friendly locator

    def assert_url_contains(self, partial_url: str) -> None:  # current URL partial match verify chestundi
        expect(self.page).to_have_url(re.compile(f".*{re.escape(partial_url)}.*"))  # regex URL assertion; partial URL auto-wait tho verify chestundi

    def save_download(self, download: Download, target_path: Path) -> Path:  # download artifact save cheyyadaniki helper
        download.save_as(str(target_path))  # save_as Playwright Download method; file local path lo save chestundi
        return target_path  # test assertions kosam saved path return chestamu
