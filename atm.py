class InvalidPinException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class ATM:
    """
    Klasa reprezentująca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """

    def __init__(self, correct_pin: int, initial_balance: float = 0.0):
        self._correct_pin = correct_pin
        self._balance = initial_balance

    def check_balance(self, pin: int) -> float:
        if pin != self._correct_pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        return self._balance

    def deposit(self, pin: int, amount: float) -> float:
        if pin != self._correct_pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        if amount < 0:
            raise ValueError("Nie można wpłacić ujemnej kwoty.")
        self._balance += amount
        return self._balance

    def withdraw(self, pin: int, amount: float) -> float:
        if pin != self._correct_pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        if amount < 0:
            raise ValueError("Nie można wypłacić ujemnej kwoty.")
        if amount > self._balance:
            raise InsufficientFundsException("Niewystarczające środki.")
        self._balance -= amount
        return self._balance
