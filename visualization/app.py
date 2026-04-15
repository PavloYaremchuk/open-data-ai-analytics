import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
import time

time.sleep(15)
DB_URL = "postgresql://admin:adminpassword@db:5432/hr_analytics"

def create_visualizations():
    print("Завантаження даних для візуалізації")
    engine = create_engine(DB_URL)
    df = pd.read_sql("SELECT * FROM employees", engine)

    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='payment_tier', hue='leave_or_not')
    plt.title("Звільнення залежно від рівня оплати (Payment Tier)")
    plt.savefig("/plots/payment_tier_churn.png")
    plt.close()

    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x='age', bins=20, kde=True)
    plt.title("Розподіл віку працівників")
    plt.savefig("/plots/age_distribution.png")
    plt.close()

    print("Графіки успішно згенеровано та збережено у папку /plots")

if __name__ == "__main__":
    create_visualizations()
