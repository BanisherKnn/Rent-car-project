from database import engine, Base
from Client import Client
from Vehicule import Vehicule
from Rental import Rental

Base.metadata.create_all(engine)
print("Base initialisée")