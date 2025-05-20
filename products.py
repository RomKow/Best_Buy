class Product:
    """
    Represents a product in the store with name, price, quantity, and active state.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Return the current quantity."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Set the quantity; deactivate if it reaches 0."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        elif not self.active:
            self.activate()

    def is_active(self) -> bool:
        """Return True if product is active, else False."""
        return self.active

    def activate(self) -> None:
        """Mark the product as active."""
        self.active = True

    def deactivate(self) -> None:
        """Mark the product as inactive."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Purchase a quantity of the product.
        Returns the total price, updates quantity, and deactivates if 0.
        Raises if requested quantity invalid or insufficient stock.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Purchase quantity must be a positive integer.")
        if quantity > self.quantity:
            raise ValueError(
                f"Cannot purchase {quantity} items; only {self.quantity} in stock."
            )

        total = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return total

    def __str__(self) -> str:
        return self.show()


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))  # Expected 12500.0
    print(mac.buy(100))  # Expected 145000.0
    print(mac.is_active())  # Expected False

    print(bose.show())  # "Bose QuietComfort Earbuds, Price: 250.0, Quantity: 450"
    print(mac.show())  # "MacBook Air M2, Price: 1450.0, Quantity: 0"

    bose.set_quantity(1000)
    print(bose.show())  # "Bose QuietComfort Earbuds, Price: 250.0, Quantity: 1000"
