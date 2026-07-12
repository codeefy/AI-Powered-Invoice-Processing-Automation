"""
Metrics Engine

Calculates benchmark metrics from the merged dataset.
"""

from compare_engine import merge_results


def calculate_metrics():

    df = merge_results()

    total_invoices = len(df)

    processed = df["final_status"].notna().sum()

    missing = total_invoices - processed

    completion_rate = (
        processed / total_invoices * 100
        if total_invoices else 0
    )

    status_counts = (
        df["final_status"]
        .fillna("NOT_PROCESSED")
        .value_counts()
    )

    metrics = {
        "Total Invoices": total_invoices,
        "Processed": processed,
        "Missing": missing,
        "Completion Rate": round(completion_rate, 2),

        "SUCCESS": int(status_counts.get("SUCCESS", 0)),
        "DUPLICATE_SKIPPED": int(status_counts.get("DUPLICATE_SKIPPED", 0)),
        "VALIDATION_FAILED": int(status_counts.get("VALIDATION_FAILED", 0)),
        "PAYLOAD_VALIDATION_FAILED": int(status_counts.get("PAYLOAD_VALIDATION_FAILED", 0)),
        "VENDOR_CREATION_FAILED": int(status_counts.get("VENDOR_CREATION_FAILED", 0))
    }

    if processed > 0:
        metrics["Workflow Success Rate"] = round(
            metrics["SUCCESS"] / processed * 100,
            2
        )
    else:
        metrics["Workflow Success Rate"] = 0

    return metrics


if __name__ == "__main__":

    metrics = calculate_metrics()

    print("\n" + "=" * 60)
    print("AI INVOICE BENCHMARK METRICS")
    print("=" * 60)

    print(f"Total Invoices          : {metrics['Total Invoices']}")
    print(f"Processed               : {metrics['Processed']}")
    print(f"Missing                 : {metrics['Missing']}")
    print(f"Completion Rate         : {metrics['Completion Rate']} %")

    print("\n" + "-" * 60)

    print(f"SUCCESS                 : {metrics['SUCCESS']}")
    print(f"DUPLICATE_SKIPPED       : {metrics['DUPLICATE_SKIPPED']}")
    print(f"VALIDATION_FAILED       : {metrics['VALIDATION_FAILED']}")
    print(f"PAYLOAD_VALIDATION_FAILED : {metrics['PAYLOAD_VALIDATION_FAILED']}")
    print(f"VENDOR_CREATION_FAILED  : {metrics['VENDOR_CREATION_FAILED']}")

    print("\n" + "-" * 60)

    print(f"Workflow Success Rate   : {metrics['Workflow Success Rate']} %")

    print("=" * 60)