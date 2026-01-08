from database import SessionLocal
from models.rental import Rental

class CarRentalSystem:
    def __init__(self):
        self.db = SessionLocal()

    def ajouter_client(self, client):
        self.db.add(client)
        self.db.commit()

    def ajouter_vehicule(self, vehicule):
        self.db.add(vehicule)
        self.db.commit()

    def creer_reservation(self, client, vehicule, date_debut, date_fin):
        if not vehicule.disponibilite:
            raise Exception("Véhicule indisponible")

        if client.age < vehicule.age_min:
            raise Exception("Âge insuffisant")

        rental = Rental(
            client=client,
            vehicule=vehicule,
            date_debut=date_debut,
            date_fin=date_fin
        )

        vehicule.disponibilite = False

        self.db.add(rental)
        self.db.commit()

    def rapport_global(self):
        vehicules = self.db.query(type(self.db.query.__self__)).all()
        clients = self.db.query(type(self.db.query.__self__)).all()

        rapport = []
        rapport.append("----Rapport Global----")
        rapport.append(f"Nombre de véhicules : {len(vehicules)}")
        rapport.append(f"Nombre de clients : {len(clients)}")

        return "\n".join(rapport)
