from django.urls import path
from . import views

app_name = 'player'
urlpatterns = [
    path('', views.player_list, name='index'),
    path('<int:player_id>/', views.player_detail, name='detail'),
    path('temp/', views.player_redirect, name='redirect'),
    path('temp2/', views.player_get_id, name='redirect'),
]