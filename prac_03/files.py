


def a():
    out_file = open("name.txt", 'w')
    name = input("What is your name? ")
    print(name, file=out_file)
    out_file.close()


def b():
    out_file = open("name.txt", 'r')
    name = out_file.read()
    print(f"Your name is {name}")
    out_file.close()


def c():
    total = 0
    out_file = open("numbers.txt", 'r')
    for i in out_file.readlines(3):
        total += int(i)
    print(total)

    out_file.close()


def d():
    total = 0
    ANY_NUMBER = 0

    out_file = open("numbers.txt", 'r')
    for i in out_file.readlines(ANY_NUMBER):
        total += int(i)
    print(total)


d()





