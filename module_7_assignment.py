import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

PYTHON_DIR = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
JSON_PATH = PYTHON_DIR / "sample-data.json"
CHARTS_DIR = PYTHON_DIR / "module_7_charts"

ORDER_COL = "Order Value (AED)"
SAT_COL = "Satisfaction (1–5)"
PAGE_COL = "Page Version"
PURCHASED_COL = "Purchased"
ALPHA = 0.05


def _find_excel_file() -> Path:
    for path in (PYTHON_DIR / "sample-data.xlsx", PYTHON_DIR.parent / "sample-data.xlsx"):
        if path.is_file():
            return path
    raise FileNotFoundError(
        "Could not find sample-data.xlsx. Please put the file in desired location and run the script again."
    )


def _sheet_to_records(df: pd.DataFrame) -> list:
    return json.loads(df.to_json(orient="records", date_format="iso"))  # pyright: ignore[reportArgumentType]


def excel_to_json(excel_path: Path | str, json_path: Path | str) -> None:
    excel_path = Path(excel_path)
    json_path = Path(json_path)

    if json_path.is_file():
        print(f"{json_path.name} already exists, skipping conversion.")
        return

    try:
        xl = pd.ExcelFile(excel_path)
    except ImportError as e:
        raise ImportError(
            "Reading .xlsx needs openpyxl. Run: pip install openpyxl"
        ) from e

    if len(xl.sheet_names) == 1:
        df = pd.read_excel(excel_path)
        payload = _sheet_to_records(df)
    else:
        payload = {}
        for sheet in xl.sheet_names:
            df = pd.read_excel(excel_path, sheet_name=sheet)
            payload[sheet] = _sheet_to_records(df)

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(xl.sheet_names)} sheet(s) to {json_path}")


def load_json_data(json_path: Path | str) -> list | dict:
    json_path = Path(json_path)
    with json_path.open(encoding="utf-8") as f:
        return json.load(f)


def load_dataframe(json_path: Path | str = JSON_PATH) -> pd.DataFrame:
    sample_data = load_json_data(json_path)
    if not isinstance(sample_data, list):
        raise ValueError("Expected a single-sheet JSON file (list of records).")
    return pd.DataFrame(sample_data)


def task_1(customer_df: pd.DataFrame) -> None:
    """Task 1: Explore the dataset."""
    print("--- Task 1: Explore dataset ---")
    print(f"Records: {len(customer_df)}")
    print(f"Columns: {list(customer_df.columns)}")
    print("\nFirst 5 rows:")
    print(customer_df.head())
    print("\nData types:")
    print(customer_df.dtypes)
    print("\nNumeric summary:")
    print(customer_df.describe())


def task_2(customer_df: pd.DataFrame) -> None:
    """Task 2: Data quality, category frequencies, and key numeric stats."""
    print("--- Task 2: Quality checks & descriptive statistics ---")

    print("\nMissing values per column:")
    print(customer_df.isnull().sum())

    duplicate_ids = customer_df["Customer ID"].duplicated().sum()
    print(f"\nDuplicate Customer IDs: {duplicate_ids}")

    categorical_cols = ["Region", "Marketing Channel", PAGE_COL, PURCHASED_COL]
    for col in categorical_cols:
        print(f"\n{col} — value counts:")
        print(customer_df[col].value_counts())

    print(f"\n{ORDER_COL}:")
    print(f"  Mean:   {customer_df[ORDER_COL].mean():.2f}")
    print(f"  Median: {customer_df[ORDER_COL].median():.2f}")
    print(f"  Std:    {customer_df[ORDER_COL].std():.2f}")

    print(f"\n{SAT_COL}:")
    print(f"  Mean:   {customer_df[SAT_COL].mean():.2f}")
    print(f"  Median: {customer_df[SAT_COL].median():.2f}")
    print(f"  Std:    {customer_df[SAT_COL].std():.2f}")

    purchase_rate = (customer_df[PURCHASED_COL] == "Yes").mean() * 100
    print(f"\nOverall purchase rate: {purchase_rate:.1f}%")


def _group_performance_summary(customer_df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    summary = customer_df.groupby(group_col, sort=True).agg(
        customers=("Customer ID", "count"),
        avg_order_aed=(ORDER_COL, "mean"),
        avg_satisfaction=(SAT_COL, "mean"),
        purchase_rate_pct=(PURCHASED_COL, lambda s: (s == "Yes").mean() * 100),
    )
    return summary.round(2)  # pyright: ignore[reportReturnType]


def task_3(customer_df: pd.DataFrame) -> None:
    """Task 3: Compare metrics by Region, Marketing Channel, and Page Version."""
    print("--- Task 3: Performance by group ---")

    group_columns = ["Region", "Marketing Channel", PAGE_COL]
    with pd.option_context("display.max_columns", None, "display.width", 120):
        for col in group_columns:
            print(f"\nBy {col}:")
            print(_group_performance_summary(customer_df, col))


def task_4(customer_df: pd.DataFrame) -> None:
    """Task 4: Visualize order value distribution and group comparisons."""
    print("--- Task 4: Visualizations ---")
    CHARTS_DIR.mkdir(exist_ok=True)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].hist(customer_df[ORDER_COL], bins=10, color="skyblue", edgecolor="black")
    axes[0].set_title("Order Value Distribution")
    axes[0].set_xlabel(ORDER_COL)
    axes[0].set_ylabel("Frequency")

    region_means = customer_df.groupby("Region")[ORDER_COL].mean().sort_values()  # pyright: ignore[reportCallIssue, reportAttributeAccessIssue]
    region_means.plot(kind="bar", ax=axes[1], color="coral", edgecolor="black")
    axes[1].set_title("Average Order Value by Region")
    axes[1].set_xlabel("Region")
    axes[1].set_ylabel("Average (AED)")
    axes[1].tick_params(axis="x", rotation=45)

    chart_path = CHARTS_DIR / "task_4_order_value_charts.png"
    fig.tight_layout()
    fig.savefig(chart_path, dpi=120)
    plt.close(fig)

    page_rates = (
        customer_df.groupby(PAGE_COL)[PURCHASED_COL]
        .apply(lambda s: (s == "Yes").mean() * 100)
        .sort_index()
    )
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    page_rates.plot(kind="bar", ax=ax2, color=["#4c78a8", "#f58518"], edgecolor="black")
    ax2.set_title("Purchase Rate by Page Version (A/B)")
    ax2.set_xlabel(PAGE_COL)
    ax2.set_ylabel("Purchase rate (%)")
    ax2.tick_params(axis="x", rotation=0)

    chart_path_2 = CHARTS_DIR / "task_4_ab_purchase_rate.png"
    fig2.tight_layout()
    fig2.savefig(chart_path_2, dpi=120)
    plt.close(fig2)

    print(f"Saved: {chart_path}")
    print(f"Saved: {chart_path_2}")


def task_5(customer_df: pd.DataFrame) -> None:
    """Task 5: Correlation between satisfaction and order value."""
    print("--- Task 5: Correlation analysis ---")

    correlation = customer_df[SAT_COL].corr(customer_df[ORDER_COL])  # pyright: ignore[reportArgumentType]
    r, p_value = stats.pearsonr(customer_df[SAT_COL], customer_df[ORDER_COL])

    print(f"Pearson correlation (r): {correlation:.3f}")
    print(f"Scipy pearsonr — r: {r:.3f}, p-value: {p_value:.4f}")

    if p_value < ALPHA:  # pyright: ignore[reportOperatorIssue]
        print(f"Result: Significant at α={ALPHA} (higher satisfaction tends to link with order value).")
    else:
        print(f"Result: Not significant at α={ALPHA} (weak evidence of linear relationship).")


def task_6(customer_df: pd.DataFrame) -> None:
    """Task 6: A/B tests — Page A vs Page B (order value t-test, purchase chi-square)."""
    print("--- Task 6: Hypothesis tests (Page A vs Page B) ---")

    page_a = customer_df[customer_df[PAGE_COL] == "A"]
    page_b = customer_df[customer_df[PAGE_COL] == "B"]

    t_stat, t_p = stats.ttest_ind(
        page_a[ORDER_COL],
        page_b[ORDER_COL],
        equal_var=False,
    )
    print("\nWelch t-test: mean order value (A vs B)")
    print(f"  t-statistic: {t_stat:.3f}")
    print(f"  p-value:     {t_p:.4f}")
    print(
        f"  Conclusion:  {'Significant difference' if t_p < ALPHA else 'No significant difference'} "  # pyright: ignore[reportOperatorIssue]
        f"at α={ALPHA}"
    )

    t_stat_sat, t_p_sat = stats.ttest_ind(
        page_a[SAT_COL],
        page_b[SAT_COL],
        equal_var=False,
    )
    print("\nWelch t-test: mean satisfaction (A vs B)")
    print(f"  t-statistic: {t_stat_sat:.3f}")
    print(f"  p-value:     {t_p_sat:.4f}")
    print(
        f"  Conclusion:  {'Significant difference' if t_p_sat < ALPHA else 'No significant difference'} "  # pyright: ignore[reportOperatorIssue]
        f"at α={ALPHA}"
    )

    contingency = pd.crosstab(customer_df[PAGE_COL], customer_df[PURCHASED_COL])
    chi2, chi_p, _, _ = stats.chi2_contingency(contingency)
    print("\nChi-square test: Page Version vs Purchased")
    print(contingency)
    print(f"  chi²:      {chi2:.3f}")
    print(f"  p-value:   {chi_p:.4f}")
    print(
        f"  Conclusion: {'Association detected' if chi_p < ALPHA else 'No significant association'} "  # pyright: ignore[reportOperatorIssue]
        f"at α={ALPHA}"
    )


def task_7(customer_df: pd.DataFrame) -> None:
    """Task 7: Business summary and recommendations from the analysis."""
    print("--- Task 7: Summary & recommendations ---")

    by_region = _group_performance_summary(customer_df, "Region")
    best_region = by_region["avg_order_aed"].idxmax()
    best_region_rate = by_region.loc[best_region, "purchase_rate_pct"]

    by_channel = _group_performance_summary(customer_df, "Marketing Channel")
    best_channel = by_channel["purchase_rate_pct"].idxmax()

    by_page = _group_performance_summary(customer_df, PAGE_COL)
    better_page = by_page["purchase_rate_pct"].idxmax()
    page_a_rate = by_page.loc["A", "purchase_rate_pct"]
    page_b_rate = by_page.loc["B", "purchase_rate_pct"]

    overall_purchase = (customer_df[PURCHASED_COL] == "Yes").mean() * 100

    print(f"\n• Overall purchase rate: {overall_purchase:.1f}% across {len(customer_df)} customers.")
    print(
        f"• Highest average order value by region: {best_region} "
        f"(purchase rate {best_region_rate:.1f}%)."
    )
    print(f"• Best purchase rate by marketing channel: {best_channel}.")
    print(
        f"• A/B pages: B has a higher observed purchase rate ({page_b_rate:.1f}% vs "
        f"{page_a_rate:.1f}% for A). Confirm with Task 6 p-values before rolling out B."
    )
    print(
        "\nRecommendation: Prioritize high-performing regions/channels, keep monitoring "
        "Page B if chi-square/t-tests support it, and track satisfaction alongside order value."
    )


if __name__ == "__main__":
    excel_to_json(_find_excel_file(), JSON_PATH)
    customer_df = load_dataframe(JSON_PATH)

    task_1(customer_df)
    task_2(customer_df)
    task_3(customer_df)
    task_4(customer_df)
    task_5(customer_df)
    task_6(customer_df)
    task_7(customer_df)
