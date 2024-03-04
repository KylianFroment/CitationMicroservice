from flask import Flask, jsonify
from googleapiclient.discovery import build

app = Flask(__name__)

# Clé API YouTube Data
api_key = 'AIzaSyB2mgKM94utD5IzytXrJHma9-ogejTN6UI'

# Initialisez l'API YouTube Data
youtube = build('youtube', 'v3', developerKey=api_key)

@app.route('/youtube/<track_name>', methods=['GET'])
def get_youtube_url(track_name):
    try:
        # Recherchez une vidéo correspondant au titre de la chanson sur YouTube
        search_response = youtube.search().list(
            q=track_name,
            part='id',
            type='video',
            maxResults=1
        ).execute()

        # Récupérez l'ID de la première vidéo de la réponse
        video_id = search_response['items'][0]['id']['videoId']

        # Construisez l'URL de la vidéo YouTube
        youtube_url = f'https://www.youtube.com/watch?v={video_id}'

        return jsonify({"youtube_url": youtube_url}), 200
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
