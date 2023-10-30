class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.total_price = 0.0

    def add_to_cart(self, product_name, price, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        item = {"product": product_name, "price": price, "quantity": quantity}
        self.cart.append(item)
        self.total_price += price * quantity

    def apply_coupon(self, coupon_code):
        discount = 0.0
        if coupon_code == "SAVE10":
            discount = 0.10  # 10% discount
        elif coupon_code == "50OFF":
            discount = 0.50  # 50% discount
        return discount

    def calculate_discounted_price(self, discount):
        return self.total_price * (1 - discount)

    def checkout(self):
        print("Items in Cart:")
        for item in self.cart:
            print(
                f"{item['product']} - ₹{item['price']} x {item['quantity']} = {item['price'] *item['quantity']}")
        print(f"Total Price: ₹{self.total_price:.2f}")

    def simulate_shopping(self, coupon=None):
        try:
            self.add_to_cart("Product A", 200.0, 2)  # Prices in Rupees
            self.add_to_cart("Product B", 150.0)    # Prices in Rupees
            self.add_to_cart("Product C", 250.0, 0)    # Prices in Rupees

            self.checkout()
            if coupon:
                discount = self.apply_coupon(coupon)
                discounted_price = self.calculate_discounted_price(discount)
                print(f"Discount Applied: {discount * 100}%")
                # print(f"Discounted Price: ₹{discounted_price:.2f}")

        except ValueError as e:
            print(f"Error: {e}")

        else:
            print(f"Total Amount to pay: ₹{discounted_price:.2f}")
            print("Thank you for shopping!")
        finally:
            print("-------------------------")


if __name__ == "__main__":
    shopping_cart = ShoppingCart()

    # Example 1: Valid Shopping Session
    # shopping_cart.simulate_shopping("SAVE10")

    # # Example 3: Invalid Coupon Code
    shopping_cart = ShoppingCart()
    shopping_cart.simulate_shopping("INVALIDCOUPON")

    # # Example 4: Different Discount Coupon
    # shopping_cart = ShoppingCart()
    # shopping_cart.simulate_shopping("50OFF")
