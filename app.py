from flask import Flask, render_template, request
from search import search_aliexpress

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    if request.method == "POST":
        q = request.form.get("query")
        data = search_aliexpress(q)
        results = data.get("result", {}).get("products", [])
    return render_template("index.html", results=results)
