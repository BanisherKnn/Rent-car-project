# CarRentalSystem.py
from sqlalchemy.orm import Session
from Client import Client
from Vehicule import Vehicule
from Rental import Rental

class CarRentalSystem:
    def __init__(self, db_session: Session):
        self.db = db_session

    # ---------------- Clients ----------------
    def ajouter_client(self, client: Client):
        # Ajouter uniquement si l'objet n'est pas déjà dans la session
        if client not in self.db:
            self.db.add(client)
        self.db.commit()

    def lister_clients(self):
        return self.db.query(Client).all()

    # ---------------- Véhicules ----------------
    def ajouter_vehicule(self, vehicule: Vehicule):
        if vehicule not in self.db:
            self.db.add(vehicule)
        self.db.commit()

    def lister_vehicules_disponibles(self):
        return self.db.query(Vehicule).filter_by(disponibilite=True).all()

    # ---------------- Réservations ----------------
    def creer_reservation(self, client: Client, vehicule: Vehicule, date_debut, date_fin):
        reservation = Rental(
            client_id=client.id,
            vehicule_id=vehicule.id,
            date_debut=date_debut,
            date_fin=date_fin
        )
        self.db.add(reservation)

        # Marquer le véhicule comme indisponible
        vehicule.disponibilite = False

        self.db.commit()

    # ---------------- Rapport Global ----------------
    def rapport_global(self):
        clients = self.db.query(Client).all()
        vehicules = self.db.query(Vehicule).all()
        reservations = self.db.query(Rental).all()

        return (
            f"Nombre de clients : {len(clients)}\n"
            f"Nombre de véhicules : {len(vehicules)}\n"
            f"Nombre de réservations : {len(reservations)}"
        )