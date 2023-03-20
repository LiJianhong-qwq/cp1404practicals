password = input("Password: ")
while len(password) < 6:
    print("Password too short")
    password = input("Password: ")

print(f"Your password is: {'*' * len(password)}")

