Fonctionnement technique du site:

Architecture du projet:

my_flask_app/                                                                            
├── app/                                                                            
│   ├── __init__.py (Lance l'app Flask et initialise la session)                                                            
│   ├── controller.py (Gestion des contrôleurs, actuellement peu utilisé)                                                        
│   ├── views.py (Gestion des vues)                                                                                
│   ├── models.py (Interaction avec la base de données)                                                
│   ├── templates/ (Pages HTML)                                                        
│   │   ├── index.html (Page d'accueil)                                                                
│   │   ├── Apropos.html (Page informatique sur le site)                                                                    
│   │   ├── contact.html (Page de contact permettant d'envoyer un message à l'admin du site ) (20/06 => envoi non fonctionnel)                                                                    
│   │   ├── login.html (Page de connexion)                                                        
│   │   ├── devis.html (gère les devis en fonction du compte connecté) (20/06=> non fonctionnel)                                                    
│   │   ├── profile.html (Page de profil utilisateur)                                                        
│   │   ├── commandes.html (Page des commandes gérée par la base de données)                                                            
│   │   ├── navigation.html (Header de toutes les pages)                                                                            
│   │   ├── services.html montre les services disponibles directement depuis la BDD                                                                                                     
│   ├── static/ (Fichiers statiques)                                                                                
│   │   ├── css/ (Feuilles de style pour chaque page)                                                                                                                                        
│   │   ├──                                                                                                     
│   │   ├── js/ (Scripts JavaScript)                                                                            
│   │   │   ├── jquery.js (Bibliothèque jQuery)                                                                                        
│   │   │   ├── index.js (Contient toutes les fonctions JavaScript)                                                                                                
│   │   ├── img/ (Images utilisées sur le site, en formats PNG & JPG)                                                        
├── config.py (Définit les variables d'environnement)                                                        
├── run.py (Lance le site sur localhost avec le port 5000)                                            
└── README.md (Ce fichier)                                                                        


Fonctionnement du site

Le site utilise Flask (framework web Python) et suit le modèle MVC (Modèle-Vue-Contrôleur) pour organiser le code :
V pour Views

    Routes et Méthodes HTTP :
        Les vues définissent les routes accessibles via des URL spécifiques (par exemple, / pour la page d'accueil).
        Chaque route peut accepter des méthodes GET et/ou POST pour recevoir des données et répondre en conséquence.
        Les vues sont responsables de la gestion de l'interface utilisateur et de la logique de présentation.

M pour Models

    Interaction avec la Base de Données :
        Les modèles effectuent des opérations sur la base de données, telles que la vérification des utilisateurs ou la gestion des sessions.
        Ils récupèrent les informations nécessaires des tables de la base de données.
        Les modèles renvoient ensuite des données à afficher dans les templates HTML situés dans le dossier templates.

C pour Controllers

    Opérations sur la Base de Données :
        Les contrôleurs réalisent idéalement les opérations directes sur la base de données.
        Actuellement, cette partie est partiellement négligée et les appels vers la base de données se font principalement dans models.py.
        Les contrôleurs coordonnent les interactions entre les modèles et les vues.

Exécution du Projet

Pour lancer le projet, assurez-vous d'avoir les dépendances nécessaires installées et exécutez le script run.py. Ce script lancera le serveur Flask et publiera le site sur http://127.0.0.1:5000. Dependances:
Flask
Flask_session
app
pymysql
config
datetime

bash:
python run.py

Améliorations à Apporter

    Séparation des Responsabilités : Déplacer les appels à la base de données de models.py vers controller.py pour une meilleure séparation des responsabilités.
    Gestion des Sessions : Assurer une gestion robuste des sessions utilisateur pour une meilleure sécurité et expérience utilisateur.
    Optimisation des Vues : Améliorer les vues pour une meilleure présentation et interactivité.
    Réaliser la page devis.html
    Fluidifier les boutons login/register/signout
    Exporter les produits dans la page service (géré par BDD)
    Pouvoir éditer le profil dans /profil
    Pouvoir envoyer un message dans /contact



