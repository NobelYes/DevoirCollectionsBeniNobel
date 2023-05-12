if __name__=="__main__":
    # Question 1
    
        marque_vehicules=['Honda','Toyota','Mercedes','ferrari','lambourghini','Mazda','Citroen','Audi','BMW','Peugeot']
        
        # 1 affichage des elements de la liste
        print(marque_vehicules)
        
        # 2 changer le contenu de l'element numero 5
        marque_vehicules[4]='Tesla'
        # affichage de la liste actualiser
        print(marque_vehicules)
        
        # 3  creation d'une liste contenant des elements de 'marque_vehicules' dont les valeurs continnent 'a'
        new_marque=[]
        for i in marque_vehicules:
            if 'a' in i:
             new_marque.append(i)
        print(new_marque)
        
        # 4  ajout d'un elt a la fin
        new_marque.append('Fiat')  
        
        # verification dans la liste
        print(new_marque)
        
        # 5  Ajout d'un elt à l'index num 2
        new_elt_on_index_2 = 'Lamborgini'
        new_marque.insert(2, new_elt_on_index_2)
        print(new_marque)
        
        # 6 Suppression de l' élément no 3
        num = 3
        i = num - 1  #L'index de l'elt num 3 sera égal à 2 .
        del new_marque[i] #Suppression de l'élt à l'index 2 .
        print(new_marque)
        
        # 7 Suppression l'élément à l’index numéro 2
        del new_marque[2]
        print(new_marque)
        
        # 8 Ordonner la liste 
        new_marque.sort(reverse = False)
        print(new_marque) #Affichage de la liste pour la vérification
        
        # 9 Afficher la liste au sens inverse (décroissant)
        new_marque.reverse() #inverser les "élts de la liste au sens inverse
        print(new_marque) #affichage de la liste
        
        # 10 Vider la liste 
        new_marque.clear() #vider la liste avec la fonction clear
        
        # 11 Suppression de lq liste
        del new_marque
        
        
    # Question II. 
    
        tuple = 1,5,7,3,8,3,15,36,2,6 #initialisation de la tuple
        print(tuple)
        
        # 1 Afficher le nombre de fois que la valeur 3 apparait dans la tuple
        print("Le chiffre 3 apparait ",tuple.count(3)," fois dans la liste")

        # 2 Afficher le contenu de l'élément numéro 5
        print("L'élément numéro 5 de la tuple est :", tuple[4]) #Car il se trouve à l'index no 4 !
        
        # 3 Ordonner la tuple
        tuple=sorted(tuple)
        print(tuple) #Affichage de la tuple pour la vérification
        
        # 4 Ajouter un élément à la fin de la tuple
        tuple.append(20)
        print(tuple) #Affichage de la tuple pour la vérification
        
        # 5 Ajouter un élément à l’index numéro 3
        tuple.insert(3, 24)
        print(tuple) #Affichage de la tuple pour la vérification
        
        # 6 La nouvelle tuple :
        print("La nouvelle tuple est : ", tuple)
        
        
    # Question III.

        cset = set(["noir", "rouge", "jaune", "blanc", "vert", "bleu", "rose", "gris", "violet", "orange"])
        
        # 1 Afficher le set
        print("Le set : ",cset)
        
        # 2 Ajout d'un élément au set 
        cset.add("mauve")
        print("Le set : ",cset) #Affichage du set pour la vérification
        
        # 3 Supprimer un élément
        cset.remove("orange")
        print("Le nouveau set : ",cset) #Affichage du set pour la vérification
        
        # 4 Supprimer le set
        del cset
        
    # Question IV.

        dictionnaire = {"N": "Nom",
                        "Pr": "Prenom",
                        "A": "Age",
                        "S": "Sexe",
                        "Ad": "Adresse",
                        "Tel": "Téléphone",
                        "Email": "Compte Email",
                        "P": "Province",
                        "C": "Commune",
                        "Av": "Avenue"}
        
        # 1 Afficher le dictionnaire : 
        print("Dictionnaire :")
        print(dictionnaire)
        
        # 2 Afficher seulement les clés :
        print("Les Clés :")
        for key in dictionnaire.keys():
            print(key)
        
        # 3 Afficher seulement les valeurs :
        print("Les valeurs : ")
        for value in dictionnaire.values():
            print(value)
            
        # 4 Afficher les clés et les valeurs sous le format : Clé : Valeur
        print("\nClés et valeurs :")
        for key, value in dictionnaire.items():
            print(f"{key} : {value}")
        
        
        