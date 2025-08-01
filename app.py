from flask import Flask, render_template, request
from search import search_aliexpress

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results = search_aliexpress(query)
        return render_template('index.html', query=query, results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
