from django.conf import settings
from django.contrib import admin

from isfilled.models import Fills

class FillsAdmin(admin.ModelAdmin):
    list_display = ['name', 'fill', 'model',]

admin.site.register(Fills, FillsAdmin)
