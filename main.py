if __name__=="__main__":
    # Question 1
        marque_vehicules=['Honda','Toyota','Mercedes','ferrari','lambourghini','Mazda','Citroen','Audi','BMW','Peugeot']
    #    1 affichage des elements de la liste
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
        # 7 Suppression l'élément à l’index numéro 2
        del new_marque[2]
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
        
        
        