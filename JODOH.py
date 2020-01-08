# primbon jodoh
import random

print("Welcome to JODOHKU KAU KAH ITU ?")
loop = True
while loop:
    cowo = input("Masukkan nama cowomu : ")
    cewe = input("Masukkan nama cewemu : ")

    print("<3 <3 <3 <3 <3 <3 <3 <3 <3")

    print("Nama cowo: ", cowo)
    print("Nama cewe: ", cewe)
    Setuju = input(" Namanya udah bener nii ? y/n = ")
    if Setuju == 'y':
        loop = False

    zodiakcowo = input("Masukkan zodiak cowomu : ")
    zodiakcewe = input("Masukkan zodiak cewemu : ")

    print("<3 <3 <3 <3 <3 <3 <3 <3 <3")

    print("Zodiak cowo: ", zodiakcowo)
    print("Zodiak cewe: ", zodiakcewe)
    Setuju = input(" Zodiaknya udah bener nii ? y/n = ")
    if Setuju == 'y':
        loop = False

    umurcowo = int(input("Berapa umur cowomu ?"))
    umurcewe = int(input("Berapa umur cewemu ?"))

    print("<3 <3 <3 <3 <3 <3 <3 <3 <3")

    print("Umur cowo : ", umurcowo)
    print("Umur cewe : ", umurcewe)
    total = int((umurcewe + umurcowo) % 2)

match = (random.randrange(0, 100))
if total == 1:
    print(match + 5)
else:
    print(match - 5)

print("matchmate ", match, "%")
if match > 80:
    print("Ndang Rabi")
elif match > 60:
    print("pikir-pikir")
elif match > 40:
    print("Yakin")
elif match > 20:
    print("Cari lagi")
elif match > 0:
    print("putusin")
