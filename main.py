import products
import store


def start(store_obj):
    """
    Interactive CLI to manage store operations.
    """
    while True:
        print()
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            items = store_obj.get_all_products()
            for idx, prod in enumerate(items, 1):
                print(f"{idx}. {prod.show()}")

        elif choice == "2":
            total = store_obj.get_total_quantity()
            print(f"Total items in store: {total}")

        elif choice == "3":
            items = store_obj.get_all_products()
            order_list = []
            print("Enter product number and quantity. Type 'done' to finish.")

            while True:
                sel = input("Product number (or 'done'): ")
                if sel.lower() == 'done':
                    break
                try:
                    idx = int(sel) - 1
                    if idx < 0 or idx >= len(items):
                        print("Invalid product number.")
                        continue
                    qty = int(input("Quantity: "))
                    order_list.append((items[idx], qty))
                except ValueError:
                    print("Invalid input.")
                    continue

            if order_list:
                try:
                    cost = store_obj.order(order_list)
                    print("********")
                    print(f"Order made! Total payment: ${cost}")
                except Exception as err:
                    print(f"Error processing order: {err}")

        elif choice == "4":  # Quit
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)
