from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    age = Column(Integer)
    permis = Column(String)
    statut = Column(String)

    historique = relationship("Rental", back_populates="client")
