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