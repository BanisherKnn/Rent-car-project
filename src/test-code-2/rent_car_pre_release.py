from datetime import date
from CarRentalSystem import CarRentalSystem
from Client import Client
from Vehicule import Vehicule

system = CarRentalSystem()

v1 = Vehicule(marque="BMW", model="G82", categorie="Berline",
              poids=2034, etat="Neuf", tarif=200, age_min=21)

c1 = Client(nom="Autreau", prenom="Christine", age=24, permis="B1")

system.ajouter_vehicule(v1)
system.ajouter_client(c1)

system.creer_reservation(c1, v1, date(2024,1,1), date(2024,1,5))

print("OK")