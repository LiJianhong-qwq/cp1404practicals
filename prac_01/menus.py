name = input("Enter name: ")
while 1 != 0:
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>>").upper()
    while choice != "H" and choice != "G" and choice != "Q":
        print("Invalid choice")
        choice = input(">>>").upper()

    if choice == "H":
        print(f"Hello {name}")

    if choice == "G":
        print(f"Goodbye {name}")

    if choice == "Q":
        print("Finished.")
        break


