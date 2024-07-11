import requests
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from rest_framework.views import APIView

@api_view(['GET'])
def get_top_products(request, category):
    url = 'http://20.244.56.144/test/companies/AMZ/categories/Laptop/products'
    params = {
        'top': request.GET.get('n', '10'),
        'minPrice': request.GET.get('minPrice', '1'),
        'maxPrice': request.GET.get('maxPrice', '10000'),
        'page': request.GET.get('page', '1'),
        'sort_by': request.GET.get('sort_by', 'rating'),
        'sort_order': request.GET.get('sort_order', 'desc')
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad status codes
        data = response.json()

        # Pagination logic
        n = int(params['top'])
        paginator = Paginator(data['products'], n)
        paginated_products = paginator.get_page(int(params['page']))

        return JsonResponse({"products": list(paginated_products)}, safe=False)
    
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error accessing API: {str(e)}", status=500)

@api_view(['GET'])
def get_product_details(request, category, product_id):
    url = f'http://20.244.56.144/test/companies/AMZ/categories/Laptop/products/{product_id}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad status codes
        product_details = response.json()

        return JsonResponse(product_details)
    
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Product details not found for ID {product_id}"}, status=404)
class ProductListView(APIView):
    def get(self, request):
        category = request.GET.get('category', None)
        products = fetch_products(category)

        if products is None:
            return JsonResponse({"error": "Products not found"}, status=404)

        # Serialize your products data if needed
        serialized_products = [product.to_json() for product in products]

        return JsonResponse(serialized_products, safe=False)