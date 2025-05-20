# Virtual Tech Store CLI

This is a practice project that simulates a virtual tech store, demonstrating object-oriented programming (OOP) concepts in Python. It provides a simple command-line interface (CLI) to manage products and place orders.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Classes](#classes)
7. [Contributing](#contributing)
8. [License](#license)
9. [Author](#author)

## Features

* Define products with name, price, quantity, and active status
* Manage inventory of products in a store
* Place orders for one or multiple products
* Interactive CLI menu for listing products, viewing total stock, and making orders
* Exception handling for invalid inputs and insufficient stock

## Requirements

* Python 3.7 or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RomKow/Best_Buy.git
   cd Best_Buy
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```
3. No external dependencies required beyond the Python standard library.

## Usage

Run the main script to start the interactive CLI:

```bash
python main.py
```

Follow the on-screen prompts to:

1. List all products in the store
2. Show total number of items in stock
3. Make an order by selecting product numbers and quantities
4. Quit the program

## Project Structure

```
virtual-tech-store/
├── products.py    # Defines the Product class
├── store.py       # Defines the Store class
├── main.py        # CLI interface and entry point
└── README.md      # Project documentation
```

## Classes

### Product (in `products.py`)

* **Attributes**: `name` (str), `price` (float), `quantity` (int), `active` (bool)
* **Methods**:

  * `get_quantity() -> int`
  * `set_quantity(quantity: int) -> None`
  * `is_active() -> bool`
  * `activate() -> None`
  * `deactivate() -> None`
  * `show() -> str`
  * `buy(quantity: int) -> float`
  * `__str__() -> str`

### Store (in `store.py`)

* **Attributes**: `_products` (list of `Product`)
* **Methods**:

  * `add_product(product: Product) -> None`
  * `remove_product(product: Product) -> None`
  * `get_total_quantity() -> int`
  * `get_all_products() -> list[Product]`
  * `order(shopping_list: list[tuple[Product, int]]) -> float`

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve functionality, add tests, or enhance the CLI.

## License

This project is released under the [MIT License](LICENSE).

## Author

Roman — Software Architect

Enjoy exploring OOP with this virtual tech store CLI!
