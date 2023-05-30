class Product:
    """class represents a product in store
    Attributes: name, price, quantity, active(if in stock)"""
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity <= 0:
            raise ValueError("Check that attributes are valid (not empty and > 0)")
        try:
            self.name = name
            self.price = price
            self._quantity = quantity
            self._active = True
        except ValueError as error:
            print(error)

    def get_quantity(self) -> int:
        """:returns quantity of product in stock"""
        return self._quantity

    def activate(self):
        """Sets True to 'active' attribute"""
        self._active = True

    def deactivate(self):
        """Sets False to 'active' attribute"""
        self._active = False

    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product,
        updates the quantity of the product in stock
        :returns the total price of the purchase"""
        if quantity > self._quantity:
            raise ValueError(f"There's only {self._quantity} items left. You can't buy more.")
        try:
            self._quantity -= quantity
            if not self._quantity:
                self._active = False
            return self.price * quantity
        except ValueError as error:
            print(error)
            return 0

    def show(self) -> str:
        """:returns a string that represents the product"""
        return f"{self.name}, Price: {self.price}, Quantity: {self._quantity}"

    def is_active(self) -> bool:
        """:returns True if the product is active, otherwise False."""
        return self._active

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        self._quantity = quantity
        self.activate()
        if not self._quantity:
            self.deactivate()
