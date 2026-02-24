import pandas as pd
import os

def check_quality(file_path):
    df = pd.read_csv(file_path)
    print("Перевірка якості даних")
    print(f"Кількість рядків: {df.shape[0]}")
    print(f"Пропущені значення:\n{df.isnull().sum()}\n")
    print(f"Кількість дублікатів: {df.duplicated().sum()}")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(current_dir), "data", "raw", "Employee.csv")
    check_quality(data_path)
