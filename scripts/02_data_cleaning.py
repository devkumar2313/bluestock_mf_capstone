# %%
import pandas as pd
from pathlib import Path

raw_dir = Path('../data/raw')
target_dir = Path('../data/processed')

target_dir.mkdir(parents=True,exist_ok=True)

nav = pd.read_csv(raw_dir / '02_nav_history.csv')
nav['date'] = pd.to_datetime(nav['date'])
nav = nav.drop_duplicates()
nav = nav[nav['nav'] > 0]

nav_dt_fund = nav.set_index('date').groupby('amfi_code')
resample_d = nav_dt_fund.resample('D')
nav_filled = resample_d.ffill()
nav_clean = nav_filled.reset_index()

nav_clean.to_csv(target_dir / 'clean_nav_history.csv',index=False)
print("cleaned")
# %%
tx = pd.read_csv(raw_dir / '08_investor_transactions.csv')

tx['transaction_date'] = pd.to_datetime(tx['transaction_date'])
tx['transaction_type'] = tx['transaction_type'].str.title().str.strip()

tx = tx[tx['amount_inr'] > 0]

valid_kyc = ['Verified','Pending']
tx = tx[tx['kyc_status'].isin(valid_kyc)]

tx.to_csv(target_dir / 'clean_investor_transactions.csv',index=False)
print("cleaned")
tx.head()
# %%
perf = pd.read_csv(raw_dir / '07_scheme_performance.csv')

perf['expense_ratio_pct'] = perf['expense_ratio_pct'].clip(lower=0.1,upper=2.5)

num_cols = ['return_1yr_pct','return_3yr_pct','return_5yr_pct','sharpe_ratio']
for col in num_cols:
    perf[col] = pd.to_numeric(perf[col],errors='coerce')

perf.to_csv(target_dir / 'clean_scheme_performance.csv',index=False)
print('clean')
# %%
#cleaning other files

pass_through_files = [
    '01_fund_master.csv',
    '03_aum_by_fund_house.csv',
    '04_monthly_sip_inflows.csv',
    '05_category_inflows.csv',
    '06_industry_folio_count.csv',
    '09_portfolio_holdings.csv',
    '10_benchmark_indices.csv'
]

for file in pass_through_files:
    data = pd.read_csv(raw_dir / file)

    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
    if 'month' in data.columns:
        data['month'] = pd.to_datetime(data['month'])


    data.to_csv(target_dir/f"processed_{file}",index=False)
    print('migrate done')

print('all set')
# %%
