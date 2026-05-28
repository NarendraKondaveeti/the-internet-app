"""Color logging utility for readable terminal execution."""

from __future__ import annotations  # annotations ni lazy ga process cheyyadaniki Python future feature

import logging  # Python logging module; execution information print cheyyadaniki use chestamu
from pathlib import Path  # Path object; logs folder create cheyyadaniki use chestamu

import colorlog  # third party package; terminal colors readable ga chupinchadaniki use chestamu


PROJECT_ROOT = Path(__file__).resolve().parents[1]  # project root path calculate chestundi
LOG_DIR = PROJECT_ROOT / "logs"  # logs folder path store chestundi
LOG_DIR.mkdir(exist_ok=True)  # folder lekapothe create chestundi; exist ayithe ignore chestundi


def get_logger(name: str = "automation") -> logging.Logger:  # reusable logger factory method
    logger = logging.getLogger(name)  # Python logging lo named logger create/reuse chestundi
    if logger.handlers:  # handlers already unte duplicate logs avoid chestamu
        return logger  # existing logger ni return chestamu

    logger.setLevel(logging.INFO)  # INFO level and above messages capture chestamu

    formatter = colorlog.ColoredFormatter(  # color formatter terminal output colorful ga chestundi
        "%(log_color)s%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",  # time readable ga kanipinchadaniki hour minute second format
        log_colors={  # each level ki color map define chestamu
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    console_handler = logging.StreamHandler()  # terminal lo logs print cheyyadaniki handler
    console_handler.setFormatter(formatter)  # handler ki color formatter attach chestamu

    file_handler = logging.FileHandler(LOG_DIR / "execution.log", encoding="utf-8")  # file lo logs save cheyyadaniki handler
    file_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s"))  # file log plain format

    logger.addHandler(console_handler)  # console handler logger ki add chestamu
    logger.addHandler(file_handler)  # file handler logger ki add chestamu
    return logger  # configured logger return chestamu
