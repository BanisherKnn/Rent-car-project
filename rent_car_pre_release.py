class Vehicule:
    def __init__(self, id_vehicule, marque, model, categorie, portes, etat, tarif):
        self.marque = marque
        self.id_vehicule = id_vehicule
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

class CarRentalSystem:
    def __init__(self):
        self.vehicule_dict = {}

    def ajouter_vehicule(self, vehicule):
        self.vehicule[self, vehicule] = vehicule

class Client:
    def __init__(self, id_client, nom, prenom, age, permis, historique):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.permis = permis
        self.historique = historique
        