from flask import Flask,jsonify, render_template, request
import requests
import random

app = Flask(__name__)

# Quotable API base URL
QUOTABLE_API_URL = "https://api.quotable.io"

def get_random_quote():
    response = requests.get(f"{QUOTABLE_API_URL}/random")
    if response.status_code == 200:
        quote_data = response.json()
        return quote_data["content"], quote_data["author"]
    else:
        return None

def get_quote_of_the_day():
    # Implement your logic to get the quote of the day (e.g., rotate daily quotes)
    # For now, let's return a hardcoded quote:
    return "Carpe diem!", "Horace"

def get_random_quote_by_author(author):
    response = requests.get(f"{QUOTABLE_API_URL}/random?author={author}")
    if response.status_code == 200:
        quote_data = response.json()
        return quote_data["content"]
    else:
        return None

@app.route('/random_quote', methods=['GET'])
def random_quote():
    quote, author = get_random_quote()
    if quote:
        return f"Random Quote: '{quote}' - {author}"
    else:
        return "Error fetching random quote"

@app.route('/quote_of_the_day', methods=['GET'])
def quote_of_the_day():
    quote, author = get_quote_of_the_day()
    if quote:
        return jsonify({"quote": quote, "author": author})
    else:
        return jsonify({"error": "Error fetching quote of the day"}), 500

@app.route('/random_quote_by_author', methods=['GET'])
def random_quote_by_author():
    author = request.args.get('author')
    quote = get_random_quote_by_author(author)
    if quote:
        return f"Random Quote by {author}: '{quote}'"
    else:
        return f"No quotes found for author '{author}'"

@app.route('/list_author', methods=['GET'])
def list_author():
    response = requests.get(f"{QUOTABLE_API_URL}/authors?sortBy=name")
    if response.status_code == 200:
        authors = response.json()
        return jsonify(authors)
    else:
        return jsonify({"error": "Error fetching authors"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)
