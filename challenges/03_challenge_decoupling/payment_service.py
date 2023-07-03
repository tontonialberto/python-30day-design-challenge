from abc import ABC, abstractmethod
from decimal import Decimal

class PaymentService(ABC):
    @abstractmethod
    def process_payment(self, amount: Decimal) -> None:
        pass

    @abstractmethod
    def process_payout(self, amount: Decimal) -> None:
        pass