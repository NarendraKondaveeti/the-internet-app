"""JavaScript alerts page object."""

from __future__ import annotations  # type hints future behavior kosam

from playwright.sync_api import expect  # assertion library import chestamu

from pages.base_page import BasePage  # common page actions inherit cheyyadaniki


class AlertsPage(BasePage):
    """Alert, confirm, and prompt workflows."""

    def open_alerts_page(self) -> None:  # alerts page navigate method
        self.open("/javascript_alerts")  # page route open chestundi

    def accept_alert(self) -> None:  # normal JS alert accept cheyyadaniki method
        with self.page.expect_dialog() as dialog_info:  # expect_dialog Playwright sync wait; popup open ayye varaku wait chestundi
            self.button("Click for JS Alert").click()  # role button locator; alert trigger click chestundi
        dialog_info.value.accept()  # Dialog accept method; alert OK click chestundi

    def dismiss_confirm(self) -> None:  # confirm dialog cancel cheyyadaniki method
        with self.page.expect_dialog() as dialog_info:  # dialog popup ni capture cheyyadaniki event wait
            self.button("Click for JS Confirm").click()  # confirm button click chestundi
        dialog_info.value.dismiss()  # dismiss method Cancel action perform chestundi

    def submit_prompt(self, value: str) -> None:  # prompt text enter cheyyadaniki method
        with self.page.expect_dialog() as dialog_info:  # prompt dialog open ayye varaku wait chestamu
            self.button("Click for JS Prompt").click()  # prompt trigger button click chestamu
        dialog_info.value.accept(value)  # accept(value) prompt lo text enter chesi OK click chestundi

    def verify_result(self, expected_text: str) -> None:  # result message verify cheyyadaniki method
        expect(self.page.locator("#result")).to_have_text(expected_text)  # CSS id locator; result element ki role ledu kabatti second preference
