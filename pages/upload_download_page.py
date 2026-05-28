"""Upload and download page object."""

from __future__ import annotations  # type hints future behavior kosam

from pathlib import Path  # file paths create/check cheyyadaniki standard library

from playwright.sync_api import expect  # Playwright assertion library import chestamu

from pages.base_page import BasePage  # common actions inherit cheyyadaniki


class UploadDownloadPage(BasePage):
    """File upload and download workflows."""

    def open_upload_page(self) -> None:  # upload page open method
        self.open("/upload")  # upload route open chestundi

    def upload_file(self, file_path: Path) -> None:  # file upload action method
        self.page.locator("#file-upload").set_input_files(str(file_path))  # CSS id locator; file input hidden style lo undachu kabatti direct input locator use chestamu
        self.button("Upload").click()  # role button locator; accessible upload submit button click chestundi

    def verify_uploaded_file(self, file_name: str) -> None:  # uploaded file name verify method
        expect(self.page.locator("#uploaded-files")).to_have_text(file_name)  # CSS id locator; result element ki role ledu kabatti CSS second preference

    def open_download_page(self) -> None:  # download page open method
        self.open("/download")  # download route open chestundi

    def download_first_file(self, downloads_dir: Path) -> Path:  # first downloadable file save cheyyadaniki method
        first_file = self.page.locator(".example a").first()  # CSS scoped locator; download links dynamic names kabatti first link select chestamu
        with self.page.expect_download() as download_info:  # expect_download file download event kosam wait chestundi
            first_file.click()  # first download link click chestamu
        download = download_info.value  # Playwright Download object collect chestamu
        target_path = downloads_dir / download.suggested_filename  # browser suggested filename tho save path build chestamu
        return self.save_download(download, target_path)  # BasePage helper download save chesi path return chestundi
