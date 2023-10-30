# Problem statement: Create a shopping cart simulation program. The program should allow users to:
# 1. Add products to the cart with their names, prices, and quantities.
# 2. Ensure that the quantity of items added to the cart is valid (greater than 0).
# 3. Apply discounts based on coupon codes ("SAVE10" and "50OFF").
# 4. Calculate the discounted total price.
# 5. Display the items in the cart and the final total price.
# 6. Handle exceptions (specifically, ValueError for invalid quantities) gracefully and provide error messages.
# 7. Regardless of exceptions, always display a "Thank you for shopping!" message.

class ShoppingCart:
    id = 0

    def __init__(self):
        self.cart = {}

    def add_to_cart(self, names, prices, quantities):
        grocery = {}
        if quantities > 0:
            grocery['name'] = names
            grocery['price'] = prices
            grocery['quantity'] = quantities
            ShoppingCart.id += 1
            self.cart[ShoppingCart.id] = grocery
            return self.cart
        else:
            raise ValueError("Quantity of items added to the cart is invalid.")

    def apply_coupon(self, discount_code):
        if discount_code == "SAVE10":
            return self.calculate_discounted_price(0.1)
        elif discount_code == "50OFF":
            return self.calculate_discounted_price(0.5)
        else:
            return self.calculate_discounted_price()

    def calculate_discounted_price(self, discount=0):
        total_price = 0

        for value in self.cart.values():
            total_price += value['price']

        return total_price * (1-discount)

    def checkout(self):
        for value in self.cart.values():
            print(
                f"Name: {value['name']}, Quantity: {value['quantity']}, Price: {value['price']}")

    def simulate_shopping(self, discount_code):
        Flag = True
        try:
            while Flag == True:
                self.name = input("Enter the grocery name: ")

                self.quantity = float(
                    input(f"Enter the quantity of the {self.name} in kgs: "))
                self.price = float(
                    input(f"Enter the price of the {self.name}: "))
                self.add_to_cart(self.name, self.price, self.quantity)
                flag = input("Do you want to continue? Y/N: ")
                if flag == 'Y' or flag == "y":
                    Flag = True
                else:
                    Flag = False
            total_price_after_discount = self.apply_coupon(discount_code)
            self.checkout()
            print(f"Total price after discount: {total_price_after_discount}")
        except ValueError as e:
            print(e)
        finally:
            print("Thank you for shopping!")


if __name__ == "__main__":
    shopping_cart = ShoppingCart()
    shopping_cart1 = ShoppingCart()
    shopping_cart.simulate_shopping("50OFF")
