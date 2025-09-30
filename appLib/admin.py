from django.contrib import admin
from unfold.admin import ModelAdmin
from appChat.models import *
from appLib.models import *
from appTask.models import *
from unfold.contrib.forms.widgets import WysiwygWidget

@admin.register(FileLibrary)
class FileLibraryAdmin(ModelAdmin):
    list_display=['title', 'description', 'file', 'uploaded_by', 'uploaded_at']
    list_display_links=['title', 'description', 'file', 'uploaded_by', 'uploaded_at']
    list_filter=['title']
    list_per_page=20
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }