from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def your_view_function(request):
    url = 'http://20.244.56.144/test/companies/AMZ/categories/Laptop/products'
    params = {
        'top': '10',
        'minPrice': '1',
        'maxPrice': '10000'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad status codes

        # Assuming the response is JSON
        data = response.json()
        return JsonResponse(data)

    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error accessing API: {str(e)}", status=500)
