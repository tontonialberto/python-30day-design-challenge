from decimal import Decimal
from typing import Callable, List


PaymentHandlerFn = Callable[[Decimal], None]


payment_handlers: dict[str, PaymentHandlerFn] = {}


def register_payment_handler(name: str, payment_handler: PaymentHandlerFn) -> None:
    payment_handlers[name] = payment_handler


def unregister_payment_handler(name: str) -> None:
    payment_handlers.pop(name)


def get_all_available_payment_method_names() -> List[str]:
    return list(payment_handlers.keys())