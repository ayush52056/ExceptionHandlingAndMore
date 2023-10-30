# Try Except and else block
try:
    num = 5
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print("Result:", result)