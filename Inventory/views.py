from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Inventory.models import ItemType, Item
from Inventory.serializers import ItemTypeSerializer, ItemSerializer


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
    def ItemType_detail(request, itemtype_id):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            itemType = ItemType.objects.get(pk=itemtype_id)
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




    @login_required
    @csrf_exempt
    def Item_list(request):
        """
        Отобразить все коды Item, или создать новый Item.
        """
        if request.method == 'GET':
            snippets = Item.objects.all()
            serializer = ItemSerializer(snippets, many=True)
            return JSONResponse(serializer.data)
            # return render(request, 'inventory/list2.html')
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ItemSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

    @login_required
    @csrf_exempt
    def Item_detail(request, item_id):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            serializer = ItemSerializer(item)
            return JSONResponse(serializer.data)
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ItemSerializer(item, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)
        elif request.method == 'DELETE':
            item.delete()
            return HttpResponse(status=204)

    @login_required
    @csrf_exempt
    def Item_rest(request):
        return render(request, 'inventory/list_item.html')