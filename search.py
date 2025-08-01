
import requests
import json

API_SECRET = "50000501234qsnZxgvELth0OH7CBxiNu1hImSgXeztmD1B1cca3313ovaRqpjBT0MJYi"
REFRESH_TOKEN = "50001500a34Og47gApXQthhYKUDIxEUrkbEjy3Ms2dIEOj1dd97a83vkq0BWqYVt1YY2"
SELLER_ID = "190149925"
USER_NICK = "il1068995306"

def search_aliexpress(query):
    url = f"https://api-someproxy.com/search?query={query}&access_token={API_SECRET}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('results', [])
        else:
            return [f"שגיאה מהשרת: {response.status_code}"]
    except Exception as e:
        return [f"שגיאה בביצוע הבקשה: {str(e)}"]
