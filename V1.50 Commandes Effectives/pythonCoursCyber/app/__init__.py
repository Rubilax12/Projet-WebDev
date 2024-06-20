# Importer Flask pour la création de l'application
from flask import Flask


# Création de l'instance principale de l'application Flask
app = Flask(__name__)




# Chargement des configurations depuis le fichier config.py
app.config.from_object('config')



# Importation des vues depuis le dossier app
from app import views
