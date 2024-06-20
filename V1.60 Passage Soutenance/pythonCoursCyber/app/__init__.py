# Importer Flask pour la création de l'application
from flask import Flask
from flask_session import Session

# Création de l'instance principale de l'application Flask
app = Flask(__name__)

app.config.from_object('config')
Session(app)

# Importation des vues depuis le dossier app
from app import views
