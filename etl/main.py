import argparse
from etl.extract import read_accidents_data
from etl.transform import transform_accident_data
from etl.load import save_to_parquet, load_to_db

def etl_process(file_url: str):
    """
    Основной ETL процесс.
    """
    print("="*50)
    print("ETL: Анализ ДТП")
    print("="*50)
    
    # 1. Extract
    print("\n1️. ЗАГРУЗКА")
    df_raw = read_accidents_data(file_url)
    
    # 2. Transform
    print("\n2️. ОЧИСТКА")
    df_clean = transform_accident_data(df_raw)
    
    # 3. Load
    print("\n3️. СОХРАНЕНИЕ")
    save_to_parquet(df_clean, "data/processed/accidents.parquet")
    load_to_db("data/processed/accidents.parquet")
    
    print("\n   Готово!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETL для ДТП")
    parser.add_argument("--url", required=True, help="URL Google Drive файла")
    args = parser.parse_args()
    
    etl_process(args.url)