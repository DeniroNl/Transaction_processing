from transaction import Transaction
from datetime import datetime


class Expense(Transaction):
    """
    Класс расходов. Сумма всегда отрицательная.
    """

    def __init__(self, date_str: str, amount: float, description: str):
        """
        Инициализация расхода.
        """
        if amount <= 0:
            raise ValueError("Ошибка: Сумма расхода должна быть положительной.")
        super().__init__(date_str, -abs(amount), description)


def add_expense(transactions_list):
    """Добавление расхода."""
    print("\n--- Добавление расхода ---")

    while True:
        try:
            date_str = input("Введите дату (ГГГГ-ММ-ДД): ")
            datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Неверный формат даты!")

    while True:
        try:
            amount = float(input("Введите сумму: "))
            if amount <= 0:
                print("Сумма должна быть положительной!")
                continue
            break
        except ValueError:
            print("Введите число!")

    description = input("Введите описание: ").strip()
    if not description:
        description = "Без описания"

    try:
        expense = Expense(date_str, amount, description)
        transactions_list.append(expense)
        print("Расход успешно добавлен!")
    except ValueError as e:
        print(f"Ошибка: {e}")