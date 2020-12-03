from random import *
def allumettes():
    a = 21
    while a > 0: #tant que a est plus que 0
        retireint = int(input("Combien en prenez-vous ?"))
        if retireint <= 3 and retireint >= 1 and retireint <= a :
            a = a-retireint

            print("il y a", a, "allumettes")
        else :
            print("Ne pas prendre plus d'allumettes qu'il ne reste ou plus de 3.. Votre tour saute...")

        if a == 0 :
            print("Vous avez perdu")
            break


        if a <= 3 :
            retirepc1 = randint(1, a)
            a = a-retirepc1
            print("le PC a joué, il y a", a, "allumettes")

        if a > 3 :
            retirepc2 = randint(1, 3)
            a = a-retirepc2

            print("le PC a joué, il y a", a, "allumettes")

        elif a == 0 :
            print("Vous avez gagné")
            break
