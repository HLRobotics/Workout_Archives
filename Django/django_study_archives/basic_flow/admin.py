from django.contrib import admin
from .import models

class NotesAdmin(admin.ModelAdmin):
    list_display=('title',)
    pass

admin.site.register(models.notes,NotesAdmin)