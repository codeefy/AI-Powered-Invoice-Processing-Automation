"""
Evaluation Pipeline

Runs the complete benchmark evaluation.

Workflow

Ground Truth
        │
Results.csv
        │
Compare Engine
        │
Metrics
        │
Report Generator
"""

from report_generator import generate_report
from metrics import calculate_metrics


# ==========================================================
# Evaluation Pipeline
# ==========================================================

def run_evaluation():

    print("\n" + "=" * 60)
    print("AI INVOICE BENCHMARK EVALUATION")
    print("=" * 60)

    print("\nLoading benchmark data...")
    metrics = calculate_metrics()

    print("Generating benchmark reports...")
    reports = generate_report()

    print("\n" + "=" * 60)
    print("EVALUATION COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print("\nGenerated Reports:\n")

    print(f"TXT Report       : {reports['txt']}")
    print(f"Markdown Report : {reports['md']}")
    print(f"CSV Summary     : {reports['csv']}")

    print("\n" + "=" * 60)
    print("BENCHMARK SUMMARY")
    print("=" * 60)

    # =====================================================
    # General
    # =====================================================

    print(f"Total Invoices          : {metrics['Total Invoices']}")
    print(f"Processed               : {metrics['Processed']}")
    print(f"Missing                 : {metrics['Missing']}")

    print()

    # =====================================================
    # Workflow Status
    # =====================================================

    print(f"SUCCESS                 : {metrics['SUCCESS']}")
    print(f"DUPLICATE_SKIPPED       : {metrics['DUPLICATE_SKIPPED']}")
    print(f"VALIDATION_FAILED       : {metrics['VALIDATION_FAILED']}")
    print(f"PAYLOAD_VALIDATION_FAILED : {metrics['PAYLOAD_VALIDATION_FAILED']}")
    print(f"VENDOR_CREATION_FAILED  : {metrics['VENDOR_CREATION_FAILED']}")

    print()

    # =====================================================
    # KPIs
    # =====================================================

    print(f"Pipeline Completion     : {metrics['Pipeline Completion Rate']} %")
    print(f"Business Success        : {metrics['Business Success Rate']} %")
    print(f"Automation Reliability  : {metrics['Automation Reliability']} %")

    print("\n" + "=" * 60)
    print("Evaluation Finished")
    print("=" * 60)


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    run_evaluation()

    