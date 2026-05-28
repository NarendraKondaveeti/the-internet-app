"""Upload and download workflow tests."""

from __future__ import annotations  # type hints future support kosam

from pathlib import Path  # file paths handle cheyyadaniki standard library

import pytest  # pytest markers kosam

from pages.upload_download_page import UploadDownloadPage  # POM import chestamu


PROJECT_ROOT = Path(__file__).resolve().parents[1]  # project root path locate chestamu


@pytest.mark.ui  # browser UI marker
@pytest.mark.regression  # regression suite marker
def test_file_upload(page) -> None:  # file upload test
    upload_page = UploadDownloadPage(page)  # upload/download POM create chestamu
    sample_file = PROJECT_ROOT / "testdata" / "upload_sample.txt"  # upload cheyyalsina sample file path
    upload_page.open_upload_page()  # upload page open chestamu
    upload_page.upload_file(sample_file)  # file input lo sample file attach chesi submit chestamu
    upload_page.verify_uploaded_file(sample_file.name)  # uploaded file name page lo kanipistunda verify chestamu


@pytest.mark.ui  # UI test marker
@pytest.mark.regression  # regression marker
def test_file_download(page) -> None:  # file download test
    upload_page = UploadDownloadPage(page)  # reusable page object create chestamu
    downloads_dir = PROJECT_ROOT / "downloads"  # downloaded files save ayye folder
    upload_page.open_download_page()  # download page open chestamu
    downloaded_path = upload_page.download_first_file(downloads_dir)  # first available download file save chestamu
    assert downloaded_path.exists()  # Python assert; file actual ga disk lo save ayinda ani check chestundi
