import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)


slow_function()

# Class Decorators
# class TimingDecorator:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         import time
#         start_time = time.time()
#         result = self.func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#         return result


# @TimingDecorator
# def slow_function():
#     import time
#     time.sleep(2)
#     print("Function executed.")


# slow_function()
