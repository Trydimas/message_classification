from loguru import logger as _logger
from config import settings

import os

if not os.path.exists(settings.LOG_FOLDER):
    os.mkdir(settings.LOG_FOLDER)

_logger.add(
    os.path.join(settings.LOG_FOLDER, "app-{time:YYYY-MM-DD-HH}.log"),
    level=settings.LOG_LEVEL,
    rotation="10 MB",
    compression="zip",
)

logger = _logger.bind(name="app")
