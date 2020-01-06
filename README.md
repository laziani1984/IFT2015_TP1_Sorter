# IFT2015_TP1_Sorter

Sorter.pdf




IFT-2015 Structures de données
Professeur: François Major
Travail pratique Sorter : 

1.
Créer une classe "Sorter", qui prendra une liste de nombres et la con-
servera en attribut. La classe "Sorter" aura une méthode "getSorted-
Data()", qui triera la liste de nombres et qui retournera un tuple con-
tenant à la position 0 une copie de la liste ordonnée (vous pourrez
prendre la fonction "sort" de python pour l’instant) et à la position 1
le temps, en secondes, requis pour effectuer le tri dans une string.
Vous pouvez « import time » en haut du fichier pour utiliser un objet
qui va mesurer le temps, je vous laisse voir comment ça marche. C’est
assez facile et ça été vu en classe.
Par exemple, si votre classe "Sorter" est construite avec la liste [5,7,1,8,0,3,5],
la fonction "getSortedData()", si elle prend 10sec, devrait retourner
([0,1,3,5,5,7,8], str(10.0))
2.
Créer une fonction "getUniqueValueList()" qui va retourner à l’utilisateur
un "set" contenant tous les nombres présents dans la liste mais sans
les doublons.
Par exemple, si votre classe "Sorter" est construite avec la liste [5,7,1,8,0,3,5],
la fonction "getUniqueValueList()", si elle prend 10sec, devrait re-
tourner un set contenant les nombres 0 , 1 , 3 , 5 , 7 , 8 .
3.
Créer une fonction "getAlphabetMappingDecode(word)" qui va tout
d’abord trier la liste puis assigner les nombres à leurs lettres de l’alphabet
dans un dictionnaire. Par exemple, si on a la liste [1,2,3,8], le diction-
naire sera {A :1, B :2, C :3, D :8}. Vous pouvez ignorez les majuscules.
Si la liste a plus de 26 nombres, vous recommencez à la lettre A,
et ainsi de suite jusqu’à avoir épuisé la liste.
Par la suite, prenez chaque lettre du paramètre « word » et faites
une liste de listes avec les valeurs numériques correspondantes. Cette
liste est la valeur de retour de la fonction. Par exemple, si le mot est 2




