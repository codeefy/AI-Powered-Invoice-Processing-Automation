"""
Compare Engine

Loads Ground Truth and Workflow Results,
cleans both datasets,
keeps only the latest workflow result,
and prepares a merged dataset for evaluation.
"""

from pathlib import Path
import pandas as pd


# =================================================
# Project Paths
# =================================================

BASE_DIR = Path(__file__).resolve().parent.parent

GROUND_TRUTH_FILE = (
    BASE_DIR
    / "Invoice_100_Test"
    / "Ground_Truth"
    / "ground_truth.xlsx"
)

RESULTS_FILE = (
    BASE_DIR
    / "Invoice_100_Test"
    / "Results"
    / "results.csv"
)


# =================================================
# Load Ground Truth
# =================================================

def load_ground_truth():

    ground_truth = pd.read_excel(GROUND_TRUTH_FILE)

    # Remove completely empty rows
    ground_truth = ground_truth.dropna(how="all")

    # Remove rows without File_Name
    ground_truth = ground_truth.dropna(subset=["File_Name"])

    # Remove extra spaces
    ground_truth["File_Name"] = (
        ground_truth["File_Name"]
        .astype(str)
        .str.strip()
    )

    return ground_truth


# =================================================
# Load Workflow Results
# =================================================

def load_results():

    results = pd.read_csv(RESULTS_FILE)

    # Remove rows without filename
    results = results.dropna(subset=["file_name"])

    results["file_name"] = (
        results["file_name"]
        .astype(str)
        .str.strip()
    )

    # Sort by processed time
    results = results.sort_values("processed_at")

    # Keep latest result only
    results = results.drop_duplicates(
        subset="file_name",
        keep="last"
    )

    return results


# =================================================
# Merge
# =================================================

def merge_results():

    ground_truth = load_ground_truth()

    results = load_results()

    merged = ground_truth.merge(

        results,

        left_on="File_Name",

        right_on="file_name",

        how="left",

        suffixes=("_expected", "_actual")

    )

    return merged


# =================================================
# Debug
# =================================================

if __name__ == "__main__":

    ground_truth = load_ground_truth()

    results = load_results()

    merged = merge_results()

    print("\n" + "=" * 60)
    print("GROUND TRUTH")
    print("=" * 60)

    print(f"Rows              : {len(ground_truth)}")
    print(f"Unique File Names : {ground_truth['File_Name'].nunique()}")

    print("\n" + "=" * 60)
    print("WORKFLOW RESULTS")
    print("=" * 60)

    print(f"Rows              : {len(results)}")
    print(f"Unique File Names : {results['file_name'].nunique()}")

    print("\n" + "=" * 60)
    print("MERGED DATASET")
    print("=" * 60)

    print(f"Rows              : {len(merged)}")

    matched = merged["file_name"].notna().sum()

    unmatched = merged["file_name"].isna().sum()

    print(f"Matched Invoices  : {matched}")

    print(f"Missing Results   : {unmatched}")

    print("\nPreview:\n")

    print(
        merged[
            [
                "Invoice_ID",
                "File_Name",
                "Vendor_Name",
                "vendor_name",
                "Expected_Result",
                "final_status"
            ]
        ].head(10)
    )