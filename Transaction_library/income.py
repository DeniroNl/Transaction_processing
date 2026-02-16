from transaction import Transaction
from datetime import datetime



class Income(Transaction):
    """
    Класс доходов содержащий сумму, дату, описание доходов
     и дополнительные методы для расчёта баланса и фильтра по дате
    """

    def __init__(self, date_str: str, amount: float, description: str):
        """
        Базовый конструктор класса
        :param date_str: Дата в формате ГГГГ-ММ-ДД
        :param amount: Сумма операции
        :param description: Описание операции
        """
        if amount <= 0:
            raise ValueError("Ошибка: Сумма дохода должна быть положительной.")
        super().__init__(date_str, abs(amount), description)



def add_income(transactions_list):
    """
     Метод для добавления расходов (заполняет param)
    :param transactions_list: Список всех транзакций
    """
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
    """
    Метод для расчёта баланса
    :param transactions_list: Список всех транзакций
    :return: Пустую строку
    """

    if not transactions_list:
        print("Нет операций для расчета баланса.")
        return None

    total_balance = sum(t.amount for t in transactions_list)
    total_income = sum(t.amount for t in transactions_list if t.amount > 0)
    total_expense = abs(sum(t.amount for t in transactions_list if t.amount < 0))

    print("\n--- Текущий баланс ---")
    print(f"Общий доход: {total_income} руб")
    print(f"Общий расход: {total_expense} руб")
    print(f"Итоговый баланс: {total_balance:} руб")
    return ""


def filter_by_date(transactions_list):
    """
    Метод длч отбора транзакций за определенный период времени и вывода их на экран.
    :param transactions_list: Список всех транзакций
    :return: Пустую строку
    """

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
    return ""


