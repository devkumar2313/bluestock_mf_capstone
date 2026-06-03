# Bluestock Mutual Fund Analytics: Data Dictionary

## 1. dim_fund (Dimension Table)
* **amfi_code (PK):** Unique identifier assigned by AMFI to each mutual fund scheme. (Integer)
* **fund_house:** Name of the Asset Management Company (AMC). (String)
* **scheme_name:** Official name of the mutual fund. (String)
* **category:** Broad classification (Equity, Debt, Hybrid). (String)
* **expense_ratio_pct:** Annual fee charged by the AMC, capped between 0.1% and 2.5%. (Float)
* **risk_category:** SEBI defined risk level (Low to Very High). (String)

## 2. fact_nav (Fact Table)
* **amfi_code (FK):** Foreign key linking to dim_fund. (Integer)
* **date:** Trading date. Missing weekends/holidays are forward-filled (ffill). (Date)
* **nav:** Net Asset Value in INR. (Float)

## 3. fact_transactions (Fact Table)
* **investor_id:** Unique ID for the retail investor. (String)
* **transaction_date:** Date the transaction was executed. (Date)
* **transaction_type:** SIP, lumpsum, or Redemption. (String)
* **amount_inr:** Transaction value in Indian Rupees. (Integer)
* **city_tier:** T30 (Top 30 cities) or B30 (Beyond 30 cities). (String)

## 4. fact_performance (Fact Table)
* **return_3yr_pct:** 3-year Compounded Annual Growth Rate (CAGR). (Float)
* **alpha:** Excess return of the fund relative to the benchmark index. (Float)
* **sharpe_ratio:** Risk-adjusted return metric. Higher is better. (Float)
* **max_drawdown_pct:** The maximum observed loss from a peak to a trough. (Float)