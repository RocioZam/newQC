from django.contrib import admin
from .models import Qcreport
# Register your models here.


class QcreportAdmin(admin.ModelAdmin):
    search_fields = ['title', 'status']
    list_display = ['id', 'title', 'client', 'status', 'author', 'tecreject', 'date_posted']
    list_editable = ['client', 'status', 'author', 'tecreject', 'date_posted']

admin.site.register(Qcreport, QcreportAdmin)