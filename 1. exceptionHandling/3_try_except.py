# Normal Try Except
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")


# Error Specific Try Except
# try:
#     num = 5
#     result = 10 / num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
