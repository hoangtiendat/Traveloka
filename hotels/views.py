from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Hotel, Imagehotel
from django.http import JsonResponse
import json

# Create your views here.
def hotel_home(request):
    return render(request, 'hotels/post/home.html')

def hotel_list(request, region):
    hotels = Hotel.objects.filter(region__contains=region)
    return render(request, 'hotels/post/list.html', {'hotels': hotels})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, id=hotel_id)
    return render(request, 'hotels/post/detail.html', {'hotel': hotel})

def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = Hotel.objects.filter(region__contains=q)
        results = []
        for r in search_qs:
            results.append(r.region)
        results = list(set(results))
        data = json.dumps(results)
    else:
        data = 'fail'
    return HttpResponse(data, content_type='application/json')
