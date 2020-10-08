from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from GameMap.models import Location
from GameMap.serializers import LocationSerializer

from .models import Location
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# @csrf_exempt
# def location_list(request):
#     """
#     Отобразить все коды ItemTypes, или создать новый ItemType.
#     """
#     if request.method == 'GET':
#         snippets = ItemType.objects.all()
#         serializer = ItemTypeSerializer(snippets, many=True)
#         return serializer.data
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ItemTypeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return serializer.data
#     return HttpResponse("Привет мир!")
    # return serializer.errors


class JSONResponse(HttpResponse):
    '''
    HttpResponse, который отображает его содержимое в JSON.
    '''
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    @login_required
    @csrf_exempt
    def location_list(request):
        """
        Отобразить все коды ItemTypes, или создать новый ItemType.
        """
        if request.method == 'GET':
            snippets = Location.objects.all()
            serializer = LocationSerializer(snippets, many=True)
            return JSONResponse(serializer.data)
            # return render(request, 'inventory/list2.html')
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = LocationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

    @login_required
    @csrf_exempt
    def location_detail(request, location_id):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            location = Location.objects.get(pk=location_id)
        except Location.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            serializer = LocationSerializer(location)
            return JSONResponse(serializer.data)
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = LocationSerializer(location, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)
        elif request.method == 'DELETE':
            location.delete()
            return HttpResponse(status=204)

    @login_required
    @csrf_exempt
    def location_rest(request):
        return render(request, 'location/list.html')

'''    
@login_required
def location_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/' )#reverse('accounts:login'))
    else:
        locations_list = Location.objects.all()
        return render(request, 'location/list2.html', {'locations_list':locations_list})
    # return HttpResponse("Привет мир!")

@login_required
def detail(request, location_id):
    try:
        a = Location.objects.get(id = location_id)
    except:
        raise Http404("Локация не найдена")
    return render(request, "location/detail2.html", {'location': a})

@login_required
def location_rest(request):
    return render(request, "location/detail2.html") 
'''