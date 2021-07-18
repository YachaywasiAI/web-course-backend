import datetime

'''
Challenge 01
'''


def get_duty(name, age, limit_hour=18):
    if age < 18:
        current_hour = datetime.datetime.now().hour
        if(current_hour > limit_hour):
            print(f"{name}, go to sleep")
        else:
            print(f"{name}, have to do your homeworks")
    else:
        print(f"{name}, dont have duties")


get_duty(input('Name: '), int(input("Age: ")))

print('*********************************************')
print('*********************************************')
print('*********************************************')


'''
Challenge 02
'''

def sort_people_by_age():
    today = datetime.datetime.now().date()
    persons = []
    for i in range(int(input('Insert number of persons: '))):
        print(f'Person {i + 1}')
        persons.append(
            {
                'name': input('Name: '),
                'dni': input('DNI: '),
                'birth': datetime.date(
                    *(int(x) for x in input('Date of birth yyyy-mm-dd: ').split('-'))
                )
            }
        )
        persons[-1]['_days'] = (today - persons[-1]['birth']).days
        print('======================')
    sorted_persons = sorted(persons, key=lambda person: person['_days'], reverse=False)

    print("Sorted list: ")
    for i, person in enumerate(sorted_persons):
        print(f"{person['name']}")

sort_people_by_age()

print('*********************************************')
print('*********************************************')
print('*********************************************')

'''
Challenge 03
'''

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


