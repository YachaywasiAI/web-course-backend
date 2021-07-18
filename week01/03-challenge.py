class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def show_description(self):
        return self.description

class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price, description):
        self.products[name] = Product(name, price, description)

    def find_products_and_show_description(self):
        while (True):
            name = input('Insert product to search: ')
            if name in self.products:
                print(f"Description {self.products[name].show_description()}")
            else:
                print(f"There isnt {name} available")
            if input("Press 0 (and enter) to exit or enter to continue") == "0":
                break

my_store = Store()

for i in range(int(input('Insert number of products '))):
    print(f"Product {i + 1}")
    my_store.add_product(
        input('Name '),
        float(input('Price ')),
        input('Description '),
    )
    print('======================')

my_store.find_products_and_show_description()

