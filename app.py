from flask import Flask, request, jsonify
from search import search_aliexpress_products

app = Flask(__name__)

ACCESS_TOKEN = "50000501234qsnZxgvELth0OH7CBxiNu1hImSgXeztmD1B1cca3313ovaRqpjBT0MJYi"

@app.route("/")
def home():
    return "AliExpress AI Search App"

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Missing query parameter 'q'"}), 400
    data = search_aliexpress_products(query, ACCESS_TOKEN)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)