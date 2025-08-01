
import requests

ACCESS_TOKEN = "50000501234qsnZxgvELth0OH7CBxiNu1hImSgXeztmD1B1cca3313ovaRqpjBT0MJYi"

def search_aliexpress(query):
    url = "https://api-sg.aliexpress.com/sync"
    payload = {
        "method": "aliexpress.search",
        "query": query,
        "page": 1,
        "page_size": 5,
        "lang": "he"
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        # סימולציה של תוצאות, החלף בהתאם לפורמט האמיתי של AliExpress API
        return [
            {
                "title": "נעליים שחורות לנשים",
                "url": "https://www.aliexpress.com/item/1005001234567890.html",
                "image": "https://example.com/image.jpg",
                "price": "₪100"
            }
        ]
    except Exception as e:
        print("שגיאה:", e)
        return []
