class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart1(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_price1 = price*quantity
        try:
            if(quantity < 0):
                raise ValueError

        except ValueError:
            print("quantity cannot be zero")

        except:
            print("quantity cannot be negative")

        finally:
            print("Thank You for Shopping!")

        print(f"{self.name} {self.price} {self.quantity} {self.total_price1}")

    def add_to_cart2(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total_price2 = price*quantity
        print(f"{self.name} {self.price} {self.quantity} {self.total_price2}")
        try:
            if(quantity < 0):
                raise ValueError

        except ValueError:
            print("quantity cannot be zero")

        except:
            print("quantity cannot be negative")
    #     pass
    #     return total_price(price,quantity)
    # def total_price(self,price,quantity):
    #     return sum(self.price * self.quantity)

    def apply_coupon():
        pass

    def calcute_discounted_price(self, discount):
        return print((self.total_price1+self.total_price2) * (1-discount))
        pass

    def checkout(self):
        for item in self.cart:
            print(item)

    def simulate_shopping(self, input):
        self.add_to_cart1("rice", 50, 3)
        self.add_to_cart2("dal", 100, 3)
        self.checkout()
        if input == "SAVE10":
            self.calcute_discounted_price(0.1)
        elif input == "50OFF":
            self.calcute_discounted_price(0.5)
        else:
            self.calcute_discounted_price(0)
        pass


if __name__ == "__main__":
    shopping_cart = ShoppingCart()
    shopping_cart1 = ShoppingCart()
    shopping_cart.simulate_shopping("SAVE10")
