#Connection à la bdd + déf fct create delete update 
from app import app
from flask import render_template, jsonify, Flask,request, session, redirect, url_for

import pymysql
from config import *

connect = pymysql.connect(host=DATABASE_HOST,
                      db=DATABASE_NAME,
                      user=DATABASE_USER,
                      password=DATABASE_PASS)
cursor = connect.cursor()

user_data = None
task_data = None



#mes pages


def supprimer_commande():
    if request.method == 'POST':
        # Récupérez les données de la commande depuis la requête POST
        id_commande = request.form.get('id')

        # Supprimez la commande de la base de données
        try:
            with connect.cursor() as cursor:
                sql = "DELETE FROM commandes WHERE commande_id = %s"
                cursor.execute(sql, (id_commande,))
                connect.commit()
                # Renvoyer une réponse JSON pour indiquer que la commande a été supprimée avec succès
                return jsonify({'message': 'Commande supprimée avec succès !'})
            
        except Exception as e:
            # Gérer les erreurs de suppression dans la base de données
            return jsonify({'error': str(e)}), 500

    # Gérer d'autres méthodes HTTP ou erreurs si nécessaire
    return jsonify({'error': 'Méthode non autorisée'}), 405




def ajouter_commande():
    if request.method == 'POST':
        # Récupérez les données de la commande depuis la requête POST
        utilisateur = request.form.get('utilisateur')
        service = request.form.get('service')
        devis = request.form.get('devis')
        prix = request.form.get('prix')

        # Insérez la nouvelle commande dans la base de données
        try:
            
                # Vérifiez d'abord si l'utilisateur existe
            with connect.cursor() as cursor:
                # Exécutez une requête pour vérifier si l'utilisateur existe
                sql_check_user = "SELECT username FROM user WHERE username = %s"
                cursor.execute(sql_check_user, (utilisateur,))
                user = cursor.fetchone()

                if user:
                    with connect.cursor() as cursor:
                        sql = "INSERT INTO commandes (username, devis, services, prix_tot) VALUES (%s, %s, %s, %s)"
                        cursor.execute(sql, (utilisateur, devis, service, prix))
                        connect.commit()
                           # Renvoyer une réponse JSON pour indiquer que la commande a été ajoutée avec succès
                    return jsonify({'message': 'Commande ajoutée avec succès !'})
                
                else:
                    # L'utilisateur n'existe pas, renvoyez une erreur
                    return jsonify({'error': 'Utilisateur inexistant'}), 400
                
    

             
            

        except Exception as e:
            # Gérer les erreurs de l'insertion dans la base de données
            return jsonify({'error': str(e)}), 500

    # Gérer d'autres méthodes HTTP ou erreurs si nécessaire
    return jsonify({'error': 'Méthode non autorisée'}), 405

def devis_page():
    return render_template("devis.html", user_data=user_data, task_data=task_data)

def admin_page():

    return redirect(url_for("route_signin"))

def caca_page():#Page de test
    return render_template("caca.html", user_data=user_data, task_data=task_data)

def produits_page():
    return render_template("produits.html")

def profil_page():
    return render_template("profil.html", user_data=user_data, task_data=task_data)

def contact_page():
    return render_template("contact.html")

def cgu_page():
    return render_template("cgu.html")

def Apropos_page(): 
    return render_template("Apropos.html")

def commandes_page():
    cursor = connect.cursor()
    cursor.execute("""
        SELECT * FROM commandes
    """)
    commandes = cursor.fetchall()
    cursor.close()
    if not commandes:
        return "Pas encore de commandes. Revenez plus tard."
    ids = [commande[0] for commande in commandes]
    user_ids = [commande[1] for commande in commandes]
    devis = [commande[2] for commande in commandes]
    services_ids = [commande[3] for commande in commandes]
    prix = [commande[4] for commande in commandes]

    return render_template("commandes.html", id=ids, user_id=user_ids, devis=devis, services_id=services_ids, prix=prix)

def services_page():
    cursor = connect.cursor()
    cursor.execute("""
        SELECT * FROM services
    """)
    services = cursor.fetchall()
    cursor.close()

    if not services:
        return "Pas encore de services. Revenez plus tard."
    
    # Réorganiser les données pour passer au template
    ids = [service[0] for service in services]
    noms = [service[1] for service in services]
    images = [service[2] for service in services]
    prix = [service[3] for service in services]
    
    return render_template("services.html", id=ids, nom=noms, images=images, prix=prix)




def create_user(data):
    empty = cursor.execute("SELECT * FROM user WHERE username='{}' AND password='{}';".format(data.get('username'),
                                                                                              data.get('password'),
                                                                                              data.get('email')))
    if empty > 0:
        return jsonify(error="internal error: (1062, \"Duplicate entry 'admin' for key 'username'\")")
    else:
        cursor.execute("INSERT INTO user (username, password) VALUES ('{}', '{}');".format(data.get('username'),
                                                                                           data.get('password'),
                                                                                           data.get('email')))
        connect.commit()#Valide les changements

        return jsonify(result="account created dear {}".format(data.get('username')))

def create_task(data):
    global user_data
    if user_data == None:
        return jsonify(error="you must be logged in")
    cursor.execute("INSERT INTO task (title, begin, end, status) VALUES ('{}', '{}', '{}', '{}');".format(data.get('title'),
                                                                                                          data.get('begin'),
                                                                                                          data.get('end'),
                                                                                                          data.get('status')))
    connect.commit()

    return jsonify(result="new task added")

def delete_task(task_id):
    global user_data
    if user_data == None:
        return jsonify(error="you must be logged in")
    empty = cursor.execute("SELECT * FROM task WHERE task_id='{}';".format(task_id))
    if empty > 0:
        cursor.execute("DELETE FROM task WHERE task_id='{}';".format(task_id))
        return jsonify(result="task deleted")
    else:
        return jsonify(error="task id does not exist")

def display_task_with_id(task_id):
    global user_data
    if user_data == None:
        return jsonify(error="you must be logged in")
    result = ''
    empty = cursor.execute("SELECT * FROM task WHERE task_id='{}';".format(task_id))
    if empty > 0:
        result = cursor.fetchall()
        for t_id, title, begin, end, status in result:
            data = {"title":title, "begin":str(begin), "end":str(end), "status":status}
        return jsonify(result=data)
    else:
        return jsonify(error="task id does not exist")


def check_if_user_exist(data):
    global user_data
    empty = cursor.execute("SELECT * FROM user WHERE username='{}' AND password='{}';".format(data.get('username'),
                                                                                                  data.get('password')))
    if empty > 0:
        user_data = data
        return jsonify(result="signin successful")
    else:
        return jsonify(error="login or password does not match")

def view_all_task():
    global task_data
    global user_data
    if user_data == None:
        return jsonify(error="you must be logged in")
    result = ''
    cursor.execute("SELECT * FROM task;")
    result = cursor.fetchall()
    task_data = {"tasks":{t_id: {"title":title, "begin":str(begin), "end":str(end), "status":status} for t_id, title, begin, end, status in result}}
    data = {"tasks":[{t_id: {"title":title, "begin":str(begin), "end":str(end), "status":status}} for t_id, title, begin, end, status in result]}
    return jsonify(result=data)

def update_task_by_id(task_id, data):
    global user_data
    if user_data == None:
        return jsonify(error="you must be logged in")
    empty = cursor.execute("SELECT * FROM task WHERE task_id='{}';".format(str(task_id)))
    if empty > 0:
        cursor.execute("UPDATE task SET title='{}', begin='{}', end='{}', status='{}' WHERE task_id='{}';".format(data.get('title'),
                                                                                                                  data.get('begin'),
                                                                                                                  data.get('end'),
                                                                                                                  data.get('status'),
                                                                                                                  str(task_id)))
        return jsonify(result="update done")
    else:
        return jsonify(error="task id does not exist")

def disconnect_user():
    global user_data
    user_data = None
    return jsonify(result="signout successful")

def see_user_information():
    global user_data
    if user_data:
        return jsonify(result=user_data)
    else:
        return jsonify(error="you must be logged in")

def main_page():
    if "user" in session:
        return render_template("index.html",
                            user_data=user_data,
                            task_data=task_data)
    else:
        return redirect(url_for("route_signin"))