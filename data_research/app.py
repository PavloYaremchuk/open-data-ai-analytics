import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
from data_load import load_employee_data


def run_research(file_path):
    print("Завантаження даних для аналізу\n")
    df = load_employee_data(file_path)

    print("\nГіпотеза 1: Вплив зарплатного рівня (Payment Tier) на звільнення")
    tier_churn = df.groupby('PaymentTier')['LeaveOrNot'].mean() * 100
    print(tier_churn.round(2).astype(str) + " %")

    print("\nГіпотеза 2: Вплив тимчасової відсутності завдань (Ever Benched) на звільнення")
    benched_churn = df.groupby('EverBenched')['LeaveOrNot'].mean() * 100
    print(benched_churn.round(2).astype(str) + " %")

    print("\nГіпотеза 3: Динаміка звільнень залежно від року приєднання (Joining Year)")
    year_churn = df.groupby('JoiningYear')['LeaveOrNot'].mean() * 100
    print(year_churn.round(2).astype(str) + " %")


    print("\nПобудова ML моделі (Random Forest)\n")

    df_encoded = df.copy()
    categorical_cols = ['Education', 'City', 'Gender', 'EverBenched']

    for col in categorical_cols:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col])

    X = df_encoded.drop('LeaveOrNot', axis=1)
    y = df_encoded['LeaveOrNot']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Точність моделі (Accuracy): {accuracy:.2f}\n")
    print("Детальний звіт класифікації:")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_file = os.path.join(project_root, "data", "raw", "Employee.csv")

    run_research(data_file)
