class Product():

    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity


class VendingMachine():

    def __init__(self):
        self.products_available = [Product("FiveStar", 5, 15)]
        self.coins_available = [Coins(1,10)]

    def show_products_available(self):
        print("%-10s %-10s %-10s " % ("Name", "Price", "Quantity Available"))
        for product in self.products_available:
            print("%-10s %-10s %-10s " % (product.name, product.price, product.quantity))

    def add_product(self):
        name = input("Enter Name of Product :")
        price = int(input("Enter Price of Product :"))
        quantity = int(input("Enter Qunatity of Produc :"))
        self.products_available.append(Product(name, price, quantity))

    def add_coins(self):
        value = int(input("Enter value of coin: "))
        quantity = int(input("Enter Qunatity of coin: "))

        self.coins_available.append(Coins())

class Coins():

    def __init__(self, value, quantity = 0):
        self.value = value
        self.quantity = quantity




if __name__ == "__main__":

    VendingMachine = VendingMachine()

    #VendingMachine.add_product()

    VendingMachine.show_products_available()
