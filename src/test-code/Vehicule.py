class Vehicule:
    def __init__(self, id_vehicule, marque, model, categorie, portes, etat, tarif):
        self.marque = marque
        self.vehicule_id = id_vehicule
        self.model = model
        self.categorie = categorie
        self.portes = portes
        self.etat = etat
        self.tarif = tarif

class Car(Vehicule):
    pass

class Motocycle(Vehicule):
    pass

class Truck(Vehicule):
    pass
