import pandas as pd
from pathlib import Path


def recommend_funds(risk_appetite: list):

    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir /"data" /"processed"

    try:
        perf_df = pd.read_csv(data_dir /"clean_scheme_performance.csv")
        master_df = pd.read_csv(data_dir /"processed_01_fund_master.csv")
    except FileNotFoundError as e:
        return f"Data file not found. Ensure ETL pipeline has run. Error: {e}"

    df = pd.merge(perf_df,master_df, on='amfi_code')

    if 'risk_category' in df.columns and 'risk_grade' in df.columns:
        df = df.drop(columns=['risk_category'])
    filtered = df[df['risk_grade'].isin(risk_appetite)]

    if filtered.empty:
        return pd.DataFrame()

    top_3 = filtered.sort_values(by='sharpe_ratio', ascending=False).head(3)
    desired_cols = ['amfi_code', 'scheme_name_x', 'category_x', 'risk_category', 'sharpe_ratio']
    available_cols = [col for col in desired_cols if col in top_3.columns]

    final_df = top_3[available_cols].copy()
    final_df = final_df.rename(columns={
        'scheme_name_x': 'scheme_name',
        'category_x': 'category'
    })

    return final_df


if __name__ == "__main__":
    print("~" * 50)
    print("BLUESTOCK MF PLATFORM - FUND RECOMMENDER")
    print("~" * 50)
    risk_dict = {
        'Low' : ['Low'],
        'Moderate' : ['Moderate','Moderately High'],
        'High' : ['High','Very High'],
    }
    for risk,val in risk_dict.items():
        print(f"\nTop Recommendations for [{risk}] Risk Profile:")
        recommendations = recommend_funds(val)
        if recommendations.empty:
            print("No funds matched this criteria.")
        else:
            print(recommendations.to_string(index=False))