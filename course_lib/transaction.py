from datetime import datetime, date

class Transaction:
    """
    Класс для финансовой транзакции.
    Содержит атрибуты: дата, сумма, описание.
    """
    def __init__(self, date_str: str, amount: float, description: str):
        """
        Инициализация.
        :date_str: Дата в формате ГГГГ-ММ-ДД
        :amount: Сумма транзакции (может быть отрицательной для расходов)
        :description: Описание транзакции
        """
        self.date = self._validate_date(date_str)
        self.amount = amount
        self.description = description

    @staticmethod
    def _validate_date(date_str: str) -> date:
        """Защита: проверка корректности формата даты."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Ошибка: Неверный формат даты. Используйте ГГГГ-ММ-ДД (например, 2023-10-05).")

    def get_info(self) -> str:
        """Возвращает строковое представление транзакции."""
        type_name = self.__class__.__name__
        sign = "+" if self.amount > 0 else ""
        return f"[{type_name}] {self.date}\n{sign}{self.amount} руб\n{self.description}"