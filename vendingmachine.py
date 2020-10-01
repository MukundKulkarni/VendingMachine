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
        price = int(input("Write the intial project price :"))
        quantity = int(input("Enter the number of product (Quantities) :"))
        cls.products_available.append(Product(name, price, quantity))

    """
    def add_coins(self):
        value = int(input("Enter value of coin: "))
        quantity = int(input("Enter Qunatity of coin: "))

        self.coins_available.append(Coins())"""

    @classmethod
    def insert_coin(cls, selected):
        cost = cls.products_available[selected - 1].price
        print("Enter the at aleast % d Rupees" % (cost))
        amount_inserted = int(input(">>> "))
        if amount_inserted < cost:
            print("Please Enter % d more : " % (cost - amount_inserted))
        elif amount_inserted == cost:
            #Greetings and display Rupees.
            print("have a Good day & Enjoy your % s" % (cls.products_available[selected-1].name))
            cls.update_product_count(selected)
            cls.update_coin_count(amount_inserted)
        else:
            change = amount_inserted - cost
            print("Collect here your % d Rupees of change." % (change))
            #it will show the change.
            print("Enjoy your % s" % (cls.products_available[selected-1].name))
            cls.update_product_count(selected)
            cls.update_coin_count(amount_inserted, change)


    @classmethod
    def select_product(cls, selected):
        if selected <= len(cls.products_available) and selected >= 1:
            cls.insert_coin(selected)
        else:
            print("Select anything from Available Products! : ")


    @classmethod
    def a_transaction(cls):
        print("Welcome back!, Please choose or select the product.\n")
        #wait for user till he select the product.
        cls.show_products_available()
        selected = int(input(">>> "))
        cls.select_product(selected)

    @classmethod
    def update_product_count(cls, selected):
        cls.products_available[selected-1].quantity -= 1


    @classmethod
    def update_coin_count(cls, amount_inserted, change = 0):
        idx = { 1 : 0,
                2 : 1,
                5 : 2,
                10 : 3,
            }

        if change == 0:
            cls.coins_available[idx[amount_inserted]].quantity += 1


if __name__ == "__main__":

    VendingMachine = VendingMachine()

    #VendingMachine.add_product()

    VendingMachine.a_transaction()

    VendingMachine.show_products_available()
