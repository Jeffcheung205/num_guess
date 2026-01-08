from django.contrib import admin
from .models import Game, GuessHistory

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'attempts', 'max_attempts', 'is_won', 'is_finished']
    list_filter = ['is_won', 'is_finished', 'created_at']
    readonly_fields = ['secret_number', 'created_at']

@admin.register(GuessHistory)
class GuessHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'game', 'guess_number', 'timestamp']
    list_filter = ['timestamp']
