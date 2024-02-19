# Les importations nécessaires
import random
import sys

op = "+-*/"                                 # les différents opérateurs arithmétiques
try :                   # permet de gérer les erreurs
    nbArg = int(sys.argv[1])                # prend ce qui a dans $1 dans generator

    for i in range(nbArg):
        choix = random.choice(op)            #choix aléatoire d'opération arithmétique
        nbA = random.randint(1,1000)  # nbA choisit aléatoirement
        nbB = random.randint(1,1000)  # nbB choisit aléatoirement
        res = str(nbA) + choix + str(nbB)    # concaténation
        print(res)
except Exception as e:  # permet de gérer les erreurs
    print(e)