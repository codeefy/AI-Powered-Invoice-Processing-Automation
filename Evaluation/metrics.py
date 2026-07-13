"""
Metrics Engine

Calculates benchmark metrics from the merged dataset.
"""

from compare_engine import merge_results


def calculate_metrics():

    df = merge_results()

    # -------------------------------------------------
    # Basic Counts
    # -------------------------------------------------

    total_invoices = len(df)

    processed = df["final_status"].notna().sum()

    missing = total_invoices - processed

    # -------------------------------------------------
    # Status Counts
    # -------------------------------------------------

    status_counts = (
        df["final_status"]
        .fillna("NOT_PROCESSED")
        .value_counts()
    )

    success = int(status_counts.get("SUCCESS", 0))
    duplicate = int(status_counts.get("DUPLICATE_SKIPPED", 0))
    validation = int(status_counts.get("VALIDATION_FAILED", 0))
    payload = int(status_counts.get("PAYLOAD_VALIDATION_FAILED", 0))
    vendor = int(status_counts.get("VENDOR_CREATION_FAILED", 0))

    # -------------------------------------------------
    # KPI Calculations
    # -------------------------------------------------

    pipeline_completion = (
        processed / total_invoices * 100
        if total_invoices else 0
    )

    business_success = (
        success / processed * 100
        if processed else 0
    )

    handled = (
        success +
        duplicate +
        validation +
        payload +
        vendor
    )

    automation_reliability = (
        handled / total_invoices * 100
        if total_invoices else 0
    )

    # -------------------------------------------------
    # Metrics Dictionary
    # -------------------------------------------------

    metrics = {

        # General

        "Total Invoices": total_invoices,
        "Processed": processed,
        "Missing": missing,

        # Status Counts

        "SUCCESS": success,
        "DUPLICATE_SKIPPED": duplicate,
        "VALIDATION_FAILED": validation,
        "PAYLOAD_VALIDATION_FAILED": payload,
        "VENDOR_CREATION_FAILED": vendor,

        # KPIs

        "Pipeline Completion Rate":
            round(pipeline_completion, 2),

        "Business Success Rate":
            round(business_success, 2),

        "Automation Reliability":
            round(automation_reliability, 2)
    }

    return metrics


# =====================================================
# Test
# =====================================================

if __name__ == "__main__":

    metrics = calculate_metrics()

    print("\n" + "=" * 60)
    print("AI INVOICE BENCHMARK METRICS")
    print("=" * 60)

    print(f"Total Invoices           : {metrics['Total Invoices']}")
    print(f"Processed                : {metrics['Processed']}")
    print(f"Missing                  : {metrics['Missing']}")

    print("\n" + "-" * 60)

    print(f"SUCCESS                  : {metrics['SUCCESS']}")
    print(f"DUPLICATE_SKIPPED        : {metrics['DUPLICATE_SKIPPED']}")
    print(f"VALIDATION_FAILED        : {metrics['VALIDATION_FAILED']}")
    print(f"PAYLOAD_VALIDATION_FAILED: {metrics['PAYLOAD_VALIDATION_FAILED']}")
    print(f"VENDOR_CREATION_FAILED   : {metrics['VENDOR_CREATION_FAILED']}")

    print("\n" + "-" * 60)

    print(f"Pipeline Completion      : {metrics['Pipeline Completion Rate']} %")
    print(f"Business Success         : {metrics['Business Success Rate']} %")
    print(f"Automation Reliability   : {metrics['Automation Reliability']} %")

    print("=" * 60)