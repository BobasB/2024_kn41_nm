from program import bank
class SavingsAccount(bank.BankAccount):
    """Ощадний рахунок з відсотковою ставкою"""

    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        """Ініціалізація ощадного рахунку з процентною ставкою"""
        super().__init__(owner, balance)
        if interest_rate < 0:
            raise ValueError("Відсоткова ставка не може бути від'ємною")
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Нарахування відсотків на баланс"""
        self.balance += self.balance * self.interest_rate
        return self.balance
