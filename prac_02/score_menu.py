def main():
    score = 0
    while 1 == 1:
        print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input(">>>").upper()
        check_choice(choice)
        if choice == "Q":
            print("Farewell")
            break
        if choice == "G":
            number = int(input("Enter your score: "))
            score = number
            check_number(number)
        if choice == "P":
            if score == 0:
                print("You are still not enter the score. ")
            else:
                print(calculate_result(int(score)))
        if choice == "S":
            print('*' * score)


def check_number(number):
    while number > 100 or number < 0:
        print("Invalid input")
        number = int(input("Enter your score: "))


def check_choice(choice) :
    while choice != "G" and choice != "P" and choice != "S" and choice != "Q":
        print("Invalid input")
        print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input(">>>").upper()


def calculate_result(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()


