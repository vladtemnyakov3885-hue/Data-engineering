# Road Accident Analysis

## Датасет
Анализ данных о дорожно-транспортных происшествиях (US_Accidents_March23.csv).

# Руководство по обработке датасета

## Структура проекта

```
road-accidents/
├── etl/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
├── notebooks/
│   └── EDA.ipynb
├── data/
│   ├── raw/
│   └── processed/
├── requirements.txt
└── README.md
```

## Создание виртуального окружения
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск ETL

Выполнить команду
```powershell
python -m etl.main --url "https://drive.google.com/file/d/12nRUQVNdVxbi99UloXX9brJi2UcKti2-/view?usp=drive_link"
```
После запуска скрипт выполняет следующее:

## Загрузка данных с Google Drive
Сохраняет в папку ./data/raw  
Отображает первые 10 строк датасета для проверки

![alt text](pic/{3FC227F6-BA36-4F43-AE57-77F1A3889AC3}.png)

Показывает информацию о количестве записей и типах данных

![alt text](pic/{6C7AF8D2-A01B-4D1E-AF51-5B2B34DEB767}.png)

## Загрузка в БД

Загружает первую 1000 строк в базу данных

![alt text](pic/{DBCB2015-F355-484D-802F-F99029D0703C}.png)

## EDA

Анализ и работа с данными в EDA представлены в файле [EDA.ipynb](./notebooks/EDA.ipynb)

