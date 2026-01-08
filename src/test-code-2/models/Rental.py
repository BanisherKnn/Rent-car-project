from sqlalchemy import Column, Integer, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    vehicule_id = Column(Integer, ForeignKey("vehicules.id"))

    date_debut = Column(Date)
    date_fin = Column(Date)
    prix_total = Column(Integer, default=0)
    penalites = Column(Integer, default=0)
    etat_de_reservation = Column(String, default="En cours")

    client = relationship("Client")
    vehicule = relationship("Vehicule")
