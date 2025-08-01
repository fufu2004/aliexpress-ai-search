import requests

ACCESS_TOKEN = "50000501234qsnZxgvELth0OH7CBxiNu1hImSgXeztmD1B1cca3313ovaRqpjBT0MJYi"

def search_aliexpress(query):
    url = "https://gw.api.taobao.com/router/rest"  # לפי המסמך שלך
    params = {
        "method": "aliexpress.affiliate.product.query",
        "app_key": "517514",
        "access_token": ACCESS_TOKEN,
        "keywords": query,
        "fields": "product_title,product_main_image_url,sale_price,promotion_link",
        "format": "json",
        "v": "2.0"
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    products = data.get("resp_result", {}).get("result", {}).get("products", [])
    results = []
    for p in products:
        results.append({
            "title": p.get("product_title"),
            "image": p.get("product_main_image_url"),
            "price": p.get("sale_price"),
            "url": p.get("promotion_link")
        })
    return results
