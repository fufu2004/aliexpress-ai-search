import hashlib
import time
import requests
from urllib.parse import urlencode

API_URL = "https://gw.api.taobao.com/router/rest"
APP_KEY = "517514"
APP_SECRET = "ikwGsyb4mcavt2EaiDLSwmohxFfX0AUN"
METHOD = "aliexpress.affiliate.product.query"
VERSION = "2.0"
FORMAT = "json"
SIGN_METHOD = "md5"

def sign_params(params: dict) -> str:
    sorted_items = sorted(params.items())
    base_str = API_SECRET + "".join(f"{k}{v}" for k, v in sorted_items) + API_SECRET
    return hashlib.md5(base_str.encode('utf-8')).hexdigest().upper()

def search_aliexpress(keyword: str, tracking_id: str = "") -> dict:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    params = {
        "method": METHOD,
        "app_key": APP_KEY,
        "sign_method": SIGN_METHOD,
        "timestamp": timestamp,
        "format": FORMAT,
        "v": VERSION,
        "keywords": keyword,
        "trackingId": tracking_id
    }
    params["sign"] = sign_params(params)
    resp = requests.post(API_URL, data=urlencode(params), headers={
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    })
    return resp.json()
