from CarRentalSystem import CarRentalSystem
from Client import Client, ClientEnCours
from Rental import Rental
from Vehicule import Vehicule, Car, Motocycle, Truck

if __name__ == "__main__":
    system = CarRentalSystem()

    v1 = Vehicule(1 ,"BMW", "G82", "Berline", 2034, "Neuf", 200, 21, True)
    v2 = Vehicule(2 ,"Mercedes", "C220", "Berline", 1987, "Bon état", 150, 20, True)
    v3 = Vehicule(3 ,"Volkswagen", "Golf-8", "coupé", 1503, "Bon état", 120, 18, True)
    v4 = Vehicule(4 ,"Volkswagen", "Golf-7", "coupé", 1405, "Correcte", 100, 18, True)

    c1 = Client(1, "Autreau", "Christine", 24, "B1", "Pas d'antécédent", statut="Actif")
    c2 = Client(2, "Yilmaz", "Kenan", 20, "B1", "Pas d'antécédent", statut="Actif")
    c3 = Client(3, "Yilmaz", "Sinan", 28, "B1", "Pas d'antécédent", statut="Actif")

    system.ajouter_vehicule(v1)
    system.ajouter_vehicule(v2)
    system.ajouter_vehicule(v3)
    system.ajouter_vehicule(v4)
    system.ajouter_client(c1)
    system.ajouter_client(c2)
    system.ajouter_client(c3)

    system.creer_reservation(c1, v1, "2024-01-01", "2024-01-05")
    system.creer_reservation(c3, v2, "2024-01-08", "2024-01-31")
    system.creer_reservation(c3, v3, "2024-01-08", "2024-01-31")

    print(system.rapport_global())
