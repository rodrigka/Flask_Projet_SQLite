from flask import Flask, request, jsonify
import sqlite3
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Utilisateurs autorisés
users = {
    "user": "12345"
}

# Fonction de vérification de l'authentification
@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
    return False

# Route pour rechercher un client par son nom
@app.route('/fiche_nom/', methods=['GET'])
@auth.login_required
def recherche_par_nom():
    nom_client = request.args.get('nom')  # Récupère le paramètre 'nom' de l'URL
    if nom_client:
        # Connexion à la base de données SQLite
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM clients WHERE nom = ?", (nom_client,))
        resultats = c.fetchall()
        conn.close()
        if resultats:
            return jsonify(resultats)  # Retourne les résultats en format JSON
        else:
            return "Aucun client trouvé avec ce nom", 404
    else:
        return "Veuillez spécifier un nom de client", 400

if __name__ == '__main__':
    app.run(debug=True)

