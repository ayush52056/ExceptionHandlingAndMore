import sys

x = range(1, 11)

print(x)
print(next(x))  # notice the error here that range object is not iterator.and to make it work we need to add one function called iter()
# if we want to get iterator from x, we need to use this function to use.

# print(next(iter(x)))


for i in x:
for i in iter(x):
