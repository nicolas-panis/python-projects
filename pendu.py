from random import*
diff = input("Choisissez une difficulté (débutant, intermédiaire, expert): ")

myListDico = []

with open('dico_france.txt','r') as file:
    # reading each line    
    for line in file:
        # print(line, end= " ")
        for word in line.split():
            myListDico.append(word)

# print(myListDico)
valeur = randint(0, len(myListDico))
result = myListDico[valeur]
print(result)

affichageUser = []
for i in range(len(result)):
    affichageUser.append("_")
for j in affichageUser:
    print(j, end = " ")
print("")

vie = 0
match diff:
    case "débutant":
        vie = 10
    case "intermédiaire":
        vie = 7
    case "expert":
        vie = 3

under = "_"
myListLetter = []
while vie > 0:
    proposition = input("Rentrer une lettre: ")
    myListLetter.append(proposition)
    if proposition in result:
        for l in range(len(affichageUser)):
            for k in range(len(result)):
                if result[k] == proposition:
                    affichageUser[k] = proposition
        for j in affichageUser:
            print(j, end = " ")
    else: 
        vie = vie - 1
        for j in affichageUser:
            print(j, end = " ")
    if under not in affichageUser:
        print("\nVous avez gagné")
        exit()
    
    if diff == "débutant" or diff == "intermédiaire":
        print("\nLettres proposées: ", end = "")
    for i in myListLetter:
        print(i, end = " ")
    print("")
    print("Nombre de vie restantes: " + str(vie))
print("Vous avez perdu")
