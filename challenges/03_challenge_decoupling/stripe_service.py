from dataclasses import dataclass
from decimal import Decimal

from payment_service import PaymentService


@dataclass
class StripePaymentService(PaymentService):
    api_key: str

    def process_payment(self, amount: Decimal) -> None:
        print(f"Processing payment of {amount} via Stripe.")

    def process_payout(self, amount: Decimal) -> None:
        print(f"Processing payout of {amount} via Stripe.")
