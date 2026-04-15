import pandas as pd
from sqlalchemy import create_engine
import json
import time

time.sleep(10)
DB_URL = "postgresql://admin:adminpassword@db:5432/hr_analytics"


def analyze_quality():
    print("Завантаження даних з бази для перевірки якості")
    engine = create_engine(DB_URL)
    df = pd.read_sql("SELECT * FROM employees", engine)

    report = {
        "total_rows": len(df),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates_count": int(df.duplicated().sum()),
        "data_types": df.dtypes.astype(str).to_dict()
    }

    with open("/reports/quality_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print("Звіт про якість даних (quality_report.json) успішно збережено")


if __name__ == "__main__":
    analyze_quality()
