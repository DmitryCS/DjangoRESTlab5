from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect


def get_js(request):
    return HttpResponseRedirect('/player/%s/' % str(1))#render(request, 'static/js/write_message.js')

def site(request):
    return render(request, "templates/list2.html")