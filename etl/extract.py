import pandas as pd
from pathlib import Path
import requests
import gdown
import warnings
warnings.filterwarnings('ignore')

def read_accidents_data(file_url: str) -> pd.DataFrame:
    """
    Загружает US_Accidents_March23.csv с Google Drive.
    """
    print(f"Загрузка данных: {file_url}")
    
    # Извлекаем ID файла из Google Drive ссылки
    if 'id=' in file_url:
        file_id = file_url.split('id=')[1].split('&')[0]
    elif '/file/d/' in file_url:
        file_id = file_url.split('/file/d/')[1].split('/')[0]
    else:
        file_id = file_url  # Если уже ID
    
    # Скачиваем через gdown
    output_path = "data/raw/US_Accidents_March23.csv"
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    
    gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)
    
    # Читаем CSV
    print("Чтение CSV файла...")
    df = pd.read_csv(output_path, low_memory=False)
    
    print(f"Данные загружены: {df.shape[0]:,} строк, {df.shape[1]} колонок")
    print(f"Первые 3 строки:")
    print(df[['ID', 'Severity', 'Start_Time', 'City', 'State']].head(3))
    
    return df