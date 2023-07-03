from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from payment_service import PaymentService


class AccountType(Enum):
    SAVINGS = "Savings"
    CHECKING = "Checking"
    

@dataclass
class Account:
    account_number: str
    balance: Decimal

    type: AccountType
    """String representing the type of the account."""


class BankService:
    def __init__(self, payment_service: PaymentService) -> None:
        self.__payment_service = payment_service

    def deposit(
        self, amount: Decimal, account: Account
    ) -> None:
        print(f"Depositing {amount} into {account.type.value} Account {account.account_number}.")
        self.__payment_service.process_payment(amount)
        account.balance += amount

    def withdraw(
        self, amount: Decimal, account: Account
    ) -> None:
        print(f"Withdrawing {amount} from {account.type.value} Account {account.account_number}.")
        self.__payment_service.process_payout(amount)
        account.balance -= amount
