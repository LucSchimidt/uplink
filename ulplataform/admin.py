from django.contrib import admin
from .models import *

@admin.register(Uplink)
class Uplink(admin.ModelAdmin):
    pass

@admin.register(UplinkTheme)
class UplinkTheme(admin.ModelAdmin):
    pass

