from products import Product
from storedb import StoreDB
from store_client import StoreClient


def main():
    """Creates products, Store and CLI instances. Runs app"""
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    StoreClient(StoreDB(product_list)).run()


if __name__ == '__main__':
    main()