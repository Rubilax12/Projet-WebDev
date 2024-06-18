#Définit les routes pour pour différentes url & utilise controller pour validation des data
from app import app
from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from datetime import timedelta
import pymysql as sql
from app import controller, models


from functools import wraps
from flask import session, redirect, url_for

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' != 'admin':
            return redirect(url_for('route_signin'))
        return f(*args, **kwargs)
    return decorated_function


app.secret_key = "SecretKeyPermettantDeChiffrerLesCookiesDeSession"
app.permanent_session_lifetime = timedelta(days=5)

@app.route('/', methods=['GET'])
def route_index():
    return models.main_page()

#mes routes
@app.route('/commandes', methods=['GET'])
#def commandes():
#    client_id = get_client_id_from_session()  # Fonction à implémenter pour récupérer l'ID du client à partir de la session
#    commandes = Commande.query.filter_by(client_id=client_id).all()
#    return models.commandes_page()

@app.route('/devis', methods=['GET'])
def devis():
    return models.devis_page()

@app.route('/admin', methods=['GET'])
@admin_required
def admin():
    return models.admin_page()

@app.route('/caca', methods=['GET'])
def caca():
    return models.caca_page()

@app.route('/produits', methods=['GET'])
def produits():
    return models.produits_page()

@app.route("/profil", methods=['GET'])
def profil():
    return models.profil_page()

@app.route("/contact", methods=['GET'])
def contact():
    return models.contact_page()

@app.route('/cgu', methods=['GET'])
def cgu():
    return models.cgu_page()

@app.route('/Apropos', methods=['GET'])
def Apropos():
    return models.Apropos_page()

#fin de mes routes

@app.route('/signin', methods=['POST', "GET"])
def route_signin():
    try:
        if request.method == "GET":
            if "user" in session:
                return redirect(url_for("caca"))
            
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
            session['user'] = data.get('username')

        
        if not all(key in data for key in ['username', 'password']): 
            return jsonify(error="Missing required fields"), 400  # Bad request

        return models.check_if_user_exist(data)
    except:
        return jsonify(error="internal error")
    

@app.route('/signin2', methods=['POST'])
def route_signin2():
    try:
        data = controller.transform_request_to_user(json_data=request.json, form_data=request.form)
        return models.check_if_user_exist(data)
    except:
        return jsonify(error="internal error")

@app.route('/register2', methods=['POST'])
def route_register2():
    try:
        data = controller.transform_request_to_user(json_data=request.json, form_data=request.form)
        return models.create_user(data)
    except:
        return jsonify(error="internal error")


@app.route('/register', methods=['POST'])
def route_register():
    try:
        # Vérifie si les données sont en JSON
        if request.is_json:
            data = request.get_json()
        # sinon essaye de récupérer les données du formulaire
        else:
            data = request.form

        # Valide et traite les données
        if not all(key in data for key in ['username', 'password', 'email']):
            return jsonify(error="Missing required fields"), 400  # Bad request

        return models.create_user(data)
    except Exception as e:  # Capture l'exception générale
        return jsonify(error=f"internal error: {e}")  # Renvoie l'erreur et le message





@app.route('/signout', methods=['POST'])
def route_signout():
    return models.disconnect_user()


@app.route('/user', methods=['GET'])
def route_user():
    try:
        return models.see_user_information()
    except:
        return jsonify(error="internal error")


@app.route('/user/task', methods=['GET'])
def route_user_task():
    try:
        return models.view_all_task()
    except:
        return jsonify(error="internal error")


@app.route('/user/task/add2', methods=['POST'])
def route_user_task_add2():
    try:
        data = controller.transform_request_to_task(json_data=request.json, form_data=request.form)
        return models.create_task(data=data)
    except Exception as e:
        print(e)
        return jsonify(error="internal error")


@app.route('/user/task/add', methods=['POST'])
def route_user_task_add():
    try:
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        if not all(key in data for key in ['title', 'begin', 'end', 'status']):
            return jsonify(
                error="Missing required fields"), 400  # Bad request

        models.create_task(data=data)
        return models.main_page()
    except Exception as e:
        print(e)
        return jsonify(error="internal error")


@app.route('/user/task/<task_id>', methods=['GET', 'POST'])
def route_user_task_id(task_id):
    """
    Cette fonction gère la route '/user/task/<task_id>' pour les méthodes HTTP GET et POST.

    - `<task_id>` est un paramètre de la route qui représente l'identifiant unique d'une tâche.

    En fonction de la méthode HTTP utilisée :

      - GET : Affiche les détails d'une tâche spécifique en utilisant l'identifiant fourni.
        - Appelle la fonction `models.display_task_with_id(task_id=task_id)` pour récupérer les informations de la tâche et les renvoyer.
      - POST : Modifie une tâche existante en utilisant l'identifiant fourni et les données de la requête.
        - Récupère les données de la requête (JSON ou formulaire) et les transforme en un format utilisable par la fonction `controller.transform_request_to_task(json_data=request.json, form_data=request.form)`.
        - Appelle la fonction `models.update_task_by_id(task_id=task_id, data=data)` pour mettre à jour la tâche dans la base de données en utilisant l'identifiant et les nouvelles données.
        - Renvoie une confirmation de la mise à jour.

    En cas d'exception :

      - Intercepte toutes les exceptions (`Exception`) survenant pendant l'exécution de la fonction.
      - Imprime l'erreur dans la console pour analyse (utile pour le débogage).
      - Renvoie une réponse d'erreur au format JSON avec le message "internal error".
    """
    try:
        if request.method == 'GET':
            return models.display_task_with_id(task_id=task_id)
        if request.method == 'POST':
            data = controller.transform_request_to_task(json_data=request.json, form_data=request.form)
            return models.update_task_by_id(task_id=task_id, data=data)
    except Exception as e:
        print(e)
        return jsonify(error="internal error")


@app.route('/user/task/del/<task_id>', methods=['POST'])
def route_user_task_del(task_id):
    """
    Cette fonction gère la route '/user/task/del/<task_id>' pour la méthode HTTP POST.

    - `<task_id>` est un paramètre de la route qui représente l'identifiant unique d'une tâche.

    Cette route permet de supprimer une tâche de la base de données.

    - Récupère l'identifiant de la tâche à supprimer à partir de l'URL.
    - Appelle la fonction `models.delete_task(task_id=task_id)` pour supprimer la tâche de la base de données en utilisant l'identifiant fourni.
    - En cas de succès, renvoie une confirmation de suppression (la nature exacte de la réponse dépend de la fonction `models.delete_task`).

    En cas d'exception :

      - Intercepte toutes les exceptions (`Exception`) survenant pendant l'exécution de la fonction.
      - Renvoie une réponse d'erreur au format JSON avec le message "internal error".
    """
    try:
        return models.delete_task(task_id=task_id)
    except:
        return jsonify(error="internal error")
