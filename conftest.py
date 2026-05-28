"""Pytest fixtures and hooks for the automation framework."""

from __future__ import annotations  # type hint evaluation postpone cheyyadaniki

import os  # Python standard library; environment variables set/read cheyyadaniki
from pathlib import Path  # artifact paths create cheyyadaniki standard library
from typing import Generator  # fixture return type explain cheyyadaniki

import pytest  # pytest framework; fixtures and hooks kosam
from playwright.sync_api import Browser, BrowserContext, Page, Playwright  # Playwright sync API types import chestamu

from api.api_client import ApiClient  # reusable API client fixture kosam
from utils.config_reader import ConfigReader  # environment config load cheyyadaniki
from utils.logger import get_logger  # colorful execution logs kosam


PROJECT_ROOT = Path(__file__).resolve().parent  # project root path store chestundi
ARTIFACT_DIRS = ["reports", "screenshots", "logs", "downloads", "traces", "videos"]  # required artifact folders list
logger = get_logger("pytest")  # pytest hooks lo use cheyyadaniki logger create chestamu


def pytest_addoption(parser: pytest.Parser) -> None:  # custom command line options add cheyyadaniki pytest hook
    parser.addoption("--env", action="store", default=None, help="qa/local environment select cheyyadaniki option")  # --env option runtime config choose chestundi
    parser.addoption("--headed-mode", action="store_true", default=False, help="browser headed ga run cheyyadaniki option")  # visible browser run kosam flag
    parser.addoption("--slow-mo", action="store", default=None, help="learning visibility kosam slow motion milliseconds")  # execution speed slow cheyyadaniki option


@pytest.fixture(scope="session")
def config(pytestconfig: pytest.Config) -> ConfigReader:  # session level config fixture
    cli_env = pytestconfig.getoption("--env")  # command line nundi env value read chestamu
    if cli_env:  # user --env pass chesthe
        os.environ["TEST_ENV"] = cli_env  # environment variable set chesi ConfigReader ki pass chestamu
    return ConfigReader()  # selected config object return chestamu


@pytest.fixture(scope="session", autouse=True)
def create_artifact_dirs() -> None:  # session start lo required folders create cheyyadaniki autouse fixture
    for folder in ARTIFACT_DIRS:  # each artifact folder loop chestamu
        (PROJECT_ROOT / folder).mkdir(exist_ok=True)  # folder lekapothe create chestamu


@pytest.fixture(scope="session")
def browser(config: ConfigReader, pytestconfig: pytest.Config, playwright: Playwright) -> Generator[Browser, None, None]:  # custom browser fixture
    browser_name = config.get("browser", "chromium")  # config nundi browser name read chestamu
    headed = bool(config.get("headed")) or bool(pytestconfig.getoption("--headed-mode"))  # config/CLI based headed mode decide chestamu
    slow_mo = int(pytestconfig.getoption("--slow-mo") or config.get("slow_mo", 0))  # learning visibility kosam slow_mo set chestamu
    logger.info("TEST SESSION STARTED | browser=%s | headed=%s | slow_mo=%s", browser_name, headed, slow_mo)  # start log print chestamu
    browser_type = getattr(playwright, browser_name)  # chromium/firefox/webkit object dynamically select chestamu
    browser_instance = browser_type.launch(headless=not headed, slow_mo=slow_mo)  # Playwright launch method browser open chestundi
    yield browser_instance  # tests run ayye varaku browser provide chestamu
    browser_instance.close()  # session end lo browser close chestamu
    logger.info("TEST SESSION ENDED")  # end log print chestamu


@pytest.fixture()
def context(browser: Browser, config: ConfigReader) -> Generator[BrowserContext, None, None]:  # each test ki isolated browser context
    context_instance = browser.new_context(  # Playwright browser context create chestundi
        base_url=config.base_url,  # relative URLs direct ga use cheyyadaniki base_url set chestamu
        accept_downloads=True,  # download tests ki files accept cheyyadaniki enable chestamu
        record_video_dir=str(PROJECT_ROOT / "videos"),  # failed test videos save avvadaniki folder
    )
    context_instance.set_default_timeout(int(config.get("timeout", 10000)))  # all actions ki default timeout set chestamu
    context_instance.tracing.start(screenshots=True, snapshots=True, sources=True)  # trace recording start chestamu
    yield context_instance  # test ki context return chestamu
    context_instance.close()  # test complete ayyaka context close chestamu


@pytest.fixture()
def page(context: BrowserContext) -> Generator[Page, None, None]:  # each test ki new page fixture
    page_instance = context.new_page()  # Playwright new tab/page create chestundi
    yield page_instance  # test method ki page provide chestamu


@pytest.fixture()
def api_client(config: ConfigReader) -> ApiClient:  # API automation fixture
    return ApiClient(config)  # configured API client return chestamu


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[object]) -> Generator[None, None, None]:  # test result hook
    outcome = yield  # pytest internal result wait chestamu
    report = outcome.get_result()  # test report object get chestamu
    setattr(item, f"rep_{report.when}", report)  # fixture teardown lo status use cheyyadaniki report attach chestamu
    if report.when == "call":  # actual test body finish ayyaka matrame log chestamu
        status = "PASSED" if report.passed else "FAILED" if report.failed else "SKIPPED"  # readable status decide chestamu
        logger.info("TEST %s | %s", status, item.nodeid)  # test pass/fail terminal lo print chestamu


@pytest.fixture(autouse=True)
def artifacts_on_failure(request: pytest.FixtureRequest, page: Page, context: BrowserContext) -> Generator[None, None, None]:  # failed tests ki artifacts collect chestundi
    logger.info("TEST START | %s", request.node.nodeid)  # test start log display chestamu
    yield  # test execute avvadaniki control pytest ki istamu
    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed  # test failed ayinda ani check chestamu
    safe_name = request.node.nodeid.replace("/", "_").replace("\\", "_").replace("::", "__").replace("[", "_").replace("]", "_")  # file safe name create chestamu
    trace_path = PROJECT_ROOT / "traces" / f"{safe_name}.zip"  # trace artifact path
    context.tracing.stop(path=str(trace_path))  # trace zip file ga save chestamu
    if failed:  # failure unte screenshot capture chestamu
        screenshot_path = PROJECT_ROOT / "screenshots" / f"{safe_name}.png"  # screenshot path create chestamu
        page.screenshot(path=str(screenshot_path), full_page=True)  # Playwright screenshot method full page capture chestundi
        logger.error("FAILED STEP DETAILS | screenshot=%s | trace=%s", screenshot_path, trace_path)  # artifact paths terminal lo print chestamu
    logger.info("TEST END | %s", request.node.nodeid)  # test end log display chestamu
