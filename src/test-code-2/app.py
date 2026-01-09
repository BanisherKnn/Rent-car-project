import streamlit as st
from sqlalchemy.orm import sessionmaker
from database import engine  # ton fichier database.py avec create_engine
from CarRentalSystem import CarRentalSystem
from Client import Client
from Vehicule import Vehicule
from Rental import Rental

# --- Session SQLAlchemy ---
Session = sessionmaker(bind=engine)
db_session = Session()

# --- Instance du système ---
system = CarRentalSystem(db_session)

# --- Menu Streamlit ---
menu = st.sidebar.selectbox("Menu", ["Ajouter Client", "Ajouter Véhicule", "Créer Réservation", "Rapport Global"])

# --- Ajouter Client ---
if menu == "Ajouter Client":
    st.header("Ajouter un Client")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    age = st.number_input("Âge", min_value=18, max_value=100)
    permis = st.text_input("Permis")
    
    if st.button("Ajouter"):
        client = Client(nom=nom, prenom=prenom, age=age, permis=permis, statut="Actif")
        system.ajouter_client(client)
        st.success(f"Client {nom} {prenom} ajouté !")

# --- Ajouter Véhicule ---
elif menu == "Ajouter Véhicule":
    st.header("Ajouter un Véhicule")
    marque = st.text_input("Marque")
    model = st.text_input("Modèle")
    tarif = st.number_input("Tarif", min_value=0)
    
    if st.button("Ajouter Véhicule"):
        vehicule = Vehicule(marque=marque, model=model, categorie="", poids=0, etat="Neuf", tarif=tarif, age_min=18, disponibilite=True)
        system.ajouter_vehicule(vehicule)
        st.success(f"Véhicule {marque} {model} ajouté !")

# --- Créer Réservation ---
elif menu == "Créer Réservation":
    st.header("Créer une Réservation")
    
    clients = db_session.query(Client).all()
    vehicules = db_session.query(Vehicule).filter_by(disponibilite=True).all()
    
    if not clients or not vehicules:
        st.warning("Il faut au moins un client et un véhicule disponible pour créer une réservation.")
    else:
        client = st.selectbox("Choisir un client", clients, format_func=lambda c: f"{c.nom} {c.prenom}")
        vehicule = st.selectbox("Choisir un véhicule", vehicules, format_func=lambda v: f"{v.marque} {v.model}")
        date_debut = st.date_input("Date début")
        date_fin = st.date_input("Date fin")
        
        if st.button("Créer Réservation"):
            try:
                system.creer_reservation(client, vehicule, date_debut, date_fin)
                st.success(f"Réservation créée pour {client.nom} {client.prenom} avec {vehicule.marque} {vehicule.model}")
            except Exception as e:
                st.error(f"Erreur: {str(e)}")

# --- Rapport Global ---
elif menu == "Rapport Global":
    st.header("Rapport Global")
    st.text(system.rapport_global())
