"""
Compare Engine

Loads Ground Truth and Workflow Results
and prepares a merged dataset for evaluation.
"""

from pathlib import Path
import pandas as pd


# -------------------------------------------------
# Project Paths
# -------------------------------------------------

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


# -------------------------------------------------
# Load Files
# -------------------------------------------------

def load_ground_truth():

    return pd.read_excel(GROUND_TRUTH_FILE)


def load_results():

    return pd.read_csv(RESULTS_FILE)


# -------------------------------------------------
# Merge Data
# -------------------------------------------------

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


# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__ == "__main__":

    merged = merge_results()

    print()

    print("=" * 60)

    print("Merged Dataset")

    print("=" * 60)

    print()

    print(merged.head())

    print()

    print(f"Rows : {len(merged)}")