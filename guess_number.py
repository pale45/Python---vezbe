import random

top_number = input("Unesite neki broj: ")

if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print("Molim vas unesite broj veci od 0 sledeci put! ")
        quit()

else:
    print("Molim vas unesite broj sledeci put! ")
    quit()

random_number = random.randint(0 , top_number)
guesses = 0

while True:
    guesses +=1
    user_guess = input ("Pogodi koji je broj ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("Unesite broj sleedeci put! ")
        continue
    
    if user_guess == random_number:
        print("Bravoo pogodio si! ")
        break
    elif user_guess > random_number:
            print("Probaj opet, blizu si ali moras malo manji broj :) ")

    else:
            print("Probaj opet, blizu si ali moras malo veci broj :) ")
        
print("Pogodio si iz", guesses, "pokusaja :)")

