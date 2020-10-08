from django.contrib import admin
from Inventory.models import Item
from Inventory.models import ItemType

# admin.site.register(Item)
# admin.site.register(ItemType)
# Register your models here.
class Item_Admin(admin.ModelAdmin):
    list_display = ('itemType','quality', 'owner',)

class ItemType_Admin(admin.ModelAdmin):
    list_display = ('type', )

admin.site.register(Item, Item_Admin)
admin.site.register(ItemType, ItemType_Admin)

