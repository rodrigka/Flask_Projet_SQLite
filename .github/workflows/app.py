from flask import Flask, request, jsonify
import sqlite3


app = Flask(__name__)

# Route pour rechercher un client par nom
@app.route('/fiche_nom/', methods=['GET'])
def recherche_par_nom():
    nom_client = request.args.get('nom')  # Obtenez le paramètre 'nom' de l'URL
    if nom_client:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM clients WHERE nom = ?", (nom_client,))
        resultats = c.fetchall()
        conn.close()
        if resultats:
            return jsonify(resultats)
        else:
            return "Aucun client trouvé avec ce nom", 404
    else:
        return "Veuillez spécifier un nom de client", 400
