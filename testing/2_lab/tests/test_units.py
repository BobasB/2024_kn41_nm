import unittest
import pytest
from random import choice, randint

from program.bank import BankAccount

class TestProgram(unittest.TestCase):
    def setUp(self):
        self.name = choice(["Богдан", "Антон", "Максим"])
        self.number = randint(50, 100) # початковий баланс акаунту
        self.obj = BankAccount(self.name, self.number)
        return super().setUp()

    def test_obj_created(self):
        """Тестуємо створення обєкта
        """
        #obj = BankAccount("Богдан", 100)
        self.assertIsInstance(self.obj, BankAccount, f"Створений обєкт не нележить до класу {BankAccount}")
        self.assertTrue(len(self.obj.owner) > 0, "Імя власника має бути більше за 0")
        self.assertEqual(self.obj.owner, self.name, "Атрибут owner повинен дорівнювати Богдан")
        self.assertIsInstance(self.obj.owner, str, "Імя власника має бути стрічкового типу")
        
        with self.assertRaises(ValueError):
            print("Цей код виконується, і тут помила коректно опрацьовується!")
            obj2 = BankAccount("", -10)

        self.assertNotEqual(self.obj.balance, -1, "Баланс нового власника не можу бути рівним -1")

    def test_bankaccount_deposit(self):
        #b = 100
        #obj = BankAccount("Богдан", b)
        add_bal = 10
        self.obj.deposit(add_bal)
        self.assertEqual(self.obj.balance, self.number + add_bal, "При додаванні депозиту сімма має збільшуватись!")
        with self.assertRaises(ValueError, msg="Неправильно опарцьовується внесення депозиту"):
            self.obj.deposit(-50)
        self.assertGreater(self.obj.balance, self.number, "Після збільшення депозиту баланс має зрости")
        self.assertIsNotNone(self.obj.deposit(10), "Цей метод не повинен повертати None")

    def test_example(self):
        self.assertTrue(True, "True неправильно працює!")

    def test_should_fail(self):
        self.assertEqual(1, 1, "Число не є символом!")
    
    def test_no_asserts_in_test(self):
        print("Тест запуститься але він нічого не тестує")

    def test_make_it_great_again(self):
        assert self.obj.withdraw(20) < self.number, "Все пропало"
        with self.assertRaises(ValueError):
            self.obj.withdraw(-20)
        # тестуємо розгалуження
        with self.assertRaises(ValueError):
            self.obj.withdraw(1000)


@pytest.fixture
def try_my_fixture():
    o = BankAccount("N", 500)
    print(o.owner)
    return f"Ми спобували Фікстури, Власник = {o.owner}"


@pytest.fixture
def try_my_object():
    o = BankAccount("N", 500)
    return f"Знову спобували Фікстури, баланс = {o.balance}"

@pytest.fixture
def define_object():
    return BankAccount("Bohdan", 500)


def test_not_in_class(try_my_fixture, try_my_object):
    assert 1 == 1, "Тут 1 має бути рівним 1"
    print(try_my_fixture)
    assert isinstance(try_my_fixture, str), "Фікстура має повернути стрічку"
    assert "Власник" in try_my_fixture, "Неправильний вивід"
    assert "баланс" in try_my_object, "Неправильний вивід"

def test_bank_property(define_object):
    print(f"Тестуємо: {define_object.owner}")
    assert define_object.get_balance == define_object.balance, "Неправильно виводиться баланс"


if __name__ == '__main__':
    unittest.main(verbosity=2)
