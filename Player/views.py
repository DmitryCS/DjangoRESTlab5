from django.shortcuts import render
from django.http import HttpResponse
from .models import Player
from django.http import Http404, HttpResponseRedirect
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def player_list(request):
    # print(request.user.username)
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/accounts/login/' )#reverse('accounts:login'))
    # else:
    player_list = Player.objects.all()
    return render(request, 'player/list.html', {'player_list':player_list})

@login_required
def player_detail(request, player_id):
    try:
        a = Player.objects.get(id = player_id)
    except:
        raise Http404("Локация не найдена")
    return render(request, "player/detail.html", {'player': a})

@login_required
def player_redirect(request):
    try:
        player_id = Player.objects.get(name=request.user.username).id
    except:
        raise Http404("Игрок не найден")
    return HttpResponseRedirect('/player/%s/' % str(player_id))#render(request, "player/detail2.html", {'player': a})


@login_required
def player_get_id(request):
    try:
        player_id = Player.objects.get(name=request.user.username).id
    except:
        raise Http404("Игрок не найден")
    responseData = {
        'player_id': player_id
    }
    return HttpResponse(json.dumps(responseData), content_type='application/json')#HttpResponseRedirect('/player/%s/' % str(player_id))#render(request, "player/detail2.html", {'player': a})