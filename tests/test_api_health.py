"""API support tests for the same application host."""

from __future__ import annotations  # type hints future support kosam

import pytest  # pytest markers kosam


@pytest.mark.api  # API suite marker
@pytest.mark.smoke  # smoke validation marker
def test_home_page_api_health(api_client) -> None:  # API client fixture use chese health test
    response = api_client.get("/")  # requests GET call root endpoint ki send chestamu
    assert response.status_code == 200  # Python assert; server OK response ichinda check chestundi
    assert "Welcome to the-internet" in response.text  # response HTML lo expected text unda verify chestundi
