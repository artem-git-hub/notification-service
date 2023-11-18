from django.contrib import admin
from .models import Client, Dispatch, Message


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    pass


@admin.register(Dispatch)
class AdminDispatch(admin.ModelAdmin):
    pass


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    pass
