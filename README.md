# BlueStack Mutual Fund Analytics Capstone

## Project Overview
This capstone project establishes a secure, end-to-end data pipeline and unified business intelligence environment designed to process raw transactional and performance metrics across 40 distinct mutual fund schemes spanning 10 major AMCs[cite: 1]. It addresses massive data fragmentation in the Indian Mutual Fund industry by programmatically cleaning data, calculating advanced risk-adjusted metrics, and identifying at-risk investor cohorts[cite: 1]. 

The core output is a Composite Fund Scorecard that provides an unbiased, multi-factor framework for evaluating scheme health based on a strict matrix: 30% 3-Year CAGR, 25% Sharpe Ratio, 20% Benchmark Alpha, 15% Inverse Expense Ratio, and 10% Inverse Maximum Drawdown[cite: 1].

## Dataset Descriptions
The pipeline ingests raw data from primary financial authorities like AMFI and NSE, consisting of the following core files[cite: 1]:

*   **`01_fund_master.csv` (Scheme Metadata):** Contains the static reference data for the 40 mutual fund schemes, including attributes like the `amfi_code`, scheme category, SEBI risk grade, and total expense ratio (TER)[cite: 1].
*   **`02_nav_history.csv` (Pricing Time-Series):** The heaviest dataset, logging the daily Net Asset Value (NAV) prices for every scheme[cite: 1].
*   **`03_investor_transactions.csv` (Behavioral Logs):** A detailed ledger of retail capital movement that records user IDs, transaction dates, investment types (SIP vs. Lumpsum), and capital amounts[cite: 1].
*   **`04_benchmark_indices.csv` (Market Baselines):** Tracks the daily closing prices of the Nifty 50 index, which acts as the fundamental baseline for all comparative benchmarking (Alpha and Beta calculations)[cite: 1].
*   **`9_portfolio_holdings.csv` (Asset Allocation):** Details the internal composition of each mutual fund, mapping exact percentage allocations to specific market sectors[cite: 1].

## Project Structure
```text
├── data/
│   ├── raw/                   # Original CSV datasets (01_fund_master.csv, etc.)
│   ├── processed/             # Cleaned CSVs and intermediate files
│   └── db/                    # SQLite database (blue_mf.db)              
├── reports/images/                  
├── notebooks/                 # Jupyter Notebooks for EDA and analytics
├── scripts/                   # Exported visuals and PNGs
│   ├── 01_data_ingestion.py   # Automated data cleaning script
│   ├── 02_data_cleaning.py    # Star Schema generation script
│   └── load_database.py       # SQLite database loader        
├── run_pipeline.py            # Master ETL orchestrator
└── README.md                  # Project documentation
```
## Setup Instructions
1. **Clone the Repository:**
```bash
    git clone [https://github.com/devkumar2313/bluestock_mf_capstone.git](https://github.com/devkumar2313/bluestock_mf_capstone.git)
    cd bluestock_mf_capstone
```
2.  **Create a Virtual Environment (Optional but Recommended):**
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3.  **Install Dependencies:**
Ensure you have the required Python libraries installed:
```bash
    pip install pandas numpy matplotlib seaborn sqlalchemy sqlite3
```
4.  **Verify Data Placement:**
    Ensure your raw CSV datasets are securely placed inside the `data/raw/` directory.

## How to Run the ETL Pipeline
The entire Extract, Transform, and Load (ETL) process has been automated using a strict-path orchestration script.

1.  Open your terminal and ensure you are in the project's root directory.
2.  Execute the master pipeline script:
```bash
    python run_pipeline.py
```
3.  **Pipeline Execution Flow:** The script will automatically trigger:
    *   `01_data_ingestion.py`: Prepares the dimensional and fact table structures for the relational database[cite: 1].
    *   `02_data_cleaning.py`: Handles deduplication, data type casting, and algorithmically forward-fills missing NAV dates for weekends/holidays[cite: 1].
    *   `load_database.py`: Ingests the cleaned data into the `blue_mf.db` SQLite database using a highly optimized Star Schema model[cite: 1]. 

## How to Open the Dashboard
The presentation layer is built in Microsoft Power BI, utilizing a direct Business Intelligence connection to the generated SQLite database[cite: 1].

1.  Ensure you have completed the ETL pipeline steps above so the `blue_mf.db` file is fully populated in the `data/db/` folder.
2.  Open **Microsoft Power BI Desktop**.
3.  Open the project's `.pbix` dashboard file.
4.  If required, click **Refresh** in the Power BI ribbon. The dashboard will instantly query the SQLite Star Schema, ensuring lightning-fast updates for the Macro Industry tracking, Quantitative Performance Engine, and Behavioral Analytics pages without manual data manipulation[cite: 1].

***
