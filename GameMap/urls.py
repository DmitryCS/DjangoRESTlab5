from django.urls import path
from . import views

app_name = 'location'
urlpatterns = [
    path('', views.JSONResponse.location_list, name='index'),
    path('<int:location_id>/', views.JSONResponse.location_detail, name='detail'),
    path('rest/', views.JSONResponse.location_rest, name='index'),
]