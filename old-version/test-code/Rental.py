class Rental:
    def __init__(self, client, vehicule, date_debut, date_fin,
                 prix_total=0, penalites=0, etat_de_reservation="En cours"):
        self.client = client
        self.vehicule = vehicule
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.prix_total = prix_total
        self.penalites = penalites
        self.etat_de_reservation = etat_de_reservation

    def calcul_prix(self):
        duree = (self.date_fin - self.date_debut)
        prix = duree * self.vehicule.tarif