import matplotlib.pyplot as plt
import seaborn as sns
import os
from data_load import load_employee_data


def create_visualizations(file_path, figures_path):
    print("Завантаження даних для візуалізації")
    df = load_employee_data(file_path)

    os.makedirs(figures_path, exist_ok=True)

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.barplot(x='PaymentTier', y='LeaveOrNot', data=df, errorbar=None, palette="viridis")
    plt.title('Відсоток звільнень за рівнем оплати (PaymentTier)')
    plt.ylabel('Ймовірність звільнення')
    file1 = os.path.join(figures_path, 'payment_tier_churn.png')
    plt.savefig(file1)
    plt.close()
    print(f"Збережено: {file1}")

    plt.figure(figsize=(6, 5))
    sns.barplot(x='EverBenched', y='LeaveOrNot', data=df, errorbar=None, palette="Set2")
    plt.title('Вплив відсутності завдань (EverBenched) на звільнення')
    plt.ylabel('Ймовірність звільнення')
    file2 = os.path.join(figures_path, 'benched_churn.png')
    plt.savefig(file2)
    plt.close()
    print(f"Збережено: {file2}")

    plt.figure(figsize=(10, 5))
    churn_by_year = df.groupby('JoiningYear')['LeaveOrNot'].mean().reset_index()
    sns.barplot(x='JoiningYear', y='LeaveOrNot', data=churn_by_year, palette="magma")
    plt.title('Динаміка звільнень за роком приєднання')
    plt.ylabel('Ймовірність звільнення')
    file3 = os.path.join(figures_path, 'joining_year_churn.png')
    plt.savefig(file3)
    plt.close()
    print(f"Збережено: {file3}")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_file = os.path.join(project_root, "data", "raw", "Employee.csv")
    figures_dir = os.path.join(project_root, "reports", "figures")

    create_visualizations(data_file, figures_dir)
