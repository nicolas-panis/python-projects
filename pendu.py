from random import*
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
user = []
# print(myListDico[valeur])
for i in range(len(result)):
    user.append("_")
for j in user:
    print(j, end = " ")
print("")

vie = 10
while vie > 0:
    test = input("Rentrer une lettre: ")

    if test in result:
        for l in range(len(user)):
            for k in range(len(result)):
                if result[k] == test:
                    user[k] = test
        for j in user:
            print(j, end = " ")
    else: 
        vie = vie - 1
        for j in user:
            print(j, end = " ")
    
    print("")
    print("Nombre de vie restantes: " + str(vie))
