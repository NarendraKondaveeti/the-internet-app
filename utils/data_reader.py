"""Reusable test data reader utilities."""

from __future__ import annotations  # modern type hint syntax support kosam

import json  # Python json module; JSON test data read cheyyadaniki
from pathlib import Path  # safe file path handling kosam
from typing import Any  # generic data return type kosam


PROJECT_ROOT = Path(__file__).resolve().parents[1]  # project root locate chestundi


def read_json(relative_path: str) -> dict[str, Any]:  # JSON file ni dictionary ga return cheyyadaniki helper
    file_path = PROJECT_ROOT / relative_path  # relative path ni absolute project path ga convert chestamu
    with file_path.open("r", encoding="utf-8") as file:  # file open chesi automatic close cheyyadaniki with use chestamu
        return json.load(file)  # json.load JSON content ni Python dict ga convert chestundi
