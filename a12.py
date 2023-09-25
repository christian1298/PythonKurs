db = {
    1000 : "Kartoffeln",
    1020 : "Gurken",
    720 : "Bananen",
    702 : "Kiwis",
    5000 : "Schokolade",
    5010 : "Kartoffelchips"
}

while True:
    t = input("Input: ")
    print(db.get(int(t), "Nicht Vorhanden"))