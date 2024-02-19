# Importation de bibliothèque et de modules
import os
import sys
# os.isatty() : fonction qui vérifie si un descripteur de fichier est associé à un terminal interactif.
#   - 0 : pour entrée standard
#   - 1 : pour sortie standard
#   - 2 : pour sortie d'erreur

# Les données suis entrée par l'utilisateur
if os.isatty(0):
    # Gére la fonction Ctrl+D de notre clavier avec le bloc try - except
    try:
        while True:     #tant qu'on n'appuie pas Ctrl+D, ça tourne en boucle
            print(">", end=" ")
            commande = input()      # Demande à l'utilisateur de taper une expression tel que 3 + 3
            res = eval(commande)    #Evalue la chaine de caractères python en tant qu'expression
            print(res)              # Affiche l'expression évaluée
    except EOFError:
        print()                     #Saute une ligne avant d'afficher notre message
        print("Fin des calculs :)")
else:
    # Les données qui sont transmises via un pipe
    for entree in sys.stdin:
        print(round(eval(entree),2))     #Affiche directement le calcul
        