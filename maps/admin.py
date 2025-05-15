from django.contrib import admin
from .models import Map

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'public', 'created_at')
    list_filter = ('public', 'created_at')
    search_fields = ('name', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('name', 'owner', 'public')}),
        ('Layout', {'fields': ('layout',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )