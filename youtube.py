from flask import Flask, render_template, request, jsonify
from googleapiclient.discovery import build

app = Flask(__name__)


# Clé API YouTube Data
api_key = 'AIzaSyAzycTU0Au65krEZCJp5-DX_7RCvWwam-s'

# Initialisez l'API YouTube Data
youtube = build('youtube', 'v3', developerKey=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        type='video',
        maxResults=10
    ).execute()
    results = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        title = item['snippet']['title']  # Récupérer le titre de la vidéo
        thumbnail = item['snippet']['thumbnails']['default']['url']
        url = f'https://www.youtube.com/watch?v={video_id}'
        results.append({'url': url, 'thumbnail': thumbnail, 'title': title})
    return jsonify({'youtube_results': results})

if __name__ == '__main__':
    app.run(debug=True)