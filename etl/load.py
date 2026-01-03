import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

def save_to_parquet(df: pd.DataFrame, output_path: str):
    """
    Сохраняет в Parquet.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"Parquet: {output_path}")

def load_to_db(output_path: str):
    """
    Загружает первые 1000 строк в SQLite.
    """
    df = pd.read_parquet(output_path)
    sample_df = df.head(1000).copy()
    
    engine = create_engine('sqlite:///data/accidents.db')
    sample_df.to_sql('accidents', engine, if_exists='replace', index=False)
    
    print(f"SQLite: data/accidents.db (1000 записей)")