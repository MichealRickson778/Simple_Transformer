from loguru import logger
import sys
from pathlib import Path
from datetime import datetime
import traceback

BASE_LOG_DIR = Path("logs")

def setup_logger(module_name: str):

    log_dir = BASE_LOG_DIR / module_name
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = log_dir / f"{timestamp}.log"

    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {extra[module]} | {message}"
    )

    logger.add(
        sys.stderr,
        level="ERROR"
    )

    logger.add(
        log_file,
        level="DEBUG",
        backtrace=True,
        diagnose=True
    )

    log = logger.bind(module=module_name)

    # 🔥 GLOBAL UNCAUGHT EXCEPTION HANDLER
    def handle_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        log.error("Uncaught exception occurred")
        log.opt(exception=(exc_type, exc_value, exc_traceback)).error("Crash traceback")

    sys.excepthook = handle_exception

    return log
