from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.JSONResponse.Messages_list, name='Messages-view'),
    path('<int:message_id>/', views.JSONResponse.Messages_detail, name='Message-item-view'),
    path('rest/', views.JSONResponse.Messages_rest, name='Message-item-view'),
]