from products import Product


class StoreDB:
    """class represents a Store. Attribute: list of products"""
    def __init__(self, products: list):
        self.products = products

    def add_product(self, product):
        """Adds product to store"""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from store"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """:returns :how many items are in the store in total"""
        return int(sum(product.get_quantity() for product in self.products))

    def get_all_products(self) -> list[Product]:
        """:returns :all products in the store that are active"""
        return [product for product in self.products if product.is_active()]

    @staticmethod
    def order(shopping_list: list) -> float:
        """:param shopping_list: a list of tuples,
        where each tuple has 2 items: Product (Product class) and quantity (int).
        Buys the products.
        :returns :the total price of the order"""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
