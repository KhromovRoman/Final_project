from django.contrib import admin
from unfold.admin import ModelAdmin
from appAuth.models import Employees
from appChat.models import *
from appLib.models import *
from appTask.models import *
from unfold.contrib.forms.widgets import WysiwygWidget

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display=['second_name', 'first_name','third_name', 'position', 'phone_number', 'e_mail', 'password_changed', 'status', 'date_created', 'date_updated']
    list_display_links=['second_name', 'first_name','third_name', 'position', 'phone_number', 'e_mail', 'status', 'date_created', 'date_updated']
    list_filter=['status']
    list_per_page=20
    list_filter_sheet = True
    list_fullwidth = True
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
