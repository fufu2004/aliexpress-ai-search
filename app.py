from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    # כאן תכניס את הלוגיקה של חיפוש באלי אקספרס עם API
    return jsonify({'results': [
        {'title': 'דוגמה 1', 'url': 'https://example.com/item1'},
        {'title': 'דוגמה 2', 'url': 'https://example.com/item2'}
    ]})
