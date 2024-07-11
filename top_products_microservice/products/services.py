from django.conf import settings
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import requests

def fetch_products(category):
    headers = {
        'Authorization': f'Bearer {settings.AUTH_TOKEN}'
    }
    products = []
    
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount('https://', adapter)

    for url in settings.E_COMMERCE_API_URLS:
        try:
            response = session.get(f"{url}/categories/{category}/products", headers=headers)
            response.raise_for_status()
            products.extend(response.json().get("products", []))
            break
        except requests.exceptions.RequestException as e:
            print(f"Error fetching products from {url}: {e}")
            continue

    return products

def fetch_product_details(product_id):
    headers = {
        'Authorization': f'Bearer {settings.AUTH_TOKEN}'
    }
    
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount('https://', adapter)

    for url in settings.E_COMMERCE_API_URLS:
        try:
            response = session.get(f"{url}/products/{product_id}", headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching product details from {url}: {e}")
            continue

    return None
