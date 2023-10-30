# Define a decorator function for logging
def log_function_call(func):
    def wrapper(*args, **kwargs):
        # Log the function name
        print(f"Calling function: {func.__name__}")
        # Log the function arguments
        if args:
            print(f"Arguments: {args}")
        if kwargs:
            print(f"Keyword Arguments: {kwargs}")
        try:
            # Call the original function
            result = func(*args, **kwargs)
            print(f"Function {func.__name__} returned: {result}")
            return result
        except Exception as e:
            print(f"Exception caught by decorator: {str(e)}")
            return
    return wrapper
# Apply the decorator to a function


@log_function_call
def add(a, b):
    return a + b


@log_function_call
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@log_function_call
def greet(name):
    return f"Hello, {name}!"


@log_function_call
def power(base, exponent):
    return base ** exponent


@log_function_call
def example_function(a, b, c=0, d=0):
    return a + b + c + d


# Test the decorated functions
result1 = add(5, 3)
result4 = divide(8, 2)
result5 = greet("Alice")
result6 = power(2, 3)
result = example_function(1, 2, c=3, d=4)
result2 = divide(10, 0)

print(f"Final result of add function: {result1}")
print(f"Final result of divide function (result1): {result4}")
print(f"Final result of divide function (result2): {result2}")
print(f"Final result of greet function: {result5}")
print(f"Final result of power function: {result6}")
print(f"Final result of example_function: {result}")
