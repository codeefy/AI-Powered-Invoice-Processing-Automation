"""
Report Generator

Generates a benchmark report from the metrics engine.
"""

from pathlib import Path
from datetime import datetime

from metrics import calculate_metrics


# ==========================================================
# Report Directory
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)


# ==========================================================
# Report File
# ==========================================================

REPORT_FILE = REPORT_DIR / "benchmark_report.txt"


# ==========================================================
# Generate Report
# ==========================================================

def generate_report():

    metrics = calculate_metrics()

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    report = f"""
============================================================
AI INVOICE BENCHMARK REPORT
============================================================

Generated On : {timestamp}

------------------------------------------------------------
GENERAL
------------------------------------------------------------

Total Invoices            : {metrics['Total Invoices']}

Processed                 : {metrics['Processed']}

Missing                   : {metrics['Missing']}

Completion Rate           : {metrics['Completion Rate']} %

------------------------------------------------------------
WORKFLOW STATUS
------------------------------------------------------------

SUCCESS                   : {metrics['SUCCESS']}

DUPLICATE_SKIPPED         : {metrics['DUPLICATE_SKIPPED']}

VALIDATION_FAILED         : {metrics['VALIDATION_FAILED']}

PAYLOAD_VALIDATION_FAILED : {metrics['PAYLOAD_VALIDATION_FAILED']}

VENDOR_CREATION_FAILED    : {metrics['VENDOR_CREATION_FAILED']}

------------------------------------------------------------
PERFORMANCE
------------------------------------------------------------

Workflow Success Rate     : {metrics['Workflow Success Rate']} %

============================================================
END OF REPORT
============================================================
"""

    with open(
        REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    return REPORT_FILE


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    report_path = generate_report()

    print("\n" + "=" * 60)

    print("Benchmark report generated successfully.")

    print(f"\nSaved to:\n{report_path}")

    print("=" * 60)