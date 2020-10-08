from django.contrib import admin
from Messages.models import Message


# Register your models here.
class Message_Admin(admin.ModelAdmin):
    list_display = ('playerFrom','playerTo', 'messageText',)
    # list_display = ('messageText',)


admin.site.register(Message, Message_Admin)
