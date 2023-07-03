from decimal import Decimal
from bank import Account, AccountType, BankService
from stripe_service import StripePaymentService


def main() -> None:
    savings_account = Account("SA001", Decimal("1000"), AccountType.SAVINGS)
    checking_account = Account("CA001", Decimal("500"), AccountType.CHECKING)

    payment_service = StripePaymentService(api_key="sk_test_1234567890")

    bank_service = BankService(payment_service)

    bank_service.deposit(Decimal("200"), savings_account)
    bank_service.deposit(Decimal("300"), checking_account)

    bank_service.withdraw(Decimal("100"), savings_account)
    bank_service.withdraw(Decimal("200"), checking_account)

    print(f"Savings Account Balance: {savings_account.balance}")
    print(f"Checking Account Balance: {checking_account.balance}")


if __name__ == "__main__":
    main()
