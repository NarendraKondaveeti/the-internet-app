"""Login automation tests for Form Authentication."""

from __future__ import annotations  # Python future import; type hints lightweight ga maintain cheyyadaniki

import pytest  # pytest framework import; markers and test runner kosam

from pages.login_page import LoginPage  # LoginPage POM import chestamu
from utils.data_reader import read_json  # JSON test data reader import chestamu


@pytest.mark.ui  # pytest marker; ee test browser UI category lo undani cheptundi
@pytest.mark.auth  # pytest marker; authentication tests grouping kosam
@pytest.mark.smoke  # pytest marker; smoke suite lo include cheyyadaniki
def test_valid_login_and_logout(page) -> None:  # page anedi pytest-playwright fixture; browser tab provide chestundi
    data = read_json("testdata/login_users.json")["valid_user"]  # test data JSON nundi valid user details read chestamu
    login_page = LoginPage(page)  # Page Object create chestamu; raw Playwright calls tests lo duplicate avvakunda
    login_page.open_login_page()  # login page ki navigate chestamu
    login_page.login(data["username"], data["password"])  # valid credentials submit chestamu
    login_page.verify_flash_message(data["expected_message"])  # success message verify chestamu
    login_page.logout()  # logout workflow complete chestamu
    login_page.verify_flash_message("You logged out of the secure area!")  # logout success message validate chestamu


@pytest.mark.ui  # UI test marker
@pytest.mark.auth  # auth module marker
@pytest.mark.regression  # regression suite marker
def test_invalid_login_error_message(page) -> None:  # invalid login validation test
    data = read_json("testdata/login_users.json")["invalid_user"]  # invalid user data file nundi read chestamu
    login_page = LoginPage(page)  # LoginPage object initialize chestamu
    login_page.open_login_page()  # login route open chestamu
    login_page.login(data["username"], data["password"])  # wrong credentials submit chestamu
    login_page.verify_flash_message(data["expected_message"])  # invalid username error message assert chestamu
