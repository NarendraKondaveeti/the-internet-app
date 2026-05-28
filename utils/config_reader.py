"""Configuration reader for environment based framework settings."""

from __future__ import annotations  # Python future import; type hints runtime lo light ga undadaniki use chestamu

import os  # Python standard library; environment variables read cheyyadaniki use chestamu
from pathlib import Path  # Python standard library; file paths safe ga handle cheyyadaniki use chestamu
from typing import Any  # Python typing module; flexible return values explain cheyyadaniki use chestamu

import yaml  # PyYAML library; environments.yaml file parse cheyyadaniki use chestamu


PROJECT_ROOT = Path(__file__).resolve().parents[1]  # ee constant project root folder ni point chestundi
CONFIG_FILE = PROJECT_ROOT / "config" / "environments.yaml"  # ee path environment config file location ni store chestundi


class ConfigReader:
    """YAML config ni chadivi selected environment details provide chestundi."""

    def __init__(self) -> None:  # __init__ Python constructor; object create appudu run avtundi
        self._data = self._load_config()  # private variable lo YAML complete data save chestamu
        self.env_name = os.getenv("TEST_ENV", self._data.get("default", "qa"))  # env variable unte danini, lekapothe default qa use chestamu
        self.env = self._data[self.env_name]  # selected environment dictionary ni store chestamu

    def _load_config(self) -> dict[str, Any]:  # private helper method; YAML file ni dictionary ga return chestundi
        with CONFIG_FILE.open("r", encoding="utf-8") as file:  # with Python context manager; file automatic close avtundi
            return yaml.safe_load(file)  # safe_load YAML ni secure ga Python dict ga convert chestundi

    def get(self, key: str, default: Any | None = None) -> Any:  # generic getter; missing key ki default return chestundi
        return self.env.get(key, default)  # dict.get Python method; key lekapothe default istundi

    @property
    def base_url(self) -> str:  # property decorator; method ni variable laga access cheyyadaniki use chestamu
        return str(self.get("base_url"))  # base_url string ga return chestamu

    @property
    def api_base_url(self) -> str:  # API base url ki readable property
        return str(self.get("api_base_url"))  # API calls ki base endpoint return chestundi
