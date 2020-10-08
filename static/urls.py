from django.urls import path
from . import views

app_name = 'static'
urlpatterns = [
    path('js/write_message.js/', views.get_js, name='index'),
    path('html/list2.html/', views.site, name='site-js'),
    # path('<int:player_id>/', views.player_detail, name='detail'),
    # path('temp/', views.player_redirect, name='redirect'),
]