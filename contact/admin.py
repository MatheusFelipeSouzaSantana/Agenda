from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'firts_name', 'last_name', 'phone',
    ordering = '-id',
    search_fields = 'id', 'first_name', 'last_name',
