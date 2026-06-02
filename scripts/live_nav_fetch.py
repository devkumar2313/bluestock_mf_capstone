import requests
import pandas as pd
from pathlib import Path
import time

def saver(code,name,raw_dir):
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"Fetching data for {name} ({code})...")

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        if 'data' in data and len(data['data'])>0:

            df = pd.DataFrame(data['data'])
            df['amfi_code'] = code

            df = df[['amfi_code','date','nav']]

            safe_name = name.replace(' ','_').lower()
            file_name = f"{code}_{safe_name}.csv"
            file_path = raw_dir / file_name

            df.to_csv(file_path,index=False)
            print(f"Saved {file_name}")
        else:
            print(f"No data for {code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")




if __name__ == "__main__":

    curr_dir = Path(__file__).resolve().parent
    base = curr_dir.parent
    raw_dir = base/'data'/'raw'

    raw_dir.mkdir(parents=True, exist_ok=True)

    schemes = {
        125497: "HDFC Top 100 Direct",
        119551: "SBI Bluechip",
        120503: "ICICI Bluechip",
        118632: "Nippon Large Cap",
        119092: "Axis Bluechip",
        120841: "Kotak Bluechip"
    }

    for code,name in schemes.items():

        saver(code,name,raw_dir)

        time.sleep(1)

    print('complete')