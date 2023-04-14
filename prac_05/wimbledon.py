filename = "wimbledon.csv"
CHAMPIONS = {}
CHAMPIONS_COUNTRY = {}


def main():
    insert_champion()
    export_champion()
    display_country()


def display_country():
    print(f"These {len(CHAMPIONS_COUNTRY)} countries have won Wimbledon: ")
    print(", ".join(country for country in CHAMPIONS_COUNTRY))


def export_champion():
    for name in CHAMPIONS:
        print(f"{name}: {CHAMPIONS[name]}")


def insert_champion():
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for i in in_file.readlines()[1:]:
            i = i.split(",")
            if i[2] not in CHAMPIONS:
                CHAMPIONS[i[2]] = 1
                CHAMPIONS_COUNTRY[i[1]] = 0
            else:
                CHAMPIONS[i[2]] += 1


main()
