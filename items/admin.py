from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'modified', 'image_original')


admin.site.register(Item, ItemAdmin)
