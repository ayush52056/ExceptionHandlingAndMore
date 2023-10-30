import sys

# generator


def gen(n):
    for i in range(n):
        yield i


for i in gen(5):
    print(i)

x = gen(5)
print(next(x))
print(next(x))


def gen():
    yield 1
    print('Pause 1')
    yield 2
    print('Paused 2')
    yield 3
