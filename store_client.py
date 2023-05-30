from collections import defaultdict

from storedb import StoreDB


class StoreClient:
    """class represents CLI"""
    def __init__(self, store_db: StoreDB):
        self.store_db = store_db

    def run(self):
        """Looped interface that asks a user's choice and executes a command"""
        while True:
            print(f"\n{'Store Menu' :-^30}\n",
                  "1. List all products in store\n",
                  "2. Show total amount in store\n",
                  "3. Make an order\n",
                  "4. Quit\n")

            res = input("Please, choose a number (1-4): ")

            if res in ("1", "3"):
                self.list_all_products()
            if res == "2":
                self.show_total_amount()
            if res == "3":
                print("\nWhen you want to finish order, enter empty text.")
                self.make_order()
            if res == "4":
                break

    def list_all_products(self):
        """prints a list of available products in store"""
        products = self.store_db.get_all_products()
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product.show()}")

    def show_total_amount(self):
        """prints how many items are in the store in total"""
        print(f"\nTotal of {self.store_db.get_total_quantity()} items in store")

    def make_order(self):
        """Ask a user what product and quantity to buy, Buys it if possible"""
        products = self.store_db.get_all_products()
        shopping_prod_to_quant = defaultdict(int)
        while True:
            product_num = input("Which product do you want? (Enter a number): ")
            amount = input("What amount do you want?: ")
            if product_num and amount:
                try:
                    current_amount = products[int(product_num) - 1].get_quantity()
                    product = products[int(product_num) - 1]
                    amount = int(amount)
                    if current_amount < amount or \
                            current_amount < shopping_prod_to_quant.get(product, 0) + amount:
                        raise ValueError(
                            "There's only "
                            f"{current_amount - shopping_prod_to_quant.get(product, 0)}"
                            " items left. You can't buy more.\n")
                    shopping_prod_to_quant[product] += amount
                    print("Product added to list!\n")
                    continue
                except ValueError as error:
                    print(error, "\n")
                    continue
                except IndexError:
                    print("Error adding product!\n")
                    continue
            else:
                if shopping_prod_to_quant:
                    shopping_list = list(shopping_prod_to_quant.items())
                    payment = self.store_db.order(shopping_list)
                    print(f"Order made! Total payment: ${payment}")
                break
