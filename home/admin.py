from django.contrib import admin
from .models import Update
from . import models

# Register your models here.
class UpdateAdmin(admin.ModelAdmin):
    update_display = ('heading_update')

admin.site.register(Update, UpdateAdmin)
