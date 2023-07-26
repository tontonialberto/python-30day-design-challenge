from dataclasses import dataclass
from decimal import Decimal
from typing import Callable


@dataclass
class Discount:
    code: str
    """Discount code. Should be unique."""

    discount: Callable[[Decimal], Decimal]
    """Applies the discount to the given subtotal."""


DISCOUNT_SAVE10 = Discount(
    code="SAVE10",
    discount=lambda subtotal: subtotal * Decimal("0.1"),
)

DISCOUNT_5BUCKSOFF = Discount(
    code="5BUCKSOFF",
    discount=lambda subtotal: Decimal("5.00"),
)

DISCOUNT_FREESHIPPING = Discount(
    code="FREESHIPPING",
    discount=lambda subtotal: Decimal("2.00"),
)

DISCOUNT_BLKFRIDAY = Discount(
    code="BLKFRIDAY",
    discount=lambda subtotal: subtotal * Decimal("0.2"),
)