from threading import RLock

class BankAccount(object):
    """
    Very simple Bank Account with transaction locking.
    """
    _lock = RLock()

    def __init__(self) -> None:
        self._balance = None

    def error_if_closed(self) -> None:
        """
        Raise a ValueError if the account is already closed.
        """
        if self._balance is None:
            raise ValueError("Cannot perform operations on a closed account!")

    def get_balance(self) -> int:
        """
        Get the curreny balance of the account.
        """
        with self._lock:
            self.error_if_closed()
            return self._balance

    def open(self) -> None:
        """
        Open the account and initialize the balance.
        """
        with self._lock:
            self._balance = 0

    def deposit(self, amount: int) -> None:
        """
        Deposit amount into account. Raises ValueError on negative amounts.
        """
        with self._lock:
            self.error_if_closed()
            if amount < 0:
                raise ValueError("Cannot make negative deposits!")
            self._balance += amount

    def withdraw(self, amount):
        """
        Withdraw amount from account. Raises ValueError on negative or overdraft withdrawls.
        """
        with self._lock:
            self.error_if_closed()
            if amount < 0:
                raise ValueError("Cannot make negative withdrawls!")
            elif amount > self._balance:
                raise ValueError("Cannot make withdrawls exceeding balance!")
            self._balance -= amount

    def close(self):
        """
        Close the account.
        """
        with self._lock:
            self._balance = None