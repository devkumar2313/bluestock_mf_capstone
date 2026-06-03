import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine,text

def load_db():
    db_path = Path('../data/db')
    db_path.mkdir(parents=True,exist_ok=True)
    db_path_ori = db_path / 'blue_mf.db'

    engine = create_engine(f'sqlite:///{db_path_ori}')

    raw_dir = Path('../data/raw')
    processed_dir = Path('../data/processed')

    table_mapping ={
        'dim_fund' : raw_dir/'01_fund_master.csv',
        'fact_nav' : processed_dir/'clean_nav_history.csv',
        'fact_transactions':processed_dir/'clean_investor_transactions.csv',
        'fact_performance':processed_dir/'clean_scheme_performance.csv',
        'fact_aum' : raw_dir/'03_aum_by_fund_house.csv'
    }

    for table,file_path in table_mapping.items():
        if(file_path.exists()):
            df = pd.read_csv(file_path)
            df.to_sql(table,engine,if_exists='replace',index=False)

            with engine.connect() as con:
                count = con.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()

            if(len(df) != count):
                print(f"Mismatch occur in {table}")
        else:
            print(f"File {file_path} missing!")

if __name__ == '__main__':
    load_db()