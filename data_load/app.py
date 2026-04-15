import pandas as pd
from sqlalchemy import create_engine
import time

print("Очікування бази даних")
time.sleep(5)

DB_URL = "postgresql://admin:adminpassword@db:5432/hr_analytics"


def load_data():
    print("1. Зчитування CSV файлу")
    df = pd.read_csv("/data/Employee.csv")

    print("2. Підключення до БД та створення таблиці")
    engine = create_engine(DB_URL)

    df.to_sql(name='employees', con=engine, if_exists='replace', index=False)
    print(f"Успішно завантажено {len(df)} записів у базу даних")


if __name__ == "__main__":
    load_data()
