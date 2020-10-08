# from django.conf.urls import patterns, url
# urlpatterns = patterns('Inventory.views',
#     url(r'^Inventory/$', 'ItemType_list'),
#     url(r'^Inventory/(?P<pk>[0-9]+)/$', 'ItemType_detail'),
# )
from django.urls import include, path
from . import views
urlpatterns = [
    path('itemtype/', views.JSONResponse.ItemType_list, name='Itemtype-view'),
    path('itemtype/<int:itemtype_id>/', views.JSONResponse.ItemType_detail, name='Itemtype-item-view'),
    path('itemtype/rest/', views.JSONResponse.ItemType_rest, name='Itemtype-rest-view'),

    path('item/', views.JSONResponse.Item_list, name='Item-view'),
    path('item/<int:item_id>/', views.JSONResponse.Item_detail, name='Item-item-view'),
    path('item/rest/', views.JSONResponse.Item_rest, name='Item-rest-view'),
]