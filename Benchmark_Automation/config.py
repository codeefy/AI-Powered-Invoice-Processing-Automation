"""
Configuration for Invoice Benchmark Runner
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# -------------------------------------------------
# Load environment variables
# -------------------------------------------------

load_dotenv()

# -------------------------------------------------
# Gmail Configuration
# -------------------------------------------------

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# -------------------------------------------------
# Email Configuration
# -------------------------------------------------

EMAIL_SUBJECT = "Invoice"

EMAIL_BODY = """
Dear Team,

Please find the attached invoice for processing.

This email was generated automatically by the Invoice Benchmark Runner.

Regards,
Invoice Automation Benchmark
"""

# -------------------------------------------------
# Benchmark Configuration
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FOLDER = BASE_DIR / "Invoice_100_Test" / "Pilot_Test"

WAIT_BETWEEN_EMAILS = 45      # Seconds
MAX_RETRIES = 3

# -------------------------------------------------
# Logging
# -------------------------------------------------

LOG_DIR = BASE_DIR / "Benchmark_Automation" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "benchmark.log"

# -------------------------------------------------
# Supported File Types
# -------------------------------------------------

SUPPORTED_EXTENSIONS = [".pdf"]