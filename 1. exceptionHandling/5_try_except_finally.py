try:
    num = 5
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
finally:
    print("This is finally block and will run everytime")
