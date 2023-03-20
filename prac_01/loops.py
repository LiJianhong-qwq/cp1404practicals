def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()


def a():
    for i in range(0, 101, 10):
        print(i, end=" ")
    print()


def b():
    for i in range(20, 0, -1):
        print(i, end=" ")
    print()


def c():
    numbers = int(input("Number of stars: "))
    for i in range(0, numbers, 1):
        print("*", end="")


def d():
    numbers = int(input("Number of stars: "))
    for i in range(1, numbers + 1, 1):
        print(i * "*")



d()