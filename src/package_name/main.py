"""
Main entry point of the Python package
"""

import logging
import os

# ──────────────────────────────
# Configuration
# ──────────────────────────────
log_path = os.getenv("LOG_FILE", "app.log")

# ──────────────────────────────
# Configuration
# ──────────────────────────────
file_handler = logging.FileHandler(log_path, encoding="utf-8")
stream_handler = logging.StreamHandler()
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)-8s | %(message)s",
    handlers=[file_handler, stream_handler],
)


def main():
    logger = logging.getLogger(__name__)
    logger.debug("Success")


if __name__ == "__main__":
    main()
