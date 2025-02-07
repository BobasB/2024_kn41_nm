import unittest

from program.bank import BankAccount

class TestProgram(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True, "True неправильно працює!")
    
    def test_should_fail(self):
        self.assertEqual(1, "1", "Число не є символом!")


if __name__ == '__main__':
    unittest.main(verbosity=2)

