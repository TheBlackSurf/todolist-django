from django.contrib import admin
from .models import Task, Settings

admin.site.register(Task)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    '''Admin View for Settings'''

    list_display = ('title', 'hcode', 'fcode', 'styles')

    