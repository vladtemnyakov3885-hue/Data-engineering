import pandas as pd
import numpy as np

def transform_accident_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Очищает и преобразует данные ДТП.
    """
    df_clean = df.copy()
    
    print("Начинаю очистку данных...")
    
    # 1. Даты
    if 'Start_Time' in df_clean.columns:
        df_clean['Start_Time'] = pd.to_datetime(df_clean['Start_Time'], errors='coerce')
        df_clean['Start_Year'] = df_clean['Start_Time'].dt.year
        df_clean['Start_Month'] = df_clean['Start_Time'].dt.month
        df_clean['Start_Day'] = df_clean['Start_Time'].dt.day
        df_clean['Start_Hour'] = df_clean['Start_Time'].dt.hour
        df_clean['Start_Weekday'] = df_clean['Start_Time'].dt.weekday
    
    if 'End_Time' in df_clean.columns:
        df_clean['End_Time'] = pd.to_datetime(df_clean['End_Time'], errors='coerce')
    
    # 2. Числовые колонки
    numeric_cols = ['Severity', 'Distance(mi)', 'Temperature(F)', 'Humidity(%)', 
                   'Pressure(in)', 'Visibility(mi)', 'Wind_Speed(mph)', 'Precipitation(in)']
    
    for col in numeric_cols:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    # 3. Категориальные
    categorical_cols = ['State', 'City', 'County', 'Timezone', 'Weather_Condition', 
                       'Sunrise_Sunset', 'Civil_Twilight']
    
    for col in categorical_cols:
        if col in df_clean.columns and df_clean[col].nunique() < 100:
            df_clean[col] = df_clean[col].astype('category')
    
    print("Очистка завершена")
    print(f"Типы данных: {df_clean.dtypes.value_counts().to_dict()}")
    
    return df_clean