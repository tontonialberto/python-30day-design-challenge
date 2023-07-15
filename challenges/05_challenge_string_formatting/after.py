from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int


def main():
    # Create a shopping cart
    items = [
        Item("Apple", Decimal("1.50"), 10),
        Item("Banana", Decimal("2.00"), 2),
        Item("Pizza", Decimal("11.90"), 5),
    ]

    total = sum(item.price * item.quantity for item in items)

    # Print the cart
    print("Shopping Cart:")
    print(f"{'Item':<10}{' ':>3} {'Price':>7} {'Qty':>6}{' ':>4}{'Total':>8}")
    # 10<-3^-6>- -4>- -3^-6>
    for item in items:
        total_price = item.price * item.quantity
        print(f"{item.name:<10}{'$':>3} {f'{item.price:.2f}':>7} {item.quantity:>6}{'$':>4}{f'{total_price:.2f}':>8}")
        # print(item.name, item.price, item.quantity, total_price, sep=", ")
    print(f"{'='}" * 40)
    print(f"Total: $ {total}")


if __name__ == "__main__":
    main()
