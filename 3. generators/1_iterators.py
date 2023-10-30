import sys

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(sys.getsizeof(x))
print(sys.getsizeof(range(1, 11)))

for element in x:
    print(element)
for i in range(1, 11):
    print(i)


# map Iterator
y = map(lambda i: i*2, x)
for i in y:
    print(i)

print(sys.getsizeof(list(y)))
print(sys.getsizeof(y))


# next()- next value in iteration through iterators.

print(next(y))
print(next(y))
print("for loop starts")

for i in y:
    print(i)

while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print('Done')
        break
