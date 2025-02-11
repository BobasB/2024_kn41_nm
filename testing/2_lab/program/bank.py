class BankAccount:
    """Клас банківського рахунку"""

    def __init__(self, owner: str, balance: float = 0.0):
        """Ініціалізація рахунку з іменем власника та початковим балансом"""
        if len(owner) <= 0:
            raise ValueError("Імя власника не може бути меншим 0!")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        """Поповнення рахунку"""
        if amount <= 0:
            raise ValueError("Сума депозиту має бути більше нуля")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        """Зняття коштів з рахунку"""
        if amount <= 0:
            raise ValueError("Сума зняття має бути більше нуля")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """Отримання балансу"""
        return self.balance
