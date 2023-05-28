import wikipedia

search = input("What do you want to search?\n>>>")
while search != "":
    print(wikipedia.page(search))
    print(wikipedia.summary(search))









