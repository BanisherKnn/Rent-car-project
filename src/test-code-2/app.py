import streamlit as st

from CarRentalSystem import CarRentalSystem
from models.Client import Client
from models.Vehicule import Vehicule

if "system" not in st.session_state:
    st.session_state.system = CarRentalSystem()

system = st.session_state.system

st.title("Location de véhicules")

st.header("Ajouter un client")
nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
age = st.number_input("Âge", min_value=18)
permis = st.text_input("Permis")

if st.button("Ajouter"):
    c = Client(nom=nom, prenom=prenom, age=age, permis=permis)
    system.ajouter_client(c)
    st.success("Client ajouté")

st.header("Test DB")
st.write("Clients :", system.db.query(Client).count())
st.write("Véhicules :", system.db.query(Vehicule).count())
