COLOR_LIST = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
              "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
              "antiquewhite": "#faebd7", "antiquewhite1": "	#ffefdb", "antiquewhite2": "#eedfcc"}

color_code = input("Enter color name: ").lower()
while color_code != "":
    if color_code in COLOR_LIST:
        print(COLOR_LIST[color_code])
    else:
        print("Invalid input")
    color_code = input("Enter color name: ").lower()
print("Good bye")









