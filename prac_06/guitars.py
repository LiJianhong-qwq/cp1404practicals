from prac_06.guitar import Guitar

guitar_list = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.90)]

print("My guitars!")
name = input("Name: ")
while name != "":
    year = input("Year: ")
    cost = float(input("Cost: "))
    name = Guitar(name, year, cost)
    print(name, "added.")
    guitar_list.append(name)
    print("\n")
    name = input("Name: ")

print("\n... snip ...\n")
print("These are my guitars:")

for i in range(0, len(guitar_list)):
    guitar_list[i].get_age()
    if guitar_list[i].is_vintage():
        print(f"Guitar {i + 1}: {guitar_list[i].name:>20} ({guitar_list[i].year}), "
              f"worth ${guitar_list[i].cost:10,.2f}(vintage)")
    else:
        print(f"Guitar {i + 1}: {guitar_list[i].name:>20} ({guitar_list[i].year}), worth ${guitar_list[i].cost:10,.2f}")

