import random

user_wins = 0
computer_wins = 0
options = ["papir", "kamen", "makaze"]
while True:
    user_input= input("Upisite Papir/Kamen/Makaze ili Q za izlazak: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue


    random_number = random.randint(0 , 2)
    #papir = 0      kamen = 1     makaze = 2
    computer_pick = options[random_number]
    print("Kompjuter je izabrao", computer_pick + ".")


    if user_input == "kamen" and computer_pick == "makaze":
        print("Cestitamo pobedili ste! ")
        user_wins += 1

    elif user_input == "papir" and computer_pick == "kamen":
        print("Cestitamo pobedili ste! ")
        user_wins += 1

    elif user_input == "makaze" and computer_pick == "papir":
        print("Cestitamo pobedili ste! ")
        user_wins += 1

    else:
        print("Kompjuter je pobedio! ")
        computer_wins += 1


print("Pobedili ste", user_wins, "puta! ")
print("Kompjuter je pobedio", computer_wins, "puta! ")

print("Pozdrav!")

