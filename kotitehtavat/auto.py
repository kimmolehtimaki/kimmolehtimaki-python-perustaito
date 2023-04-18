# tehdään valikko
print("*********************************")
print("* 1 - Käynnistä auto")
print("* 2 - Aja autoa")
print("* 3 - Sammuta auto")
print("* 4 - Lopeta peli")
print("*********************************")

# koodi alkaa
numero = input("Syötä autolla ajamisen vaihe: ")

match numero:
    case "1":
        print("Muista kiinnittää turvavyö!")
    case "2":
        print("Pidä katse tiessä!")
    case "3":
        print("Voit nyt avata turvavyön!")
    case "4":
        print("Kiitos, hei!")
