import unittest
from program.savings import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    """Тести для класу SavingsAccount"""

    def setUp(self):
        """Створення об'єкта перед кожним тестом"""
        self.savings = SavingsAccount("Alice", 1000.0, 0.05)

    def test_arguments(self):
        self.assertEqual(self.savings.balance, 0, "Збереження більші за 0")
    
    def test_args_failed(self):
        self.assertEqual(self.savings.owner, "", "Пустий овнер")