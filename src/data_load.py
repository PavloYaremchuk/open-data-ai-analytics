import pandas as pd
import os


def load_employee_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не знайдено: {file_path}.")

    df = pd.read_csv(file_path)
    print(f"Дані успішно завантажено. Розмір датасету: {df.shape}")

    return df


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, "data", "raw", "Employee.csv")

    dataset = load_employee_data(data_path)

    print(dataset.head())
