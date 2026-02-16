from datetime import datetime, date

class Transaction:
    """
    Класс для обработки финансовой транзакции
    """
    def __init__(self, date_str: str, amount: float, description: str):
        """
        Базовый конструктор класса
        :param date_str: Дата в формате ГГГГ-ММ-ДД
        :param amount: Сумма транзакции
        :param description: Описание транзакции
        """
        self.date = self._validate_date(date_str)
        self.amount = amount
        self.description = description

    @staticmethod
    def _validate_date(date_str: str) -> date:
        """
        Метод для обработки даты транзакции
        :param date_str:
        :return: date
        """

        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Ошибка: Неверный формат даты. Используйте ГГГГ-ММ-ДД (например, 2023-10-05).")

    def get_info(self) -> str:
        """
        Метод для выведения информации о транзакции
        :return: информации об операции через str
        """

        type_name = self.__class__.__name__
        sign = "+" if self.amount > 0 else ""
        return f"[{type_name}] {self.date}\n{sign}{self.amount} руб\n{self.description}"

