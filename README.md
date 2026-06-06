# Indian Mutual Fund Analytics & Quantitative Scorecard

## 📌 Project Overview
This project is an end-to-end data engineering and quantitative analytics pipeline for the Indian Mutual Fund industry. It processes raw transactional and NAV data across 40 mutual fund schemes (2022–2026) to generate interactive exploratory data visualizations and compute advanced financial performance metrics.

The final deliverable is a **Composite Fund Scorecard (0-100)** that ranks funds based on a weighted matrix of CAGR, Sharpe Ratio, Alpha, Expense Ratios, and Maximum Drawdowns.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Database:** SQLite3
* **Data Processing:** Pandas, NumPy
* **Quantitative Analysis:** SciPy (`scipy.stats`)
* **Data Visualization:** Matplotlib, Seaborn, Plotly

## 📂 Project Architecture

### Phase 1: Data Engineering & Ingestion (Days 1 & 2)
* Designed a relational dimensional model (Fact and Dimension tables).
* Cleaned and normalized raw CSV datasets (handling missing values, standardizing dates, and mapping categorical data).
* Built an automated Python ingestion script (`load_db.py`) using SQLAlchemy to populate the SQLite database (`blue_mf.db`).

### Phase 2: Exploratory Data Analysis (Day 3)
* **AUM & Market Share:** Grouped bar charting of fund house dominance (e.g., SBI's ₹12.5L Cr AUM).
* **Investor Demographics:** Visualized age brackets, gender splits, and geographic (T30 vs B30) distribution.
* **Trend Analysis:** Mapped the exponential industry folio growth and plotted interactive time-series for monthly SIP inflows (highlighting the ₹31,002 Cr all-time high).
* **Correlation:** Generated a pairwise NAV return correlation matrix (Heatmap) to identify portfolio overlap risk.

### Phase 3: Quantitative Performance Analytics (Day 4)
* **Return Metrics:** Calculated Daily Returns and 1-yr, 3-yr, and 5-yr Compound Annual Growth Rates (CAGR).
* **Risk Metrics:** Computed standard deviation, Sharpe Ratio (using a 6.5% risk-free proxy), and Sortino Ratio.
* **Alpha & Beta:** Ran OLS regression on daily fund returns against Nifty market benchmarks to extract $\alpha$ and $\beta$ coefficients.
* **Drawdown Analysis:** Identified the Maximum Drawdown (Max DD) and worst-case drop scenarios for every fund.

## 📊 The Composite Fund Scorecard
To objectively rank the 40 mutual fund schemes, a standardized 0-100 scoring system was engineered using the following percentile weightings:
* **30%** - 3-Year CAGR Rank
* **25%** - Sharpe Ratio Rank
* **20%** - Alpha Rank
* **15%** - Expense Ratio Rank (Inverse)
* **10%** - Maximum Drawdown Rank (Inverse)

## 🚀 How to Run the Project
1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly scipy sqlalchemy
   ```
3. Run the database ingestion script from the root directory:
   ```bash
   python load_db.py
   ```
4. Open the Jupyter Notebooks in the /notebooks directory sequentially (01_... to 04_...) to reproduce the data cleaning, EDA, and quantitative analytics.

## 📁 Repository Structure
```text
├── data/
│   ├── raw/                 # Original CSV datasets
│   ├── processed/           # Cleaned CSVs and final scorecard exports
│   └── db/                  # SQLite database (blue_mf.db)
├── images/                  # Exported PNGs and interactive charts
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_db_ingestion.ipynb
│   ├── 03_eda_analysis.ipynb
│   └── 04_performance_analytics.ipynb
├── load_db.py               # Automated SQL ingestion script
└── README.md                # Project documentation
```
