"""
Benchmark Runner - Milestone 2
PDF Discovery + Production Logging
"""

from pathlib import Path
from datetime import datetime
import logging

from config import (
    INPUT_FOLDER,
    SUPPORTED_EXTENSIONS,
    LOG_FILE
)


# -------------------------------------------------
# Configure Logger
# -------------------------------------------------

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# -------------------------------------------------
# Discover PDF Files
# -------------------------------------------------

def discover_pdfs():
    """
    Return a sorted list of PDF files.
    """

    files = []

    for file in Path(INPUT_FOLDER).iterdir():

        if (
            file.is_file()
            and file.suffix.lower() in SUPPORTED_EXTENSIONS
        ):
            files.append(file)

    return sorted(files)


# -------------------------------------------------
# Log Benchmark Information
# -------------------------------------------------

def log_benchmark_start(pdf_list):

    logger.info("=" * 60)
    logger.info("Invoice Benchmark Started")
    logger.info("=" * 60)

    logger.info(f"Start Time : {datetime.now()}")

    logger.info(f"Input Folder : {INPUT_FOLDER}")

    logger.info(f"Total PDFs : {len(pdf_list)}")

    logger.info("")

    for i, pdf in enumerate(pdf_list, start=1):
        logger.info(f"{i:03d}. {pdf.name}")

    logger.info("=" * 60)


# -------------------------------------------------
# Main
# -------------------------------------------------

def main():

    pdfs = discover_pdfs()

    print("=" * 60)
    print("Invoice Benchmark Runner")
    print("=" * 60)

    print(f"\nFound {len(pdfs)} PDF files:\n")

    for i, pdf in enumerate(pdfs, start=1):
        print(f"{i:03d}. {pdf.name}")

    log_benchmark_start(pdfs)

    print("\nBenchmark log created successfully.")


if __name__ == "__main__":
    main()