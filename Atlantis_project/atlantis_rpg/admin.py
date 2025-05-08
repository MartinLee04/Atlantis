from django.contrib import admin
from .models import Player, Narrative

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'health', 'location', 'created_at')
    search_fields = ('name',)

@admin.register(Narrative)
class NarrativeAdmin(admin.ModelAdmin):
    list_display = ('location', 'description')
    search_fields = ('location', 'description')
