import unittest
from atm import ATM, InvalidPinException, InsufficientFundsException

class TestATM(unittest.TestCase):

    def setUp(self):
        self.atm = ATM(correct_pin=1234, initial_balance=1000.0)

    def test_check_balance_should_return_balance_when_pin_is_correct(self):
        balance = self.atm.check_balance(1234)
        self.assertEqual(balance, 1000.0)

    def test_check_balance_should_raise_exception_when_pin_is_incorrect(self):
        with self.assertRaises(InvalidPinException):
            self.atm.check_balance(1111)

    def test_deposit_should_increase_balance_when_pin_is_correct(self):
        new_balance = self.atm.deposit(1234, 500.0)
        self.assertEqual(new_balance, 1500.0)

    def test_deposit_should_raise_exception_when_pin_is_incorrect(self):
        with self.assertRaises(InvalidPinException):
            self.atm.deposit(1111, 500.0)

    def test_deposit_should_raise_exception_when_amount_is_negative(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(1234, -100.0)

    def test_withdraw_should_decrease_balance_when_pin_and_amount_are_correct(self):
        new_balance = self.atm.withdraw(1234, 400.0)
        self.assertEqual(new_balance, 600.0)

    def test_withdraw_should_raise_exception_when_pin_is_incorrect(self):
        with self.assertRaises(InvalidPinException):
            self.atm.withdraw(1111, 400.0)

    def test_withdraw_should_raise_exception_when_amount_is_negative(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(1234, -100.0)

    def test_withdraw_should_raise_exception_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsException):
            self.atm.withdraw(1234, 2000.0)

if __name__ == '__main__':
    unittest.main()
