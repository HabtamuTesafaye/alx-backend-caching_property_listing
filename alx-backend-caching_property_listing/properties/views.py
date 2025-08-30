from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)  # 15 minutes
def property_list(request):
    properties = get_all_properties()
    data = [{"id": p.id, "title": p.title, "price": str(p.price)} for p in properties]
    return JsonResponse(data, safe=False)
