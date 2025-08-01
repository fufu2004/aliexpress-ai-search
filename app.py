from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "האפליקציה שלך עובדת! 🚀"

@app.route('/search')
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Missing query parameter"}), 400
    # כאן תהיה קריאה ל־AliExpress API או תוצאה מזויפת
    return jsonify({"results": [f"Fake result for '{query}'"]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
