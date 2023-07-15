from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Literal, Optional, Union


class ShoppingCartItemNotFound(Exception):
    pass


@dataclass
class Item:
    name: str
    price: Decimal
    quantity: int

    @property
    def total(self) -> Decimal:
        """Item's total price."""
        return self.price * self.quantity


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)
    discount_code: str | None = None

    @property
    def total(self) -> Union[Decimal, Literal[0]]:
        """Shopping cart's total price."""
        return sum(item.total for item in self.items)
    
    def _find_item_or_fail(self, name: str) -> Item:
        """Retrieve the cart item with the given name. Raise an error if it does not exist."""
        candidates: List[Item] = [
            item for item in self.items
            if item.name == name
        ]
        if len(candidates) == 0:
            raise ShoppingCartItemNotFound(f"Item '{name}' not found")
        return candidates[0]
    
    def remove_item(self, name: str) -> None:
        """Remove shopping cart item by name."""
        item = self._find_item_or_fail(name)
        self.items.remove(item)

    def update_item(self, name: str, price: Optional[Decimal] = None, quantity: Optional[int] = None) -> None:
        """Update cart item by name."""
        item = self._find_item_or_fail(name)
        if price is not None:
            item.price = price
        if quantity is not None:
            item.quantity = quantity


def display_shopping_cart(cart: ShoppingCart) -> None:
    """Print shopping cart in a tabular way."""
    print("Shopping Cart:")
    print(f"{'Item':<10}{'Price':>10}{'Qty':>7}{'Total':>13}")
    for item in cart.items:
        total_price = item.total
        print(
            f"{item.name:<12}${item.price:>7.2f}{item.quantity:>7}     ${total_price:>7.2f}"
        )
    print("=" * 40)
    print(f"Total: ${cart.total:>7.2f}")


def main() -> None:
    # Create a shopping cart and add some items to it
    cart = ShoppingCart(
        items=[
            Item("Apple", Decimal("1.5"), 10),
            Item("Banana", Decimal("2"), 2),
            Item("Pizza", Decimal("11.90"), 5),
        ],
    )

    # Update some items' quantity and price
    cart.update_item("Apple", quantity=10)
    cart.update_item("Pizza", price=Decimal("3.50"))

    # Remove an item
    cart.remove_item("Banana")

    # Print the cart
    display_shopping_cart(cart=cart)


if __name__ == "__main__":
    main()
