
import timeit
from time import time
import string

"""""   
        Nom d'auteur: Wael ABOU ALI.
        Numéro de matricule: 20034365.
        Créé en:    09-30-2019.
        Version:    v1.0   
        But:        Cette classe est créée pour faire une comparaison entre 
                    les différents algorithmes en calculant leurs vitesses 
                    d'exécution par rapport au temps consommé.
                    La classe contient plusieurs algorithmes d'exécution
                    comme : le sort standard du python, bubbleSort et 
                    MergeSort.
                    Aussi, cette classe présente des méthodes pour avoir la
                    liste originale(getData), avoir un set au lieu d'une
                    liste(getUniqueValue) et transformer une liste originale
                    en dictionnaire et la liste passée en paramétre à la 
                    méthode va suivre les règlements de ce dictionnaire.
        Méthodes:   1. __init__(constructeur).
                    2. getData(retourne la liste créée par le constructeur
                    (self.__list_nums)).
                    3. getSortedData(retourne une copie ordonnée de la 
                    liste à l'aide de la méthode sort du python).
                    4. getUniqueValueList(retourne une copie de la liste sous
                    forme d'un set ordonnè).
                    5. getAlphabetMappingDecode(retourne la chaîne des 
                    caractères passèe en paramètre sous forme d'une liste
                    des listes contenant des valeurs numériques. Ces valeurs
                    numériques sont les valeurs dans la dictionnaire formée 
                    à partir de la liste source dont les valeurs sont les 
                    valeurs de la liste et les clés sont les positions de ces
                    valeurs sous forme des alphabets(index 0 sur la liste_src 
                    représente A, 1 ---> B, et ainsi de suite.
                    6. getSortedDataSafe(retourne une copie triée de la liste 
                    originale à l'aide de BubbleSorte).
                    7. getSortedDataSafeAndFast(retourne une copie triée de la 
                    liste originale à l'aide de MergeSort).
                    8. MergeSort(une méthode récursive appelée dans 
                    getSortedDataSafeAndFast qui s'occupe de trier la copie de
                    la liste en utilisant MergeSort).
"""""


class Sorter(object):

    def __init__(self, list_nums):
        self.__list_nums = list_nums

    def getData(self):
        return self.__list_nums

    def getSortedData(self):
        # On a deux choix(implementation du python, algorithme d'insertion).
        # 1. Méthode implementée dans python:
        # ==================================
        liste_temp = self.__list_nums[:]
        return sorted(liste_temp)

        # 2. Algorithme d'insertion:
        # ==========================
        # sorted_array = []
        # for a in self.__list_nums:
        #     # Loop backwards through sorted_array
        #     for i, b in reversed(list(enumerate(sorted_array))):
        #         if a > b:
        #             sorted_array.insert(i + 1, a)  # Insert a to the right of b
        #             break
        #     else:
        #         # a is less than all numbers in sorted_array
        #         sorted_array.insert(0, a) # Add a to beginning of list
        # return sorted_array

    # Retourne un ensemble au lieu d'une liste.
    def getUniqueValueList(self):
        liste_temp = self.__list_nums[:]
        return sorted(set(liste_temp))

    # mon_dict sera notre dictionnaire qui contiendra(clé(alphabet[i] :
    # valeur(un item de la liste originale[i]) en respectant que la liste
    # ne dépasse pas les 26 lettres qui représentent les alphabets.
    # Puis, on ajoute la valeur qui correspond à la lettre(clé) dans mon_dict
    # dans une liste temporaire qui sera retournée.
    def getAlphabetMappingDecode(self, word):
        mon_dict = {}
        for i in range(len(self.__list_nums)):
            mon_dict.setdefault(string.ascii_uppercase[i % 25], []).append(self.__list_nums[i])
        liste_temp = []
        for char in word:
            liste_temp.append(mon_dict.get(char))
        return liste_temp

    # BubbleSort.
    def getSortedDataSafe(self):
        liste_temp = self.__list_nums[:]  # Une copie de la liste originale.
        last_index = len(self.__list_nums) - 1  # dernière position.
        while last_index > 0:
            for i in range(last_index):
                a, b = liste_temp[i], liste_temp[i + 1]  # deux indexes consécutifs.
                if a > b:
                    liste_temp[i], liste_temp[i + 1] = b, a  # On échange les positions.
            last_index -= 1  # On a changé la position d'un nouveau item.
        return liste_temp

    # MergeSort.
    def getSortedDataSafeAndFast(self):
        liste_temp = self.__list_nums[:]
        return self.mergeSort(liste_temp)

    # Méthode récursive de MergeSort.
    def mergeSort(self, liste_temp):
        if len(liste_temp) > 1:
            milieu = len(liste_temp) // 2  # point milieu.
            partie_g = liste_temp[:milieu]  # partie gauche.
            partie_d = liste_temp[milieu:]  # partie droite.
            Sorter.mergeSort(self, partie_g)  # appel récursif(partie gauche).
            Sorter.mergeSort(self, partie_d)  # appel récursif(partie droite).
            i = j = k = 0
            while i < len(partie_g) and j < len(partie_d):
                if partie_g[i] < partie_d[j]:  # si élément à la position i dans
                    liste_temp[k] = partie_g[i]  # la partie gauche < celui à partie
                    i += 1  # droite ---> je l'ajoute à liste_temp.
                else:  # Si l'inverse.
                    liste_temp[k] = partie_d[j]
                    j += 1
                k += 1
            while i < len(partie_g):  # S'il y en a des éléments qui restent à la
                liste_temp[k] = partie_g[i]  # partie gauche, je les ajoutent et j'incrémente.
                i += 1
                k += 1
            while j < len(partie_d):  # Même chose pour partie droite.
                liste_temp[k] = partie_d[j]
                j += 1
                k += 1
        return liste_temp


"""""   
        Nom d'auteur: Wael ABOU ALI.
        Numéro de matricule: 20034365.
        Créé en:    09-30-2019.
        Version:    v1.0   
        But:        C'est la classe main du programme. Cette classe est responsable 
                    de tester les méthodes importées de la classe Sorter. Elle esr
                    divisée en six parties(six questions).
                    1ère: Sort normal(algorithme d'insertion en alternatif(décoché)).
                    2ième: Liste ---> set.
                    3ième: Liste ---> dictionnaire <--- liste(en paramètre).
                    4ième: Tester l'algorithme de BubbleSort.
                    5ième: Tester l'algorithme de MergeSort.
                    6ième: Comparaison entre les deux algorithmes(par rapport au
                     temps d'exécution).

************************************************************************************** 
||  Note : - j'ai utilisé l'importation de time et timeit. Timeit donne un calcul   ||
||  de temps plus précis pour triage des petites listes et c'est pour cette raison  ||
||  que je l'ai utilisé.                                                            ||
||  - J'ai coché le calcul de temps comme en commentaire pour les questions 2,3,4,5.||
||  Si vous voulez voir les calculs de temps, il suffit de les déchocher seulement. ||
**************************************************************************************

"""""


def main():

    # Question 1
    # ==========

    """"" Créer une classe "Sorter", qui prendra une liste de nombres et la 
    conservera en attribut. La classe "Sorter" aura une méthode "getSorted-
    Data()", qui triera la liste de nombres et qui retournera un tuple con-
    tenant à la position 0 une copie de la liste ordonnée (vous pourrez
    prendre la fonction "sort" de python pour l’instant) et à la position 1
    le temps, en secondes, requis pour effectuer le tri dans une string.
    Vous pouvez « import time » en haut du fichier pour utiliser un objet
    qui va mesurer le temps, je vous laisse voir comment ça marche. C’est
    assez facile et ça été vu en classe.
    Par exemple, si votre classe "Sorter" est construite avec la liste 
    [5,7,1,8,0,3,5], la fonction "getSortedData()", si elle prend 10sec, 
    devrait retourner ([0,1,3,5,5,7,8], str(10.0)). """""

    print("\n***** Question 1 : *****\n------------------------")
    # 1er cas
    # -------
    liste_src1 = Sorter([5, 7, 1, 8, 0, 3, 5])
    temps_debut = time()
    time_before = timeit.default_timer()
    tri_liste1 = liste_src1.getSortedData()
    temps_fin = time()
    time_after = timeit.default_timer()
    # -------------------------------------------------------
    # print orders :
    # --------------
    print("liste_src1:", liste_src1.getData())
    print("avec timeit: (", tri_liste1, "), str(",
          (time_after - time_before), ")")
    print("avec time:(", tri_liste1, "), str(",
          (temps_debut - temps_fin), ")")

    # 2ième cas
    # ---------
    liste_src2 = Sorter([5, 7, 1, 8, 0, 3, 5, 10, 1, 22, 45, 12, 11, 1001,
                         21, 32, 29])
    temps_debut = time()
    time_before = timeit.default_timer()
    tri_liste2 = liste_src2.getSortedData()
    temps_fin = time()
    time_after = timeit.default_timer()
    # --------------------------------------------------------------------
    # print orders :
    # --------------
    print("liste_src2:", liste_src2.getData())
    print("avec timeit: (", tri_liste2, "), str(",
          (time_after - time_before), ")")
    print("avec time:(", tri_liste2, "), str(",
          (temps_debut - temps_fin), ")")

    print("\n\t\t**********************************************************\n")

    # =========================================================================
    # Question 2
    # ==========

    """"" 
    Créer une fonction "getUniqueValueList()" qui va retourner à 
    l’utilisateur un "set" contenant tous les nombres présents dans la 
    liste mais sans les doublons.
    Par exemple, si votre classe "Sorter" est construite avec la liste 
    [5,7,1,8,0,3,5], la fonction "getUniqueValueList()", si elle prend 10sec, 
    devrait retourner un set contenant les nombres 0 , 1 , 3 , 5 , 7 , 8 
    """""

    print("***** Question 2 : *****\n------------------------")
    # 1er cas
    # -------
    temps_debut = time()
    time_before = timeit.default_timer()
    tri_set1 = liste_src1.getUniqueValueList()
    temps_fin = time()
    time_after = timeit.default_timer()
    # -------------------------------------------------------
    # print orders :
    # --------------
    print("liste_src1:", liste_src1.getData())
    print("tri_set1:", tri_set1)
    print("avec timeit: (", tri_set1, "), str(", (time_after - time_before), ")")
    print("avec time:(", tri_set1, "), str(", (temps_debut - temps_fin), ")")

    # 2ième cas
    # ---------
    temps_debut = time()
    time_before = timeit.default_timer()
    tri_set2 = liste_src2.getUniqueValueList()
    temps_fin = time()
    time_after = timeit.default_timer()
    # -------------------------------------------------------
    # print orders :
    # --------------
    print("liste_src2:", liste_src2.getData())
    print("tri_set1:", tri_set2)
    print("avec timeit: (", tri_set2, "), str(", (time_after - time_before), ")")
    print("avec time:(", tri_set2, "), str(", (temps_debut - temps_fin), ")")
    print("\n\t\t**********************************************************\n")
    # =========================================================================
    # Question 3
    # ==========

    """"" Créer une fonction "getAlphabetMappingDecode(word)" qui va tout
    d’abord trier la liste puis assigner les nombres à leurs lettres de 
    l’alphabet dans un dictionnaire. Par exemple, si on a la liste [1,2,3,8], 
    le dictionnaire sera {A :1, B :2, C :3, D :8}. Vous pouvez ignorez 
    les majuscules.
    Si la liste a plus de 26 nombres, vous recommencez à la lettre A, et ainsi 
    de suite jusqu’à avoir épuisé la liste.
    Par la suite, prenez chaque lettre du paramètre « word » et faites
    une liste de listes avec les valeurs numériques correspondantes. 
    Cette liste est la valeur de retour de la fonction. Par exemple, si le mot 
    est « abc » et le dictionnaire {A :1, B :2, C :3, D :8}, vous retournez 
    [[1],[2],[3]]. 
    Considérez que les lettres majuscules et minuscules sont les mêmes. """""

    print("***** Question 3 : *****\n------------------------")
    # 1er cas
    # -------
    liste_src3 = Sorter([1, 2, 3, 8])
    # temps_debut = time()
    # time_before = timeit.default_timer()
    liste_vals1 = liste_src3.getAlphabetMappingDecode("ABC")
    # temps_fin = time()
    # time_after = timeit.default_timer()
    # -------------------------------------------------------
    # print orders :
    # --------------
    # print("liste_src3:", liste_src3.getData())
    print("liste_vals1:", liste_vals1)
    # print("avec timeit: (", liste_vals1, "), str(", (time_after - time_before), ")")
    # print("avec time:(", liste_vals1, "), str(", (temps_debut - temps_fin), ")")

    # 2ième cas
    # ---------
    liste_src4 = Sorter([5, 7, 1, 8, 0, 3, 5, 10, 1, 22, 45, 12, 11, 1001, 21,
                         32, 29, 28, 27, 26, 25, 24, 23, 38, 37, 36, 35, 34,
                         33, 32, 31, 30, 50, 49, 48, 47, 46, 45, 44, 43, 42,
                         41, 40, 39, 60, 61, 62, 63, 64, 65, 80, 79, 78, 77,
                         76, 75, 74, 73])
    # temps_debut = time()
    # time_before = timeit.default_timer()
    liste_vals2 = liste_src4.getAlphabetMappingDecode("HELLOWORLD")
    # temps_fin = time()
    # time_after = timeit.default_timer()
    # -------------------------------------------------------
    # print orders :
    # --------------
    # print("liste_src4:", liste_src4.getData())
    print("liste_vals2:", liste_vals2)
    # print("avec timeit: (", liste_vals2, "), str(", (time_after - time_before), ")")
    # print("avec time:(", liste_vals2, "), str(", (temps_debut - temps_fin), ")")
    print("\n\t\t**********************************************************\n")
    # ==============================================================================
    # Question 4
    # ==========

    """"" On a récemment découvert qu’un gouvernement avait mis la main
    sur la librairie de Python et utilisait sa fonction "sort()" pour trans-
    mettre les données des utilisateurs dans le but de faire de l’espionnage !
    Apprenant cette situation, vous avez comme mandat de créer la fonc-
    tion "getSortedDataSafe()" qui aura le même comportement que "get-
    SortedData" mais avec votre propre implémentation de "sort". Prenez
    un BubbleSort pour cette exercice. 
    Pas de panique ! Cette situation est bien sûr fictive! """""

    print("***** Question 4 : *****\n------------------------")
    # 1er cas
    # -------
    # temps_debut = time()
    # time_before = timeit.default_timer()
    print("liste_src1:", liste_src1.getData())
    tri_liste1 = liste_src1.getSortedDataSafe()
    print("liste_src1 triée avec bubbleSort:", tri_liste1)
    # temps_fin = time()
    # time_after = timeit.default_timer()
    # -------------------------------------------------------
    # print orders :
    # --------------
    # print("avec timeit: (", tri_liste1, "), str(", (time_after - time_before), ")")
    # print("avec time:(", tri_liste1, "), str(", (temps_debut - temps_fin), ")")

    # 2ième cas
    # ---------
    # temps_debut = time()
    # time_before = timeit.default_timer()
    print("liste_src2:", liste_src2.getData())
    tri_liste2 = liste_src2.getSortedDataSafe()
    print("liste_src1 triée avec bubbleSort:", tri_liste2)
    # temps_fin = time()
    # time_after = timeit.default_timer()
    # -------------------------------------------------------
    # print orders :
    # --------------
    # print("avec timeit: (", tri_liste2, "), str(", (time_after - time_before), ")")
    # print("avec time:(", tri_liste2, "), str(", (temps_debut - temps_fin), ")")

    print("\n\t\t**********************************************************\n")
    # =========================================================================
    # Question 5
    # ==========

    """"" Les données des utilisateurs sont maintenant protégées (yé!), 
    mais ils se plaignent que votre algorithme de tri est trop lent. 
    Ah ces usagers! Jamais contents !
    En effet, le "bubblesort" à une complexité en temps dans O(n2). 
    Vous pouvez facilement trouver un algorithme qui fera le boulot en temps
    dans O(nlogn): MergeSort.
    Vous devez donc créer la fonction "getSortedDataSafeAndFast()" qui
    utilisera cet algorithme. Faites une implémentation récursive. """""

    print("***** Question 5 : *****\n------------------------")
    # 1er cas
    # -------
    # temps_debut = time()
    # time_before = timeit.default_timer()
    print("liste_src1:", liste_src1.getData())
    tri_liste1 = liste_src1.getSortedDataSafeAndFast()
    print("liste_src1 triée avec mergeSort:", tri_liste1)
    # temps_fin = time()
    # time_after = timeit.default_timer()
    # -------------------------------------------------------
    # print orders :
    # --------------
    # print("avec timeit: (", tri_liste1, "), str(", (time_after - time_before), ")")
    # print("avec time:(", tri_liste1, "), str(", (temps_debut - temps_fin), ")")

    # 2ième cas
    # ---------
    # temps_debut = time()
    # time_before = timeit.default_timer()
    print("liste_src2:", liste_src2.getData())
    tri_liste2 = liste_src2.getSortedDataSafeAndFast()
    print("liste_src2 triée avec mergeSort:", tri_liste2)
    # temps_fin = time()
    # time_after = timeit.default_timer()
    # -------------------------------------------------------
    # print orders :
    # --------------
    # print("avec timeit: (", tri_liste2, "), str(", (time_after - time_before), ")")
    # print("avec time:(", tri_liste2, "), str(", (temps_fin - temps_debut), ")")
    print("\n\t\t**********************************************************\n")
    # =========================================================================
    # Question 6
    # ==========

    """"" Les clients se plaignent toujours et ont indiqué à votre patron que
    cette nouvelle fonction n’est pas plus rapide que l’ancienne.
    Pour éviter la colère de votre patron, créer la fonction "getSortTimes()"
    qui mesurera les vitesses de tri des 2 fonctions et qui retournera dans un
    tuple le temps d’exécution et le nom de la méthode dans une "string".
    De cette façon, vous pourrez montrer à votre patron que votre nouvel
    algorithme en temps réel est plus efficace. """""

    print("***** Question 6 : *****\n------------------------")
    liste_src5 = Sorter(list(reversed(range(0, 1000))))
    start_merge = time()
    liste_src5.getSortedDataSafeAndFast()
    end_merge = time()
    start_bubble = time()
    liste_src5.getSortedDataSafe()
    end_bubble = time()
    # -------------------------------------------------------
    # print orders :
    # --------------
    print("(\"getSortedDataSafeAndFast() ---> MergeSort : str(",
          (end_merge - start_merge), ")\",\n \"getSortedDataSafe() ---> BubbleSort : str(",
          (end_bubble - start_bubble), ")\")")
    print("\n\t\t**********************************************************\n")
    # =========================================================================


if __name__ == "__main__":
    main()
