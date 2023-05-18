from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    user_choice = input(">>> ").upper()
    while user_choice != "Q" and user_choice != "C" and user_choice != "D" :
        print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").upper()

    while user_choice != "Q":
        if user_choice == "C":
            current_taxi = choose_taxi()

        if user_choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                pass

        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").upper()


def choose_taxi():
    print("Taxis available: ")
    for i, j in zip(taxis, range(0, len(taxis))):
        print(f"{j} - {i}")
    taxi_chosen = check_taxi_choice("Choose taxi: ")
    return taxi_chosen


def check_taxi_choice(prompt):
    choice = int(input(prompt))
    if 0 <= choice <= len(taxis) - 1:
        return taxis[choice]
    else:
        print("Invalid taxi choice")
        return None


main()
