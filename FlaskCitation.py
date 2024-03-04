from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

def fetch_quote(author=None):
    # Construire l'URL de l'API
    api_url = "https://zenquotes.io/api/quotes"
    # Si un auteur est spécifié, ajouter le paramètre d'auteur à l'URL de l'API
    if author:
        api_url += f"?author={author}"
    # Faire une requête GET à l'API et stocker la réponse
    response = requests.get(api_url)
    # Vérifier le statut de la réponse
    if response.status_code == 200:
        # Extraire la citation et l'auteur
        data = response.json()
        if data:
            quote = data[0]["q"]
            author = data[0]["a"]
            return quote, author
    return None, None

@app.route('/citation', methods=['GET'])
def get_citation():
    # Récupérer le paramètre d'auteur de la requête
    author = request.args.get('auteur')
    # Récupérer la citation et l'auteur
    quote, author = fetch_quote(author)
    if quote and author:
        # Retourner la citation et l'auteur sous forme de JSON
        return jsonify({"citation": quote, "auteur": author}), 200
    else:
        # Retourner un message d'erreur si la citation n'a pas pu être récupérée
        return jsonify({"erreur": "Impossible de récupérer la citation"}), 500

@app.route('/citation.html', methods=['GET'])
def get_citation_html():
    # Récupérer le paramètre d'auteur de la requête
    author = request.args.get('auteur')
    # Récupérer la citation et l'auteur
    quote, author = fetch_quote(author)
    if quote and author:
        # Rendre le template HTML avec la citation et l'auteur
        return render_template('citation.html', citation=quote, auteur=author)
    else:
        # Retourner une page d'erreur si la citation n'a pas pu être récupérée
        return render_template('error.html', message="Impossible de récupérer la citation"), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
