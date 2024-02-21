# Projet Minitrice
Ce projet consiste à créer un programme qui permet de réaliser les 4 opérations arithmétiques élémentaires (+, -, * et /) entre deux nombres positifs.

- [Projet Minitrice](#projet-minitrice)
    - [Intoduction](#intoduction)
  - [Installation](#installation)
  - [Exécution](#exécution)
    - [Programme Minitrice](#programme-minitrice)
    - [Minitrice + Pipeline](#minitrice--pipeline)
  - [Génerator](#génerator)
    - [Programme](#programme)
    - [Gestion des erreurs:](#gestion-des-erreurs)
  - [Publication](#publication)
  - [Liens Utiles](#liens-utiles)

### Intoduction

>[!NOTE] 
> 
> Concernant ce projet, il a été réalisé par `4 étudiants`:
> | Nom | Prenom | Pseudo |
> | --- | --- | --- |
> | GRONDIN | Olivier | Kuma974 |
> | RAZAFINDRAIBE | Jerry | jerryalex15 |
> | JAVEL  | Camille Marcel| GodOfCode0X |
> | LENORMAND | Julien | Synepsy |

Comme énoncer dans le sujet du projet, nous avons cinq scénarios différents qui se base sur le programme Minitrice. Nous allons vous guider pas à pas pour faire fonctionner les scripts associés à chacun d'eux.

## Installation

Dans ce projet, nous allons avoir besoin de :

>[!TIP] 
>
> - [Python](https://www.python.org/downloads/) : site officiel.
> - [WLS2](https://www.ionos.fr/digitalguide/serveur/know-how/wsl2/) pour avoir accès à un terminal similaire à un terminal Unix sur Windows (Recommandation)
> - Comment installer python : [cliquez-moi](https://kinsta.com/fr/base-de-connaissances/installer-python/).


## Exécution 

### Programme Minitrice

Pour exécuter le programme, veuillez saisir `./minitrice` dans votre terminal Bash afin de lancer la minitrice.

Exemple de calcul :

```bash
$ ./minitrice
> 1+1
2
> 5*3
15
> 6-5
1
```
Pour quitter le programme, utilisez la combinaison de touches `Ctrl + D`.

Vous recevrez alors un message de fin élégant :
```bash
>
Fin des calculs :)
```

### Minitrice + Pipeline

**Utilisation avec la syntaxe de pipeline**
Vous pouvez également utiliser la syntaxe suivante :

```bash
$ echo "2+8" | ./minitrice
10
```
Cela vous affichera directement le résultat du calcul sans interaction supplémentaire. 

## Génerator

### Programme

Le programme generator génére des expressions calculable de façon aléatoire. Deux nombres choisi aléatoirement dans l'interval [1, 1000] sont utilisé pour générer les expressions. Ci-dessous un exemple :

```bash
$ ./generator 3
122+556
211/26
544/456
$
```
### Gestion des erreurs:

Pour gérer les différentes erreurs que peut produire le programme, nous avons utilisé le bloc suivant :
```python
try:
    /* Code */
except Exception as e:
    print(e)
```

Ce bloc sert à exécuter le code dans la partie try et s'il y a une erreur, on entre dans le bloc except et on affiche l'erreur en question dans la console.


## Publication

Ci-dessous en cliquant sur le lien, nous vous présentons une visualisation captivante de l'évolution de notre projet à travers le temps. 

Cette vidéo Gource offre un aperçu dynamique de l'activité de notre dépôt Git, mettant en lumière les contributions, les branches et les interactions au sein de notre code. Bonne visualisation. 
- [Gource](https://youtu.be/yhvncF9SdUI) : lien youtube

## Liens Utiles

>[!TIP]
>
>- [Python Random](https://docs.python.org/fr/3/library/random.html) : nous a permit de connaitre comment choisir aléatoirement dans une chaine de caractère en Python.
>- [Markdown](https://experienceleague.adobe.com/docs/contributor/contributor-guide/writing-essentials/markdown.html?lang=fr) : nous a aidé à embellir notre fichier `README.md`
>- [Installation python](https://kinsta.com/fr/base-de-connaissances/installer-python/) : ce site guide pas à pas pour installer python.