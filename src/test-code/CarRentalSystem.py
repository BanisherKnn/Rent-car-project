from Rental import Rental

class CarRentalSystem:
    def __init__(self):
        self.vehicule_dict = {}
        self.client_dict = {}

    def rapport_global(self):
        rapport = []
        rapport.append("----Rapport Global----")
        rapport.append(f"Nombre de vehicule : {len(self.vehicule_dict)}")
        rapport.append(f"Nombre de clients : {len(self.client_dict)}")
        
        rapport.append("\n --Véhicules--")
        for v in self.vehicule_dict.values():
            dispo = "Disponible" if v.disponibilite else "Indisponible"
            rapport.append(f"{v.marque} {v.model} - {dispo}")

        rapport.append("\n --Clients--")
        for c in self.client_dict.values():
            rapport.append(f"{c.nom} {c.prenom} - Réservation = {len(c.historique)}")

        return "\n".join(rapport)

    def ajouter_vehicule(self, vehicule):
        self.vehicule_dict[vehicule.id_vehicule] = vehicule

    def supprimer_vehicule(self, id_vehicule):
        if id_vehicule in self.vehicule_dict:
            del self.vehicule_dict[id_vehicule]

    def lister_vehicule(self, vehicule):
        for v in self.vehicule_dict.values():
            print (v.marque, v.model)

    def ajouter_client(self, client):
        self.client_dict[client.id_client] = client

    def creer_reservation(self, client, vehicule, date_debut, date_fin):
        if not vehicule.disponibilite:
            raise Exception("Véhicule est indisponible") 
        
        if client.age < vehicule.age_min:
            raise Exception("Age insuffisant")
        
        rental = Rental(client, vehicule, date_debut, date_fin, prix_total=0, penalites=0, etat_de_reservation="En cours")
        vehicule.disponibilite = False
        client.historique.append(rental)