from typing import List, Tuple
from products import Product


class Store:
    """
    Represents a store holding multiple products and allows operations on them.
    """

    def __init__(self, products: List[Product] = None) -> None:
        """
        Initialize the store with an optional list of products.
        """
        self._products: List[Product] = products.copy() if products else []

    def add_product(self, product: Product) -> None:
        """
        Add a product to the store.
        """
        if not isinstance(product, Product):
            raise ValueError("Can only add Product instances.")
        self._products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Remove a product from the store.
        """
        try:
            self._products.remove(product)
        except ValueError:
            raise ValueError("Product not found in store.")

    def get_total_quantity(self) -> int:
        """
        Return the total quantity of all products in the store.
        """
        return sum(p.get_quantity() for p in self._products)

    def get_all_products(self) -> List[Product]:
        """
        Return a list of active products in the store.
        """
        return [p for p in self._products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Place an order given a list of (Product, quantity) tuples.
        Returns the total price of the order.
        """
        total_price = 0.0
        for product, qty in shopping_list:
            if product not in self._products:
                raise ValueError(f"Product {product.name} not sold here.")
            total_price += product.buy(qty)
        return total_price


if __name__ == "__main__":
    import products

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)

    print(best_buy.get_total_quantity())  # Expected 850
    # Order 1 MacBook and 2 Earbuds
    active_products = best_buy.get_all_products()
    cost = best_buy.order([(active_products[0], 1), (active_products[1], 2)])
    print(cost)  # Expected 1450 + 500 = 1950
