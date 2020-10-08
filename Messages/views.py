from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Messages.models import Message
from Messages.serializers import MessageSerializer

import requests
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required
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
    def Messages_list(request):
        """
        Отобразить все коды ItemTypes, или создать новый ItemType.
        """
        # print(request)
        # print(type(request))
        # print(dir(request))
        # print(request.POST)
        if request.method == 'GET':
            snippets = Message.objects.all()
            serializer = MessageSerializer(snippets, many=True)
            # return render(request, 'messages/list2.html')
            return JSONResponse(serializer.data)
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            print(data)
            serializer = MessageSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        # return render(request, 'messages/list2.html')

    @login_required
    @csrf_exempt
    def Messages_detail(request, message_id):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            message = Message.objects.get(pk=message_id)
        except Message.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'GET':
            serializer = MessageSerializer(message)
            return JSONResponse(serializer.data)
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = MessageSerializer(message, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)
        elif request.method == 'DELETE':
            message.delete()
            return HttpResponse(status=204)

    @login_required
    @csrf_exempt
    def Messages_rest(request):
        return render(request, 'messages/list.html')