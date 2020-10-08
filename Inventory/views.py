from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Inventory.models import ItemType
from Inventory.serializers import ItemTypeSerializer


# Create your views here.
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
    def ItemType_list(request):
        """
        Отобразить все коды ItemTypes, или создать новый ItemType.
        """
        if request.method == 'GET':
            snippets = ItemType.objects.all()
            serializer = ItemTypeSerializer(snippets, many=True)
            return JSONResponse(serializer.data)
            # return render(request, 'inventory/list2.html')
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ItemTypeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

    @login_required
    @csrf_exempt
    def ItemType_detail(request, inventory_id):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            itemType = ItemType.objects.get(pk=inventory_id)
        except ItemType.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            serializer = ItemTypeSerializer(itemType)
            return JSONResponse(serializer.data)
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ItemTypeSerializer(itemType, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)
        elif request.method == 'DELETE':
            itemType.delete()
            return HttpResponse(status=204)

    @login_required
    @csrf_exempt
    def ItemType_rest(request):
        return render(request, 'inventory/list_itemtype.html')
