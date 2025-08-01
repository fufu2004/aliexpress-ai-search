from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_TOKEN = "50000501234qsnZxgvELth0OH7CBxiNu1hImSgXeztmD1B1cca3313ovaRqpjBT0MJYi"

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('q')
    if not keyword:
        return jsonify({"error": "Missing 'q' parameter"}), 400

    url = "https://api-sg.aliexpress.com/sync_search"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    params = {
        "keywords": keyword,
        "page_size": 10,
        "language": "en"
    }
    response = requests.get(url, headers=headers, params=params)
    try:
        return jsonify(response.json())
    except Exception:
        return response.text

if __name__ == '__main__':
    app.run(debug=True)
