# Importer les modules nécessaires
import requests
import json

# Définir l'URL de l'API
api_url = "https://zenquotes.io/api/random"

# Faire une requête GET à l'API et stocker la réponse
response = requests.get(api_url)

# Vérifier le statut de la réponse
if response.status_code == 200:
  # Convertir la réponse en JSON
  data = json.loads(response.text)
  # Extraire la citation et l'auteur
  quote = data[0]["q"]
  author = data[0]["a"]
  # Afficher la citation du jour
  print(f"Citation du jour : {quote} - {author}")
else:
  # Afficher un message d'erreur
  print(f"Erreur : {response.status_code}")
