# name = str(input("Введіть пароль:"))
# assert len(name) > 5, "Потрібно вивести кілька символі!"
# #assert "Тестування" in name or "Методи" in name, "Введіть правильну назву предмета"
# assert name.isascii(), "Посинні бути символи з аблиці ASCII"
# assert name.islower(), "Використайти символи з Великої букви"
# assert name.isupper(), "Введіть символ з малої букви"
# print(f"ввели: {name}")

class MyName:
    def __init__(self, name:str):
        #assert name.isnumeric(), "Імя не посинне містити цифр"
        if name.isnumeric():
            # Це код дозволить програмі впасти ще до того як ми будемо використовувати дані обєкта
            raise TypeError("Імя не посинне містити цифр")
        self.name = name

a = MyName("Богдан")
b = MyName("123")
print(f"Імя першого обєкта: {a.name} та другого: {b.name}")