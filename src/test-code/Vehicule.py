class Vehicule:
    def __init__(self, id_vehicule, marque, model, categorie, poids, etat, tarif):
        self.marque = marque
        self.vehicule_id = id_vehicule
        self.model = model
        self.categorie = categorie
        self.poids = poids
        self.etat = etat
        self.tarif = tarif

class Car(Vehicule):
    def __init__(self, id_vehicule, marque, model, categorie, poids, etat, tarif, portes):
        super().__init__(id_vehicule, marque, model, categorie, poids, etat, tarif)
        self.portes = portes

class Motocycle(Vehicule):
    pass

class Truck(Vehicule):
    def __init__(self, id_vehicule, marque, model, categorie, poids, etat, tarif, hauteur):
        super().__init__(id_vehicule, marque, model, categorie, poids, etat, tarif)
        self.hauteur = hauteur