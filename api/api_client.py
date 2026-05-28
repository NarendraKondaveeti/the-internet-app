"""Reusable API client for API + UI automation support."""

from __future__ import annotations  # type annotations forward references support kosam

from typing import Any  # response json dynamic kabatti Any use chestamu

import requests  # requests package; simple API validation ki use chestamu

from utils.config_reader import ConfigReader  # project config reader import chestamu


class ApiClient:
    """Base API client; UI tests ki backend health verify cheyyadaniki use cheyyachu."""

    def __init__(self, config: ConfigReader) -> None:  # constructor; config object receive chestundi
        self.base_url = config.api_base_url.rstrip("/")  # trailing slash remove chesi clean base url store chestamu
        self.session = requests.Session()  # session object reuse chestamu so headers/cookies maintain avvachu

    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:  # GET request reusable wrapper
        url = f"{self.base_url}/{endpoint.lstrip('/')}"  # base url and endpoint combine chestamu
        response = self.session.get(url, timeout=15, **kwargs)  # requests GET method call chestamu
        return response  # caller status code/body assertions cheyyadaniki response return chestamu
