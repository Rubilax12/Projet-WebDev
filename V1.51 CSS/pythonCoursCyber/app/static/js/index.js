var id_to_modify = null;


//Persos
function supprimerCommande(id_commande) {
    // Envoi des données au serveur Flask via une requête Ajax
    $.ajax({
        type: 'POST',
        url: '/supprimer_commande',  // URL de votre route Flask pour supprimer une commande
        data: {
            id: id_commande
        },
        success: function() {
            // Réponse du serveur (optionnel)
            console.log('Commande supprimée avec succès !');
            location.reload();
        },
        error: function(xhr, status, error) {
            console.error('Erreur lors de la suppression de la commande : ', xhr.responseText);
            alert('Erreur lors de la suppression de la commande. Veuillez réessayer plus tard.', status, error);
        }
    });
}

function ajouterCommande() {
        // Exemple de récupération de données (à remplacer par votre propre logique)
        var nouvelUtilisateur = document.getElementById('Utilisateur').value;
        var nouveauDevis = document.getElementById('Devis').value;
        var nouveauService = document.getElementById('Services').value;
        var nouveauPrix = document.getElementById('Prix').value;

        // Envoi des données au serveur Flask via une requête Ajax
        $.ajax({
            type: 'POST',
            url: '/ajouter_commande',  // URL de votre route Flask pour ajouter une commande
            data: {
                utilisateur: nouvelUtilisateur,
                devis: nouveauDevis,
                service: nouveauService,
                prix: nouveauPrix
            },
            
            success: function() {
                // Réponse du serveur (optionnel)
                console.log('Commande ajoutée avec succès !');
                // Vous pouvez mettre à jour l'affichage ou effectuer d'autres actions ici
                location.reload();
            },
            error: function(error) {
                console.error('Erreur lors de l\'ajout de la commande : ', error);
            }
        });
}


function reloadTask() {
    $.getJSON('http://127.0.0.1:5000/user/task');
    location.reload();
    return false;
}

function displayBox(type, text) {
    document.getElementById("textType").innerHTML = type;
    document.getElementById("textValue").innerHTML = text;
    document.getElementById("info").classList.add("displayed");
}
  
function removeBox() {
    document.getElementById("info").classList.remove("displayed");
    if (document.getElementById("textValue").innerHTML.localeCompare("signin successful") == 0)
        location.reload();
    if (document.getElementById("textValue").innerHTML.localeCompare("signout successful") == 0)
        location.reload();
    if (document.getElementById("textValue").innerHTML.localeCompare("new task added") == 0)
        location.reload();
    if (document.getElementById("textValue").innerHTML.localeCompare("task deleted") == 0)
        location.reload();
    location.reload();
}
  
function signin() {
    $.post('http://127.0.0.1:5000/signin', {
        username: $('input[name="username"]').val(),
        password: $('input[name="password"]').val(),
        email: $('input[name="email"]').val()
    }, function(data) {
        if (data.result){
            displayBox("RESULT", data.result);
            location.reload();}
        else
            displayBox("ERROR", data.error);
    }, 'json');
    return false;
}

function register() {
    $.post('http://127.0.0.1:5000/register', {
        username: $('input[name="username"]').val(),
        password: $('input[name="password"]').val(),
        email: $('input[name="email"]').val()
    }, function(data) {
        if (data.result){
            displayBox("RESULT", data.result);}
            

        else
            displayBox("ERROR", data.error);
    }, 'json');
    return false;
}

function signout() {
    $.post('http://127.0.0.1:5000/signout', function(data) {
        displayBox("RESULT", data.result);
    }, 'json');
    return false;
}

function replace(chain, pos, char) {
    console.log(chain);
    return chain.substring(0,pos - 1) + char + chain.substring(pos);
};
  
function transformJSON() {
    var taskData = {title: $('input[name="title"]').val(),
                begin: replace($('input[name="begin"]').val(), 11, ' ').concat(":00"),
                end: replace($('input[name="end"]').val(), 11, ' ').concat(":00"),
                status: $('select').val()};
    $.post('http://127.0.0.1:5000/user/task/add', taskData, function(data) {
        if (data.result)
            displayBox("RESULT", data.result);
        else
            displayBox("ERROR", data.error);
    }, 'json');
    document.getElementById('task_page').classList.remove("displayedTask");
    reloadTask();
    return false;
}

function transformJSON_update() {
    var taskData = {title: $('input[name="title"]').val(),
                begin: replace($('input[name="begin"]').val(), 11, ' ').concat(":00"),
                end: replace($('input[name="end"]').val(), 11, ' ').concat(":00"),
                status: $('select').val()};
    $.post('http://127.0.0.1:5000/user/task/'.concat(id_to_modify), taskData, function(data) {
        if (data.result)
            displayBox("RESULT", data.result);
        else
            displayBox("ERROR", data.error);
    }, 'json');
    document.getElementById('task_page').classList.remove("displayedTask");
    reloadTask();
    return false;
}
  
function displayTask(data) {
    document.getElementById('taskText').innerHTML = data;
    document.getElementById('task_page').classList.add("displayedTask");
}

function deleteTask(taskID) {
    $.post('http://127.0.0.1:5000/user/task/del/'.concat(taskID),
    function(data) {
        if (data.result)
            displayBox("RESULT", data.result);
        else
            displayBox("ERROR", data.error);
    }, 'json');
    return false;
}

function modifyTask(taskID, title, begin, end, status) {
    id_to_modify = taskID.toString();
    $("#titleID").val(title);
    $("#beginID").val(replace(begin, 11, 'T').substring(0, 16));
    $("#endID").val(replace(end, 11, 'T').substring(0, 16));
    $("#statusID").val(status);
    document.getElementById('valid_button').setAttribute("onClick", "transformJSON_update()");
    displayTask("Update task");
}