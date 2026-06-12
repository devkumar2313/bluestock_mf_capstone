# %%
import pandas as pd
from pathlib import Path

data_path = Path('../data/raw')

data_collection = {}


for file in data_path.glob('*.csv'):
    file_name = file.stem
    data = pd.read_csv(file)
    data_collection[file_name] = data

    print(f"Overview of {file_name}")
    print(f"Shape: {data.shape}")
    print(f"info: {data.info()}")
    print(f"missing_val : {data.isna().sum()[data.isna().sum()> 0]}")


# %%
# analysing the fund_master
fund_master = data_collection['01_fund_master']

print(f"Total Unique Schemes: {fund_master['amfi_code'].nunique()}\n")

print("Unique Fund Houses:")
print(fund_master['fund_house'].unique())

print("\nCategories:")
print(fund_master['category'].unique())
print(fund_master['category'].value_counts())

print("\nSub-Categories:")
print(fund_master['sub_category'].unique())

print("\nRisk Grades:")
print(fund_master['risk_category'].unique())

print(fund_master['expense_ratio_pct'].describe())

print(pd.crosstab(fund_master['fund_house'],fund_master['risk_category']))

# %%

nav_history = data_collection['02_nav_history']


master_codes = set(fund_master['amfi_code'].unique())
nav_codes = set(nav_history['amfi_code'].unique())


missing_codes = master_codes - nav_codes

if len(missing_codes) == 0:
    print("all fund master amfi codes present")
else:
    print(f"missing amfi in nav: {missing_codes}")
# %% [markdown]
# ## Day 1: Initial Data Quality Summary
# 
# Based on the preliminary data ingestion and profiling, here is the state of the raw datasets:
# 
# **1. Overall Data Health & Completeness**
# * The datasets are exceptionally clean. Out of 10 files, only `04_monthly_sip_inflows.csv` contains missing values (12 nulls in `yoy_growth_pct`). This is mathematically expected, as the first 12 months of data cannot have a Year-over-Year comparison.
# * All other tables show zero missing values in this initial read.
# 
# **2. Relational Integrity**
# * **Passed:** A strict set-subtraction confirms that all 40 unique `amfi_code` values in the `fund_master` table perfectly map to the historical records in `nav_history`. No orphan records or missing NAV sets.
# 
# **3. Business Logic Validation**
# * The `fund_master` dataset correctly contains exactly 40 schemes across 10 unique AMCs.
# * Expense ratios range from 0.55% to 1.64% (Mean: 1.23%), which strictly aligns with real-world SEBI limits for mutual funds.
# * The dataset is heavily skewed towards Equity (34 schemes) versus Debt (6 schemes).
# 
# **4. Action Items for Day 2 (Data Cleaning)**
# * **Type Conversion:** Across almost all datasets (especially `nav_history`, `investor_transactions`, and `benchmark_indices`), the date columns have been imported as standard `object` (string) types. These must be explicitly cast to `datetime` objects for time-series analysis.
# * **Holiday Forward-Filling:** While `nav_history` has no *nulls*, we must verify if weekends/holidays are missing rows entirely and apply `ffill()` per the project rubric requirements.