class Product():

    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

class Coins():

    def __init__(self, value, quantity = 0):
        self.value = value
        self.quantity = quantity



class VendingMachine():

    products_available = [Product("FiveStar", 5, 15), Product("Lays", 10, 15), Product("Balaji", 10, 15), Product("Coke", 15, 15)]
    coins_available = [Coins(1,10), Coins(2,10), Coins(5,10), Coins(10,10)]

    @classmethod
    def show_products_available(cls):
        print("%-3s %-10s %-10s %-10s " % ("Sr.", "Name", "Price", "Quantity Available"))
        for i,product in enumerate(cls.products_available):
            print("%-3d %-10s %-10s %-10s " % (i + 1, product.name, product.price, product.quantity))

    @classmethod
    def add_product(cls):
        name = input("Enter Name of Product :")
        price = int(input("Enter Price of Product :"))
        quantity = int(input("Enter Qunatity of Produc :"))
        cls.products_available.append(Product(name, price, quantity))

    """
    def add_coins(self):
        value = int(input("Enter value of coin: "))
        quantity = int(input("Enter Qunatity of coin: "))

        self.coins_available.append(Coins())"""

    def insert_coin():
        pass

    @classmethod
    def select_product(cls, selected):
        if selected.isnumeric() and int(selected) <= len(cls.products_available):
            cls.insert_coin()
        else:
            print("Please Select from Available Products!")


    @classmethod
    def a_transaction(cls):
        print("Welcome, Please select a product.\n")
        cls.show_products_available()
        selected = input(">>> ")
        cls.select_product(selected)




if __name__ == "__main__":

    VendingMachine = VendingMachine()

    #VendingMachine.add_product()

    VendingMachine.a_transaction()
