class Vehicule:
    def __init__(self, id_vehicule, marque, model, categorie, poids,
                 etat, tarif, age_min, disponibilite=True):
        self.marque = marque
        self.id_vehicule = id_vehicule
        self.model = model
        self.categorie = categorie
        self.poids = poids
        self.etat = etat
        self.tarif = tarif
        self.age_min = age_min
        self.disponibilite = disponibilite

class Car(Vehicule):
    def __init__(self, id_vehicule, marque, model, categorie, poids,etat, tarif, age_min, disponibilite, portes):
        super().__init__(id_vehicule, marque, model, categorie, poids, etat, tarif, age_min, disponibilite)
        self.portes = portes

class Motocycle(Vehicule):
    pass

class Truck(Vehicule):
    def __init__(self, id_vehicule, marque, model, categorie, poids, etat, tarif, age_min, disponibilite, hauteur, portes):
        super().__init__(id_vehicule, marque, model, categorie, poids, etat, tarif, age_min, disponibilite)
        self.hauteur = hauteur
        self.portes = portes