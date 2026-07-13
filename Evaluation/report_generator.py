"""
Report Generator

Generates benchmark reports in:

1. TXT
2. Markdown
3. CSV

from one execution.
"""

from pathlib import Path
from datetime import datetime
import pandas as pd

from metrics import calculate_metrics


# ==========================================================
# Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

REPORT_DIR = BASE_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

TXT_FILE = REPORT_DIR / "benchmark_report.txt"
MD_FILE = REPORT_DIR / "benchmark_report.md"
CSV_FILE = REPORT_DIR / "benchmark_summary.csv"


# ==========================================================
# Generate Reports
# ==========================================================

def generate_report():

    metrics = calculate_metrics()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ======================================================
    # TXT REPORT
    # ======================================================

    txt = f"""
============================================================
AI INVOICE BENCHMARK REPORT
============================================================

Generated On : {timestamp}

============================================================
GENERAL
============================================================

Total Invoices              : {metrics['Total Invoices']}
Processed                   : {metrics['Processed']}
Missing                     : {metrics['Missing']}

============================================================
WORKFLOW STATUS
============================================================

SUCCESS                     : {metrics['SUCCESS']}
DUPLICATE_SKIPPED           : {metrics['DUPLICATE_SKIPPED']}
VALIDATION_FAILED           : {metrics['VALIDATION_FAILED']}
PAYLOAD_VALIDATION_FAILED   : {metrics['PAYLOAD_VALIDATION_FAILED']}
VENDOR_CREATION_FAILED      : {metrics['VENDOR_CREATION_FAILED']}

============================================================
PERFORMANCE KPIs
============================================================

Pipeline Completion Rate    : {metrics['Pipeline Completion Rate']} %

Business Success Rate       : {metrics['Business Success Rate']} %

Automation Reliability      : {metrics['Automation Reliability']} %

============================================================
END OF REPORT
============================================================
"""

    TXT_FILE.write_text(txt, encoding="utf-8")

    # ======================================================
    # MARKDOWN REPORT
    # ======================================================

    md = f"""# AI Invoice Benchmark Report

Generated: **{timestamp}**

---

## General

| Metric | Value |
|--------|------:|
| Total Invoices | {metrics['Total Invoices']} |
| Processed | {metrics['Processed']} |
| Missing | {metrics['Missing']} |

---

## Workflow Status

| Status | Count |
|--------|------:|
| SUCCESS | {metrics['SUCCESS']} |
| DUPLICATE_SKIPPED | {metrics['DUPLICATE_SKIPPED']} |
| VALIDATION_FAILED | {metrics['VALIDATION_FAILED']} |
| PAYLOAD_VALIDATION_FAILED | {metrics['PAYLOAD_VALIDATION_FAILED']} |
| VENDOR_CREATION_FAILED | {metrics['VENDOR_CREATION_FAILED']} |

---

## Performance

| KPI | Value |
|-----|------:|
| Pipeline Completion Rate | {metrics['Pipeline Completion Rate']} % |
| Business Success Rate | {metrics['Business Success Rate']} % |
| Automation Reliability | {metrics['Automation Reliability']} % |
"""

    MD_FILE.write_text(md, encoding="utf-8")

    # ======================================================
    # CSV REPORT
    # ======================================================

    summary = pd.DataFrame({

        "Metric": metrics.keys(),

        "Value": metrics.values()

    })

    summary.to_csv(

        CSV_FILE,

        index=False

    )

    return {

        "txt": TXT_FILE,

        "md": MD_FILE,

        "csv": CSV_FILE

    }


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    files = generate_report()

    print("\n" + "=" * 60)

    print("Reports Generated Successfully")

    print("=" * 60)

    print(f"\nTXT Report : {files['txt']}")
    print(f"Markdown  : {files['md']}")
    print(f"CSV       : {files['csv']}")

    print("\n" + "=" * 60)