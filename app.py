from flask import Flask, request, render_template
from search import search_aliexpress

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query = None
    if request.method == 'POST':
        query = request.form.get('query')
        results = search_aliexpress(query)
    return render_template('index.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
