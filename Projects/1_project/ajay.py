class ShoppingCart:

    def __init__(self):
        self.store = {
            "book": {'price': 100, 'quantity': 5},
            'pen': {'price': 10, 'quantity': 10},
            "guitar": {'price': 8000, 'quantity': 2},
            "laptop": {'price': 50000, 'quantity': 1},
            "mouse": {'price': 800, 'quantity': 4},
            "keyboard": {'price': 3000, 'quantity': 1}
        }
        self.cart = {}
        self.totalPrice = 0

    def checkOut(self):
        try:
            if len(self.cart) == 0:
                raise Exception(
                    "your cart is empty, Please add items and Try again")
        except Exception as e:
            print(e)

    def addItem(self, item, quantity=0):

        try:

            if item not in self.store:
                raise Exception("Item is not avilable")
            if quantity == 0:
                raise ValueError
            if quantity > self.store[item]['quantity']:
                raise Exception("out of items. \nAvilable stock is {}".format(
                    self.store[item]['quantity']))

            self.cart[item] = quantity
            self.store[item]['quantity'] = self.store[item]['quantity'] - quantity
            print('{} is added to cart'.format(item))

        except ValueError:
            print("Please enter the quantity")
        except Exception as e:
            print(e)
        finally:
            print("Thank you for shopping!")

    def showCart(self):
        print('\n\n--item ------ quantity--')
        for item, itemquantity in self.cart.items():
            print(f'{item}:         {itemquantity}')
            itemPrice = self.store[item]['price']
            self.totalPrice += itemquantity * itemPrice

        print('====================')
        print('Total Price : {}\n'.format(self.totalPrice))

    def applycoupon(self, cupon=''):
        print('\n====================')
        try:
            if cupon == '':
                raise Exception("Please enter coupon")
            if cupon == "SAVE10":
                print('SAVE10 Coupon is applied')
                self.totalPrice = self.totalPrice - \
                    (self.totalPrice * (10/100))
            elif cupon == "50OFF":
                print('50OFF Coupon is applied')
                self.totalPrice = self.totalPrice * (50/100)
            else:
                raise Exception('Coupon is not valid')

            print('====================')
            print('Total Price : {}'.format(self.totalPrice))
        except Exception as e:
            print(e)
        finally:
            print("Thank you for shopping!")


if __name__ == "__main__":
    amazon = ShoppingCart()
    amazon.addItem("book", 2)
    amazon.addItem("laptop", 1)
    amazon.addItem("mouse", 2)
    amazon.showCart()
    amazon.applycoupon('50OFF')
