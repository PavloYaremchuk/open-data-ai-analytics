import pandas as pd
from sqlalchemy import create_engine
import json
import time

time.sleep(12)
DB_URL = "postgresql://admin:adminpassword@db:5432/hr_analytics"


def research_data():
    print("Завантаження даних для дослідження")
    engine = create_engine(DB_URL)
    df = pd.read_sql("SELECT * FROM employees", engine)

    stats = df.describe().to_dict()

    with open("/reports/research_summary.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=4, ensure_ascii=False)

    print("Дослідження даних (research_summary.json) успішно збережено")


if __name__ == "__main__":
    research_data()
