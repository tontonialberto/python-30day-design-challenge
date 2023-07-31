from decimal import Decimal
from factory import register_payment_handler


def process_payment_revolut(total: Decimal) -> None:
    print(f"Processing payment of ${total:.2f} using Revolut...")


def load() -> None:
    register_payment_handler("revolut", process_payment_revolut)