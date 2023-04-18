vuosi = int(input("Syötä vuosi: "))

if vuosi < 1753 and 1753 % 4 == 0:
    print("On karkausvuosi")
if vuosi % 400 == 0:
    print("On karkausvuosi")

elif vuosi % 4 == 0 and vuosi % 100 != 0:
    print("On karkausvuosi")

else:
    print("Ei ole karkausvuosi")
