"""
Emails
Estimate: 20 minutes
Actual:   40 minutes
"""
EMAILS = {}


def main():
    email = input("Email: ")
    while email != "":
        separate_email = email.split("@")
        if "." in separate_email[0]:
            name = separate_email[0].split(".")
            user_choice = input(f"Is your name {name[0].title()} {name[1].title()}? (Y/n)").upper()
        else:
            name = separate_email[0].title()
            user_choice = input(f"Is your name {name.title()}? (Y/n)").upper()

        if user_choice == "Y" or user_choice == "":
            if "" in name:
                EMAILS[email] = "".join(i.title() for i in name.split())
            else:
                EMAILS[email] = " ".join(i.title() for i in name)
        else:
            real_name = input("Name: ")
            EMAILS[email] = real_name
        email = input("Email: ")
    for i in EMAILS:
        print(f"{EMAILS[i]}({i})")







main()





