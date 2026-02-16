from transaction import Transaction
from datetime import datetime
from expense import add_expense


class Income(Transaction):
    """Сумма всегда положительная. """

    def __init__(self, date_str: str, amount: float, description: str):
        """Инициализация дохода"""
        if amount <= 0:
            raise ValueError("Ошибка: Сумма дохода должна быть положительной.")
        super().__init__(date_str, abs(amount), description)



def add_income(transactions_list):
    """Добавление дохода."""
    print("\n--- Добавление дохода ---")

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
        income = Income(date_str, amount, description)
        transactions_list.append(income)
        print("Доход успешно добавлен!")
    except ValueError as e:
        print(f"Ошибка: {e}")


def calculate_balance(transactions_list):

    if not transactions_list:
        print("Нет операций для расчета баланса.")
        return None

    total_balance = sum(t.amount for t in transactions_list)
    total_income = sum(t.amount for t in transactions_list if t.amount > 0)
    total_expense = abs(sum(t.amount for t in transactions_list if t.amount < 0))

    print("\n--- Текущий баланс ---")
    print(f"Общий доход: {total_income:.2f} руб")
    print(f"Общий расход: {total_expense:.2f} руб")
    print(f"Итоговый баланс: {total_balance:+.2f} руб")
    return None


def filter_by_date(transactions_list):

    if not transactions_list:
        print("Нет операций для отображения.")
        return None

    print("\n--- Фильтр по дате ---")

    while True:
        try:
            start_date = input("Введите начальную дату (ГГГГ-ММ-ДД): ")
            start = datetime.strptime(start_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Неверный формат начальной даты!")

    while True:
        try:
            end_date = input("Введите конечную дату (ГГГГ-ММ-ДД): ")
            end = datetime.strptime(end_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Неверный формат конечной даты!")

    filtered = [t for t in transactions_list if start <= t.date <= end]

    if not filtered:
        print("За указанный период операций не найдено.")
    else:
        print(f"\nОперации с {start_date} по {end_date}:")
        for t in filtered:
            print(t.get_info())
    return None



if __name__ == "__main__":
    """Главная функция для запуска программы."""

    transactions = []
    """ Список для хранения всех транзакций"""

    while True:
        print("\nУчёт расходов и доходов")
        print("1. Добавить расход")
        print("2. Добавить доход")
        print("3. Рассчитать баланс")
        print("4. Фильтр операций по дате")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_expense(transactions)
        elif choice == '2':
            add_income(transactions)
        elif choice == '3':
            calculate_balance(transactions)
        elif choice == '4':
            filter_by_date(transactions)
        elif choice == '0':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт меню от 0 до 4.")
