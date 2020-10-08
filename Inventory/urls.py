# from django.conf.urls import patterns, url
# urlpatterns = patterns('Inventory.views',
#     url(r'^Inventory/$', 'ItemType_list'),
#     url(r'^Inventory/(?P<pk>[0-9]+)/$', 'ItemType_detail'),
# )
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.JSONResponse.ItemType_list, name='Inventory-view'),
    path('<int:inventory_id>/', views.JSONResponse.ItemType_detail, name='Inventory-item-view'),
    path('rest/', views.JSONResponse.ItemType_rest, name='Inventory-view'),
    # path('Inventory/', include('Inventory.urls')),
]