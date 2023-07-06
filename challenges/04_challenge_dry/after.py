from decimal import Decimal
from dataclasses import dataclass
from enum import StrEnum
from typing import Iterable


class OrderType(StrEnum):
    ONLINE = "online"
    IN_STORE = "in store"


@dataclass
class Item:
    name: str
    price: Decimal


@dataclass
class Order:
    id: int
    type: OrderType
    customer_email: str


@dataclass
class Email:
    body: str
    subject: str
    recipient: str
    sender: str


WEBSHOP_EMAIL = "sales@webshop.com"


def calculate_total_price(items: Iterable[Item]) -> Decimal:
    total_price = Decimal(sum(item.price for item in items))
    return total_price


def calculate_discounted_price(items: Iterable[Item], discount: Decimal) -> Decimal:
    total_price = calculate_total_price(items)
    discounted_price = total_price - (total_price * discount)
    return discounted_price


def generate_email(*, subject: str, body: str, sender: str, recipient: str) -> Email:
    return Email(
        body=body,
        subject=subject,
        recipient=recipient,
        sender=sender,
    )


def generate_order_confirmation_email(order: Order, sender: str) -> Email:
    return generate_email(
        subject="Order Confirmation",
        body=f"Thank you for your order! Your order #{order.id} has been confirmed.",
        sender=sender,
        recipient=order.customer_email,
    )


def generate_order_shipping_notification(order: Order, sender: str) -> Email:
    return generate_email(
        subject="Order Shipped",
        body=f"Good news! Your order #{order.id} has been shipped and is on its way.",
        sender=sender,
        recipient=order.customer_email,
    )


def process_order(order: Order) -> None:
    print(f"Processing {order.type} order...")
    print(generate_order_confirmation_email(order, sender=WEBSHOP_EMAIL))
    if order.type == OrderType.ONLINE:
        print("Shipping the order...")
        print(generate_order_shipping_notification(order, sender=WEBSHOP_EMAIL))
    elif order.type == OrderType.IN_STORE:
        print("Order ready for pickup.")
    print("Order processed successfully.")


def main() -> None:
    items = [
        Item(name="T-Shirt", price=Decimal("19.99")),
        Item(name="Jeans", price=Decimal("49.99")),
        Item(name="Shoes", price=Decimal("79.99")),
    ]

    online_order = Order(
        id=123, type=OrderType.ONLINE, customer_email="sarah@gmail.com"
    )

    total_price = calculate_total_price(items)
    print("Total price:", total_price)

    discounted_price = calculate_discounted_price(items, Decimal("0.1"))
    print("Discounted price:", discounted_price)

    process_order(online_order)

    in_store_order = Order(
        id=456, type=OrderType.IN_STORE, customer_email="john@gmail.com"
    )

    process_order(in_store_order)


if __name__ == "__main__":
    main()
