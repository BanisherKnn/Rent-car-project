class Client:
    def __init__(self, id_client, nom, prenom, age, permis, historique, statut="NonActif"):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.permis = permis
        self.historique = historique
        self.statut = statut
        
class ClientEnCours(Client):
    def __init__(self, id_client, nom, prenom, age, permis, historique, date_debut, date_fin):
        super().__init__(id_client, nom, prenom, age, permis, historique)
        self.date_debut = date_debut
        self.date_fin = date_fin 
