import random

numbers = []

pick_times = int(input("How many quick picks? "))
for i in range(pick_times):
    for q in range(6):
        randoms_number = random.randint(1, 45)
        while randoms_number in numbers:
            randoms_number = random.randint(1, 45)
        numbers.append(randoms_number)
    print(" ".join(f"{number:2}".format(number) for number in sorted(numbers))) # PyCharm said it error but still working good
    numbers.clear()









