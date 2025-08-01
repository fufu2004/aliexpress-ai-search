
import requests

ACCESS_TOKEN = "50000501234qsnZxgvELth0OH7CBxiNu1hImSgXeztmD1B1cca3313ovaRqpjBT0MJYi"

def search_aliexpress(query):
    url = "https://api.aliexpress.com/search"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    params = {
        "q": query,
        "language": "he",
        "currency": "USD",
        "page": 1
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get('items', [])
    except Exception as e:
        return [{"title": "שגיאה בעת הבקשה", "error": str(e)}]
