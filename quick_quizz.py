##Kviz znanja - Python vezba

print("Dobrodosli u brzi kviz znanja!")

playing = input ("Da li ste spremni za pocetak? ")

if playing.lower() != "da":
    quit()

print("Super! Ajde da pocnemo :) ")
score = 0

answer = input ("Koji je glavni grad Norveske? ")

if answer.lower() == "oslo":
    print("Tacan odgovor!")
    score += 1
else:
    print('Netacan odgovor :( ')



answer = input ("Koliko iznosi broj Pi (dve decimale)? ")

if answer == "3.14":
    print("Tacan odgovor!")
    score += 1
else:
    print('Netacan odgovor :( ')



answer = input ("Na koliko metara visine se nalazi obruc u kosarci (dve decimale)? ")

if answer == "3.05":
    print("Tacan odgovor!")
    score += 1
else:
    print('Netacan odgovor :( ')



answer = input ("Kako se zove poznati muzej u Parizu? ")

if answer.lower() == "luvr":
    print("Tacan odgovor!")
    score += 1
else:
    print('Netacan odgovor :( ')



answer = input ("Posle koliko godina se slavi zlatna svadba? ")

if answer == "50":
    print("Tacan odgovor!")
    score += 1
else:
    print('Netacan odgovor :( ')


print("Bravo tacno si odgovorio na " + str(score) + " pitanja! " )
print("Procenat tacnih odgovora je: " +str((score)/5 *100) + "%")
input("Klikni Enter za izlazak: ")
