
from flask import Flask, request, render_template
from search import search_aliexpress

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_aliexpress(query)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
