from CarRentalSystem import CarRentalSystem
from Client import Client, ClientEnCours
from Rental import Rental
from Vehicule import Vehicule, Car, Motocycle, Truck

if __name__ == "__main__":
    system = CarRentalSystem()

    v1 = Vehicule(1 ,"BMW", "G82", "Berline", 2034, "Neuf", 200, 21, True)
    v2 = Vehicule(2 ,"Mercedes", "C220", "Berline", 1987, "Bon état", 150, 18, True)

    c1 = Client(1, "Autreau", "Christine", 24, "B1", "Pas d'antécédent", statut="Actif")
    c2 = Client(2, "Yilmaz", "Kenan", 20, "B1", "Pas d'antécédent", statut="Actif")

    system.ajouter_vehicule(v1)
    system.ajouter_vehicule(v2)
    system.ajouter_client(c1)
    system.ajouter_client(c2)

    system.creer_reservation(c1, v1, "2024-01-01", "2024-01-05")

    print(system.rapport_global())
