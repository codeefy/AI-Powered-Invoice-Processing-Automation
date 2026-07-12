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
Benchmark Report
"""

from report_generator import generate_report
from metrics import calculate_metrics


def run_evaluation():

    print("\n" + "=" * 60)
    print("AI Invoice Benchmark Evaluation")
    print("=" * 60)

    print("\nCalculating benchmark metrics...")

    metrics = calculate_metrics()

    print("Generating benchmark report...")

    report_path = generate_report()

    print("\n" + "=" * 60)
    print("Evaluation Completed Successfully")
    print("=" * 60)

    print(f"\nReport Saved To:\n{report_path}")

    print("\nSUMMARY\n")

    print(f"Total Invoices        : {metrics['Total Invoices']}")
    print(f"Processed             : {metrics['Processed']}")
    print(f"Missing               : {metrics['Missing']}")
    print(f"Completion Rate       : {metrics['Completion Rate']} %")

    print()

    print(f"SUCCESS               : {metrics['SUCCESS']}")
    print(f"DUPLICATE_SKIPPED     : {metrics['DUPLICATE_SKIPPED']}")
    print(f"VALIDATION_FAILED     : {metrics['VALIDATION_FAILED']}")
    print(f"PAYLOAD_VALIDATION_FAILED : {metrics['PAYLOAD_VALIDATION_FAILED']}")
    print(f"VENDOR_CREATION_FAILED: {metrics['VENDOR_CREATION_FAILED']}")

    print()

    print(f"Workflow Success Rate : {metrics['Workflow Success Rate']} %")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_evaluation()