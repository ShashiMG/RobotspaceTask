from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

TMDB_API_KEY = "75290d132cfe02ab7e0e5bce57e5562e"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search_movies():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'No query provided'})

    response = requests.get(f'https://api.themoviedb.org/3/search/movie',
                            params={'api_key': TMDB_API_KEY, 'query': query})

    if response.status_code == 200:
        data = response.json()
        results = data.get('results', [])
        return jsonify({'results': results})
    else:
        return jsonify({'error': 'Error fetching data'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
