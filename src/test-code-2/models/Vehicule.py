from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Vehicule(Base):
    __tablename__ = "vehicules"

    id = Column(Integer, primary_key=True)
    marque = Column(String)
    model = Column(String)
    categorie = Column(String)
    poids = Column(Integer)
    etat = Column(String)
    tarif = Column(Integer)
    age_min = Column(Integer)
    disponibilite = Column(Boolean, default=True)
