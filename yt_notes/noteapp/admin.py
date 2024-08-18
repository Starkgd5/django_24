from django.contrib import admin

from .models import Note


# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created', 'updated']
    readonly_fields = ['slug']
