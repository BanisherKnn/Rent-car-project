class Client:
    def __init__(self, id_client, nom, prenom, age, permis, historique, statut="NonActif"):
        self.id_client = id_client
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.permis = permis
        self.historique = []
        self.statut = statut
        
        
class ClientEnCours(Client):
    pass