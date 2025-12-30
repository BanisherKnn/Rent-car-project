class CarRentalSystem:
    def __init__(self):
        self.vehicule_dict = {}

    def ajouter_vehicule(self, vehicule):
        self.vehicule_dict[self, vehicule.id_vehicule] = vehicule

    def supprimer_vehicule(self, id_vehicule):
        if id_vehicule in self.vehicule_dict:
            del self.vehicule_dict[id_vehicule]

    def lister_vehicule(self, vehicule):
        for v in self.vehicule_dict.values():
            print (v.marque, v.model)

    def creer_reservation(self, client, vehicule, date_debut, date_fin):
        if not vehicule.disponibilite:
            raise Exception("Véhicule est indisponible") 
        
        if client.age < vehicule.age_min:
            raise Exception("Age insuffisant")
        
        rental = Rental(client, vehicule, date_debut, date_fin)
        vehicule.disponibilite = False
        client.historique.append(Rental)

