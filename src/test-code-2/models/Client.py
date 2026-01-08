from sqlalchemy import Column, Integer, String
from database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    prenom = Column(String)
    age = Column(Integer)
    permis = Column(String)
    statut = Column(String, default="Actif")
