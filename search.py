import requests

def search_aliexpress_products(keyword, access_token):
    url = "https://api.aliexpress.com/v1/search"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "q": keyword,
        "page": 1,
        "page_size": 10
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()