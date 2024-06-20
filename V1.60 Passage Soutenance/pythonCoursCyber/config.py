# Définition des la variables d'environnement pour l'hôte, le nom, l'utilisateur et le mot de passe de la base de données
DATABASE_HOST = 'localhost'
DATABASE_NAME = 'project'
DATABASE_USER = 'root'
DATABASE_PASS = 'root'

from flask import Flask
from flask_session import Session
from app import app

app.secret_key = "SecretKeyPermettantDeChiffrerLesCookiesDeSession"
SESSION_TYPE = 'filesystem'