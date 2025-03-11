# name = str(input("Введіть пароль:"))
# assert len(name) > 5, "Потрібно вивести кілька символі!"
# #assert "Тестування" in name or "Методи" in name, "Введіть правильну назву предмета"
# assert name.isascii(), "Посинні бути символи з аблиці ASCII"
# assert name.islower(), "Використайти символи з Великої букви"
# assert name.isupper(), "Введіть символ з малої букви"
# print(f"ввели: {name}")

# class MyName:
#     def __init__(self, name:str):
#         #assert name.isnumeric(), "Імя не посинне містити цифр"
#         if name.isnumeric():
#             # Це код дозволить програмі впасти ще до того як ми будемо використовувати дані обєкта
#             raise TypeError("Імя не посинне містити цифр")
#         self.name = name

# a = MyName("Богдан")
# b = MyName("123")
# print(f"Імя першого обєкта: {a.name} та другого: {b.name}")
def new_fun():
    return 50

from program import bank
from program import savings

if __name__ == "__main__":
    b = bank.BankAccount("БвБ", 1.1)
    print(f"Баланс {b.owner}: {b.get_balance}")
    b.deposit(2.5)
    print(f"Баланс {b.owner}: {b.get_balance}")
    print(dir(bank.BankAccount))

    ss = savings.SavingsAccount("Alice", 1000.0, 0.05)
    print(f"У друшому класі баланс: {ss.balance}")
