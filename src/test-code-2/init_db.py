from database import engine, Base
from models.Client import Client
from models.Vehicule import Vehicule
from models.Rental import Rental

Base.metadata.create_all(engine)
print("Base initialisée")